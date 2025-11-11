# Changelog - MAIKA Bot

## [v2.0.0] - Expansión de Capacidades (2025-11-10)

### ✨ Nuevas Características

#### Intenciones Agregadas (16 nuevas)
- `mood_surprised` - Reconoce sorpresa del usuario
- `mood_scared` - Detecta miedo o nerviosismo
- `mood_confused` - Identifica confusión
- `mood_excited` - Reconoce entusiasmo
- `mood_tired` - Detecta cansancio
- `mood_bored` - Identifica aburrimiento
- `mood_love` - Reconoce expresiones de afecto
- `ask_joke` - Cuenta chistes
- `ask_motivation` - Brinda motivación
- `ask_weather` - Responde sobre el clima
- `ask_name` - Responde su nombre
- `ask_how_are_you` - Responde cómo está
- `compliment` - Responde a cumplidos
- `insult` - Maneja insultos con empatía
- `ask_age` - Responde sobre su edad
- `ask_capabilities` - Explica sus capacidades

#### Ejemplos de Entrenamiento
- **128 nuevos ejemplos** agregados en `data/nlu.yml`
- Total: **183 líneas** de ejemplos de entrenamiento
- Cobertura ampliada de variaciones de lenguaje natural

#### Historias de Conversación
- **16 nuevas historias** en `data/stories.yml`
- Total: **95 líneas** de flujos de conversación
- Mejor manejo de contextos diversos

### 🎭 Sistema de Emociones

#### Mapeo Inteligente
- Bot reconoce múltiples estados emocionales
- Mapeo optimizado a las **5 emociones del avatar**:
  - `smile` (56.5% de uso)
  - `neutral` (21.7% de uso)
  - `sad` (17.4% de uso)
  - `angry` (4.3% de uso)
  - `talk` (reservado)

#### Respuestas Contextuales
- **23 respuestas únicas** personalizadas por intención
- Tono empático y natural en español
- Respuestas adaptadas al estado emocional del usuario

### 🔧 Mejoras Técnicas

#### `actions/actions.py`
- Expandido diccionario `EMOTION_RESPONSES` con 23 intenciones
- Mapeo inteligente de emociones complejas a las 5 disponibles
- Respuestas más naturales y contextuales

#### `RasaReceiver.cs`
- Simplificado switch de emociones
- Soporte para variaciones en español e inglés
- Comentarios mejorados para claridad
- Manejo robusto de las 5 emociones del avatar

#### `domain.yml`
- 23 intenciones definidas
- Estructura organizada y escalable

### 📚 Documentación

#### Nuevos Archivos
- **README.md** - Documentación completa del proyecto
  - Descripción de capacidades
  - Tabla de intenciones y emociones
  - Ejemplos de uso
  - Guía de entrenamiento
  - Estadísticas del proyecto

- **MAPEO_EMOCIONES.md** - Guía detallada del mapeo
  - Distribución de emociones
  - Criterios de asignación
  - Instrucciones para modificar
  - Recomendaciones de uso

- **CHANGELOG.md** - Historial de cambios (este archivo)

### 📊 Estadísticas

#### Antes (v1.0.0)
- 7 intenciones
- 4 emociones básicas
- ~55 ejemplos de entrenamiento
- 7 historias

#### Ahora (v2.0.0)
- **23 intenciones** (+229%)
- **5 emociones** optimizadas
- **183 líneas** de ejemplos (+233%)
- **95 líneas** de historias (+1257%)

### 🎯 Capacidades Nuevas

#### Interacción Social
- Responde a cumplidos e insultos
- Comparte información personal (nombre, edad)
- Pregunta por el estado del usuario

#### Entretenimiento
- Cuenta chistes
- Brinda motivación
- Mantiene conversaciones más naturales

#### Reconocimiento Emocional Avanzado
- Detecta 11+ estados emocionales diferentes
- Responde con empatía apropiada
- Adapta tono según el contexto

### 🔄 Compatibilidad

- ✅ Compatible con avatar de 5 emociones
- ✅ Mantiene estructura de proyecto original
- ✅ WebSocket en `localhost:5050`
- ✅ Formato JSON de mensajes sin cambios
- ✅ Integración Unity sin modificaciones adicionales

### 🐛 Correcciones

- Simplificado manejo de emociones en Unity
- Eliminadas emociones no soportadas por el avatar
- Mapeo consistente entre Python y C#

### 📝 Notas de Actualización

Para actualizar desde v1.0.0:

1. Entrenar nuevo modelo:
   ```bash
   rasa train
   ```

2. Reiniciar servidor de acciones:
   ```bash
   rasa run actions
   ```

3. No se requieren cambios en Unity (compatible con código existente)

### 🚀 Próximos Pasos

- [ ] Integrar API de clima real
- [ ] Agregar más chistes variados
- [ ] Implementar memoria de conversaciones
- [ ] Agregar reconocimiento de entidades
- [ ] Crear diálogos multi-turno
- [ ] Implementar emoción "talk" para animación de habla

---

## [v1.0.0] - Versión Inicial

### Características Iniciales
- 7 intenciones básicas
- 4 emociones (smile, angry, sad, neutral)
- Integración Unity vía WebSocket
- Respuestas básicas en español

---

**Mantenido por**: Proyecto MAIKA  
**Última actualización**: 2025-11-10
