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
    "gratitude": {
        "response": "¡Gracias a ti! Me hace feliz poder ayudarte.",
        "emotion": "smile",
    },
    "help_request": {
        "response": "Puedo orientarte con información, recordatorios y un poco de ánimo. ¿Por dónde comenzamos?",
        "emotion": "neutral",
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
