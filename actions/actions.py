from typing import Any, Dict, List
import json
import logging

import websockets
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)

EMOTION_RESPONSES: Dict[str, Dict[str, str]] = {
    "greet": {
        "response": "¡Hola! Qué gusto verte otra vez. Estoy aquí para ayudarte en lo que necesites.",
        "emotion": "smile",
    },
    "goodbye": {
        "response": "Fue un placer conversar contigo. ¡Hasta pronto!",
        "emotion": "neutral",
    },
    "mood_happy": {
        "response": "¡Qué alegría escucharlo! Vamos a aprovechar toda esa energía positiva.",
        "emotion": "smile",
    },
    "mood_sad": {
        "response": "Siento que estés pasando por un momento difícil. Estoy aquí para acompañarte.",
        "emotion": "sad",
    },
    "mood_angry": {
        "response": "Entiendo tu frustración. Respiremos profundo y busquemos una solución juntos.",
        "emotion": "angry",
    },
    "mood_surprised": {
        "response": "¡Wow! ¡Yo también estoy sorprendida! Las sorpresas hacen la vida más interesante.",
        "emotion": "smile",
    },
    "mood_scared": {
        "response": "Entiendo que tengas miedo. Estoy aquí contigo, no estás solo. Todo va a estar bien.",
        "emotion": "sad",
    },
    "mood_confused": {
        "response": "No te preocupes, la confusión es temporal. Vamos paso a paso y encontraremos claridad.",
        "emotion": "neutral",
    },
    "mood_excited": {
        "response": "¡Qué emoción! Tu entusiasmo es contagioso. ¡Vamos a disfrutar este momento!",
        "emotion": "smile",
    },
    "mood_tired": {
        "response": "Parece que necesitas un descanso. Recuerda que cuidarte es importante. ¿Quieres que hablemos de algo relajante?",
        "emotion": "sad",
    },
    "mood_bored": {
        "response": "¡Vamos a cambiar eso! ¿Qué tal si te cuento algo interesante o jugamos un poco?",
        "emotion": "smile",
    },
    "mood_love": {
        "response": "¡Aww! Qué lindo. Yo también te aprecio mucho. Gracias por compartir ese sentimiento conmigo.",
        "emotion": "smile",
    },
    "gratitude": {
        "response": "¡Gracias a ti! Me hace feliz poder ayudarte.",
        "emotion": "smile",
    },
    "help_request": {
        "response": "Puedo orientarte con información, recordatorios y un poco de ánimo. ¿Por dónde comenzamos?",
        "emotion": "neutral",
    },
    "ask_joke": {
        "response": "¿Por qué los programadores prefieren el modo oscuro? ¡Porque la luz atrae bugs! 😄",
        "emotion": "smile",
    },
    "ask_motivation": {
        "response": "¡Tú puedes con esto y mucho más! Cada paso que das te acerca a tus metas. ¡Sigue adelante, campeón!",
        "emotion": "smile",
    },
    "ask_weather": {
        "response": "No tengo acceso al clima en tiempo real, pero espero que sea un día hermoso para ti. ¿Cómo está el clima por allá?",
        "emotion": "neutral",
    },
    "ask_name": {
        "response": "Me llamo MAIKA, tu asistente virtual. Es un placer conocerte mejor.",
        "emotion": "smile",
    },
    "ask_how_are_you": {
        "response": "¡Estoy muy bien, gracias por preguntar! Lista para ayudarte. ¿Y tú cómo estás?",
        "emotion": "smile",
    },
    "compliment": {
        "response": "¡Ay, qué lindo! Muchas gracias. Tú también eres increíble. Me alegra que trabajemos juntos.",
        "emotion": "smile",
    },
    "insult": {
        "response": "Entiendo que puedas estar frustrado, pero estoy aquí para ayudarte. ¿Hay algo que pueda hacer mejor?",
        "emotion": "sad",
    },
    "ask_age": {
        "response": "Soy una IA, así que no tengo edad en el sentido tradicional. ¡Pero siempre estoy aprendiendo cosas nuevas!",
        "emotion": "neutral",
    },
    "ask_capabilities": {
        "response": "Puedo conversar contigo, reconocer tus emociones, contarte chistes, motivarte y mucho más. ¡Estoy aquí para lo que necesites!",
        "emotion": "smile",
    },
}

DEFAULT_RESPONSE = {
    "response": "¡Estoy aquí para apoyarte! Cuéntame un poco más y buscaremos la mejor respuesta.",
    "emotion": "neutral",
}


class ActionSendToUnity(Action):
    def name(self) -> str:
        return "action_send_to_unity"

    async def _send_async(self, message_data: Dict[str, Any]) -> None:
        uri = "ws://localhost:5050"  # Debe coincidir con Unity
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(message_data))

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        intent_name = tracker.latest_message.get("intent", {}).get("name")
        payload = EMOTION_RESPONSES.get(intent_name, DEFAULT_RESPONSE)

        try:
            await self._send_async(payload)
        except Exception as exc:
            logger.exception("No se pudo enviar el mensaje a Unity: %s", exc)

        dispatcher.utter_message(text=payload["response"])
        return []
