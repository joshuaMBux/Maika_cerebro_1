# MAIKA - Asistente Virtual con Emociones

Bot conversacional en español con reconocimiento de emociones e integración con Unity para expresiones faciales del avatar.

## 🎭 Emociones Disponibles

El avatar soporta 5 expresiones faciales que el bot utiliza según el contexto:

### Emociones del Avatar
- **Sonreír** (`smile`) - Para felicidad, saludos, gratitud, emoción, amor, chistes
- **Enojado** (`angry`) - Para frustración y enojo
- **Triste** (`sad`) - Para tristeza, miedo, cansancio, empatía
- **Neutral** (`neutral`) - Para información general, confusión, clima
- **Hablar** (`talk`) - Para conversación activa (disponible pero no usado por defecto)

El bot reconoce muchas más emociones en el texto del usuario, pero las mapea inteligentemente a estas 5 expresiones disponibles en el avatar.

## 💬 Capacidades del Bot

### Conversación General
- Saludos y despedidas
- Preguntar cómo está el bot
- Preguntar el nombre del bot
- Preguntar la edad
- Preguntar capacidades

### Reconocimiento Emocional
- Detecta 11 estados emocionales diferentes
- Responde con empatía según el contexto
- Adapta su tono a la situación

### Funciones Interactivas
- **Chistes** - Cuenta chistes para alegrar el día
- **Motivación** - Brinda palabras de aliento
- **Consulta del clima** - Interactúa sobre el clima
- **Respuesta a cumplidos** - Agradece los halagos
- **Manejo de insultos** - Responde con empatía

## 🚀 Intenciones Implementadas

| Intención | Descripción | Emoción Avatar |
|-----------|-------------|----------------|
| `greet` | Saludos iniciales | smile |
| `goodbye` | Despedidas | neutral |
| `mood_happy` | Usuario feliz | smile |
| `mood_sad` | Usuario triste | sad |
| `mood_angry` | Usuario enojado | angry |
| `mood_surprised` | Usuario sorprendido | smile |
| `mood_scared` | Usuario asustado | sad |
| `mood_confused` | Usuario confundido | neutral |
| `mood_excited` | Usuario emocionado | smile |
| `mood_tired` | Usuario cansado | sad |
| `mood_bored` | Usuario aburrido | smile |
| `mood_love` | Expresiones de amor | smile |
| `gratitude` | Agradecimientos | smile |
| `help_request` | Solicitud de ayuda | neutral |
| `ask_joke` | Pedir un chiste | smile |
| `ask_motivation` | Pedir motivación | smile |
| `ask_weather` | Preguntar por el clima | neutral |
| `ask_name` | Preguntar nombre | smile |
| `ask_how_are_you` | Preguntar cómo está | smile |
| `compliment` | Hacer cumplidos | smile |
| `insult` | Insultos | sad |
| `ask_age` | Preguntar edad | neutral |
| `ask_capabilities` | Preguntar capacidades | smile |

## 📁 Estructura del Proyecto

```
Flutter_Rasa_Unity_Connection/
├── actions/
│   ├── actions.py          # Lógica de respuestas y emociones
│   └── __init__.py
├── data/
│   ├── nlu.yml             # Ejemplos de entrenamiento (183 líneas)
│   └── stories.yml         # Flujos de conversación (95 líneas)
├── models/                 # Modelos entrenados
├── config.yml              # Configuración del pipeline
├── domain.yml              # Definición de intenciones y acciones
├── endpoints.yml           # Configuración de endpoints
├── RasaReceiver.cs         # Script Unity para recibir emociones
└── test_unty.py           # Script de prueba
```

## 🔧 Configuración

### Pipeline de Rasa
- **Tokenizer**: WhitespaceTokenizer
- **Featurizer**: CountVectorsFeaturizer (word + char n-grams)
- **Classifier**: DIETClassifier (100 epochs)
- **Policies**: MemoizationPolicy, RulePolicy, TEDPolicy

### Integración Unity
El bot se comunica con Unity vía WebSocket en `localhost:5050`, enviando:
```json
{
  "response": "Texto de la respuesta",
  "emotion": "nombre_emocion"
}
```

## 🎮 Uso en Unity

El script `RasaReceiver.cs` maneja las emociones recibidas y las aplica al `AvatarController`.

### Expresiones Soportadas por el Avatar:

```csharp
avatarController.SetExpression("smile");    // Sonreír
avatarController.SetExpression("angry");    // Enojado
avatarController.SetExpression("sad");      // Triste
avatarController.SetExpression("neutral");  // Neutral
avatarController.SetExpression("talk");     // Hablar
```

El bot envía estas emociones vía WebSocket y el avatar las interpreta automáticamente.

## 🧪 Ejemplos de Uso

### Ejemplo 1: Expresar felicidad
**Usuario**: "Estoy muy feliz hoy"  
**MAIKA**: "¡Qué alegría escucharlo! Vamos a aprovechar toda esa energía positiva."  
**Emoción**: smile

### Ejemplo 2: Pedir un chiste
**Usuario**: "Cuéntame un chiste"  
**MAIKA**: "¿Por qué los programadores prefieren el modo oscuro? ¡Porque la luz atrae bugs! 😄"  
**Emoción**: smile

### Ejemplo 3: Expresar miedo
**Usuario**: "Tengo miedo"  
**MAIKA**: "Entiendo que tengas miedo. Estoy aquí contigo, no estás solo. Todo va a estar bien."  
**Emoción**: sad (empatía)

### Ejemplo 4: Pedir motivación
**Usuario**: "Dame motivación"  
**MAIKA**: "¡Tú puedes con esto y mucho más! Cada paso que das te acerca a tus metas. ¡Sigue adelante, campeón!"  
**Emoción**: smile

## 🔄 Entrenamiento del Modelo

Para entrenar el modelo con las nuevas intenciones:

```bash
rasa train
```

Para probar el bot:

```bash
rasa shell
```

Para iniciar el servidor de acciones:

```bash
rasa run actions
```

## 📊 Estadísticas

- **23 intenciones** diferentes
- **5 emociones** del avatar (smile, angry, sad, neutral, talk)
- **183 líneas** de ejemplos de entrenamiento
- **95 líneas** de historias de conversación
- **Idioma**: Español
- **Mapeo inteligente**: El bot reconoce más emociones en el texto pero las adapta a las 5 disponibles

## 🎯 Próximas Mejoras

- [ ] Integrar API de clima real
- [ ] Agregar más chistes variados
- [ ] Implementar memoria de conversaciones
- [ ] Agregar reconocimiento de entidades (nombres, fechas, etc.)
- [ ] Crear respuestas contextuales más complejas
- [ ] Implementar diálogos multi-turno

## 👨‍💻 Autor

Proyecto MAIKA - Asistente Virtual Emocional
