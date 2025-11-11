using UnityEngine;
using System;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Net.WebSockets;
using System.Net;
using System.Collections.Generic;

// --- Clase que recibe las emociones desde Rasa y las pasa a AvatarController ---
public class RasaReceiver : MonoBehaviour
{
    private HttpListener httpListener;
    public AvatarController avatarController; // tu script de control facial
    public int port = 5050;
    private bool isRunning = true;

    async void Start()
    {
        await StartWebSocketServer();
    }

    async Task StartWebSocketServer()
    {
        try
        {
            httpListener = new HttpListener();
            httpListener.Prefixes.Add($"http://localhost:{port}/");
            httpListener.Prefixes.Add($"http://127.0.0.1:{port}/");
            httpListener.Prefixes.Add($"http://[::1]:{port}/");
            httpListener.Start();
            Debug.Log($"🌐 Servidor WebSocket escuchando en puerto {port}...");

            while (isRunning)
            {
                try
                {
                    var context = await httpListener.GetContextAsync();
                    Debug.Log($"📥 Petición recibida: {context.Request.HttpMethod} {context.Request.RawUrl}");

                    if (!isRunning) break;

                    if (context.Request.IsWebSocketRequest)
                    {
                        try
                        {
                            var wsContext = await context.AcceptWebSocketAsync(null);
                            var ws = wsContext.WebSocket;
                            Debug.Log("🤖 Cliente Rasa conectado.");
                            await HandleConnection(ws);
                        }
                        catch (NotImplementedException nie)
                        {
                            Debug.LogError($"❌ AcceptWebSocketAsync no está implementado en esta plataforma: {nie.Message}");
                            context.Response.StatusCode = 501;
                            context.Response.Close();
                        }
                    }
                    else
                    {
                        Debug.LogWarning("🙅‍♂️ La petición no es WebSocket; respondiendo 400.");
                        Debug.LogWarning($"   ↳ Url: {context.Request.Url}");
                        Debug.LogWarning($"   ↳ RemoteEndPoint: {context.Request.RemoteEndPoint}");
                        foreach (string headerKey in context.Request.Headers.AllKeys)
                        {
                            string headerValue = context.Request.Headers[headerKey];
                            Debug.LogWarning($"   ↳ Header {headerKey}: {headerValue}");
                        }
                        Debug.LogWarning($"   ↳ ProtocolVersion: {context.Request.ProtocolVersion}");
                        Debug.LogWarning($"   ↳ UserAgent: {context.Request.UserAgent}");
                        context.Response.StatusCode = 400;
                        context.Response.Close();
                    }
                }
                catch (HttpListenerException)
                {
                    break;
                }
                catch (ObjectDisposedException)
                {
                    break;
                }
                catch (Exception ex)
                {
                    Debug.LogError($"⚠️ Error en servidor WebSocket: {ex.Message}");
                }
            }

            Debug.Log("🛑 Servidor WebSocket detenido correctamente.");
        }
        catch (Exception e)
        {
            Debug.LogError($"❌ Error iniciando el servidor WebSocket: {e.Message}");
        }
    }

    async Task HandleConnection(WebSocket ws)
    {
        var buffer = new byte[1024 * 4];
        while (isRunning && ws.State == WebSocketState.Open)
        {
            try
            {
                var result = await ws.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);

                if (result.MessageType == WebSocketMessageType.Close)
                {
                    await ws.CloseAsync(WebSocketCloseStatus.NormalClosure, string.Empty, CancellationToken.None);
                }
                else
                {
                    string message = Encoding.UTF8.GetString(buffer, 0, result.Count);
                    Debug.Log("📨 Mensaje recibido desde Rasa: " + message);
                    ProcessMessage(message);
                }
            }
            catch (Exception ex)
            {
                Debug.LogWarning($"🔌 Conexión finalizada: {ex.Message}");
                break;
            }
        }
    }

    [System.Serializable]
    public class RasaMessage
    {
        public string response;
        public string emotion;
    }

    void ProcessMessage(string json)
    {
        try
        {
            RasaMessage data = JsonUtility.FromJson<RasaMessage>(json);
            string emotion = data.emotion.ToLower();

            Debug.Log($"🎭 Emoción recibida: {emotion}");

            // Avatar solo soporta: Sonreír, Enojado, Triste, Neutral, Hablar
            switch (emotion)
            {
                case "smile":
                case "sonreir":
                case "alegre":
                case "feliz":
                    avatarController.SetExpression("smile");
                    break;
                case "angry":
                case "enojado":
                    avatarController.SetExpression("angry");
                    break;
                case "sad":
                case "triste":
                    avatarController.SetExpression("sad");
                    break;
                case "talk":
                case "hablar":
                case "speaking":
                    avatarController.SetExpression("talk");
                    break;
                case "neutral":
                default:
                    avatarController.SetExpression("neutral");
                    break;
            }
        }
        catch (Exception e)
        {
            Debug.LogError("❌ Error procesando JSON: " + e.Message);
        }
    }

    private void OnApplicationQuit()
    {
        try
        {
            isRunning = false;

            if (httpListener != null && httpListener.IsListening)
            {
                httpListener.Stop();
                httpListener.Close();
            }

            Debug.Log("✅ Listener detenido sin errores.");
        }
        catch (Exception e)
        {
            Debug.LogWarning($"⚠️ Error al cerrar el servidor: {e.Message}");
        }
    }
}
