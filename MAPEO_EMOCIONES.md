# Mapeo de Emociones - MAIKA

## 🎭 Emociones del Avatar (5 disponibles)

El avatar en Unity soporta únicamente estas 5 expresiones faciales:

1. **Sonreír** (`smile`)
2. **Enojado** (`angry`)
3. **Triste** (`sad`)
4. **Neutral** (`neutral`)
5. **Hablar** (`talk`)

## 🔄 Mapeo Inteligente de Intenciones

El bot reconoce 23 intenciones diferentes del usuario y las mapea a las 5 emociones disponibles:

### 😊 SMILE (Sonreír)
Usado para expresiones positivas, alegría y entusiasmo:
- `greet` - Saludos
- `mood_happy` - Felicidad
- `mood_surprised` - Sorpresa
- `mood_excited` - Emoción/Entusiasmo
- `mood_bored` - Aburrimiento (respuesta animada)
- `mood_love` - Amor/Afecto
- `gratitude` - Agradecimiento
- `ask_joke` - Chistes
- `ask_motivation` - Motivación
- `ask_name` - Presentación
- `ask_how_are_you` - Pregunta sobre el bot
- `compliment` - Cumplidos
- `ask_capabilities` - Capacidades

**Total: 13 intenciones → smile**

### 😠 ANGRY (Enojado)
Usado para frustración y enojo:
- `mood_angry` - Enojo/Frustración

**Total: 1 intención → angry**

### 😢 SAD (Triste)
Usado para tristeza, empatía y situaciones difíciles:
- `mood_sad` - Tristeza
- `mood_scared` - Miedo (empatía)
- `mood_tired` - Cansancio (empatía)
- `insult` - Insultos (respuesta empática)

**Total: 4 intenciones → sad**

### 😐 NEUTRAL (Neutral)
Usado para información general y estados neutrales:
- `goodbye` - Despedida
- `mood_confused` - Confusión
- `help_request` - Solicitud de ayuda
- `ask_weather` - Clima
- `ask_age` - Edad

**Total: 5 intenciones → neutral**

### 🗣️ TALK (Hablar)
Disponible pero no usado por defecto. Puede activarse manualmente si se desea mostrar al avatar hablando durante las respuestas.

**Total: 0 intenciones → talk (reservado para uso futuro)**

## 📊 Distribución de Emociones

```
smile:   13 intenciones (56.5%)
neutral:  5 intenciones (21.7%)
sad:      4 intenciones (17.4%)
angry:    1 intención   (4.3%)
talk:     0 intenciones (0%)
```

## 🎯 Lógica del Mapeo

### Criterios de Asignación:

**SMILE** → Situaciones positivas, alegres, motivadoras o de conexión emocional positiva

**ANGRY** → Solo frustración y enojo explícito del usuario

**SAD** → Situaciones que requieren empatía, apoyo emocional o comprensión

**NEUTRAL** → Información objetiva, estados indefinidos o transiciones

**TALK** → Reservado para animación de habla (puede implementarse en el futuro)

## 🔧 Cómo Modificar el Mapeo

Para cambiar qué emoción se muestra para una intención específica:

1. Edita `actions/actions.py`
2. Busca la intención en el diccionario `EMOTION_RESPONSES`
3. Cambia el valor de `"emotion"` a una de las 5 disponibles: `smile`, `angry`, `sad`, `neutral`, `talk`

Ejemplo:
```python
"ask_joke": {
    "response": "¿Por qué los programadores prefieren el modo oscuro? ¡Porque la luz atrae bugs! 😄",
    "emotion": "smile",  # ← Cambiar aquí
},
```

## 💡 Recomendaciones

- **SMILE** es la emoción más versátil y positiva, úsala para la mayoría de interacciones amigables
- **SAD** funciona bien para mostrar empatía sin ser demasiado negativo
- **ANGRY** úsalo con moderación, solo cuando el usuario exprese frustración real
- **NEUTRAL** es perfecto para información objetiva
- **TALK** puede activarse programáticamente cuando el avatar esté respondiendo

## 🚀 Expansión Futura

Si el avatar recibe más expresiones faciales en el futuro, puedes:

1. Agregar nuevas emociones al diccionario en `actions.py`
2. Actualizar el switch en `RasaReceiver.cs`
3. Redistribuir las intenciones según las nuevas emociones disponibles
4. Actualizar este documento de mapeo

---

**Nota**: Este mapeo está optimizado para las 5 emociones actuales del avatar, priorizando una experiencia de usuario positiva y empática.
