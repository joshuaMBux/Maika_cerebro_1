import asyncio, websockets, json

async def test():
    uri = "ws://localhost:5050"
    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({"response": "Hola", "emotion": "alegre"}))
        print("✅ Enviado")
asyncio.run(test())
