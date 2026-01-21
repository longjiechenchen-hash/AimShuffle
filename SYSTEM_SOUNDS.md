## AimShuffle - Sistema de Sonidos

### Resumen de Cambios

Se ha agregado un **sistema completo de sonidos** al juego AimShuffle:

### Archivos Nuevos Creados:

1. **[src/audio.py](src/audio.py)** - Módulo gestor de sonidos
   - Carga y reproduce efectos de sonido
   - Sistema de activación/desactivación
   - Manejo de errores graceful

2. **[generate_sounds.py](generate_sounds.py)** - Generador de sonidos
   - Crea automáticamente archivos WAV
   - 4 efectos diferentes: click, éxito, inicio, fin
   - Sin dependencias externas complicadas

3. **[SOUNDS.md](SOUNDS.md)** - Documentación de sonidos
   - Guía de personalización
   - Solución de problemas

4. **[setup.py](setup.py)** - Script de configuración rápida
   - Instala dependencias
   - Genera sonidos automáticamente

### Archivos Modificados:

1. **[src/main.py](src/main.py)**
   - Integración del módulo de sonidos
   - Sonidos en: clic correcto, inicio, fin
   - Control M para activar/desactivar sonidos
   - Muestra estado de audio en menú

2. **[requirements.txt](requirements.txt)**
   - Agregado `numpy` y `scipy` para generación de sonidos

3. **[README.md](README.md)**
   - Actualizado con instrucciones de sonidos
   - Nueva tecla: M para sonido ON/OFF

---

## # Cómo Usar

### Setup Rápido (Recomendado):
```bash
python setup.py
```

O manualmente:

### 1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 2. Generar archivos de sonido:
```bash
python generate_sounds.py
```

### 3. Ejecutar juego:
```bash
python src/main.py
```

---

## # Controles de Sonido

| Acción | Tecla |
|--------|-------|
| Alternar Sonido ON/OFF | **M** |
| Ver estado | **Menú Principal** |

Los sonidos se reproducen en:
-  Al hacer clic en número correcto
-  Al iniciar una partida (SPACE)
-  Al completar el juego

---

### Estructura de Sonidos

```
assets/sounds/
├── click.wav       # Beep al hacer clic
├── success.wav     # Sonido de victoria
├── start.wav       # Sonido de inicio
└── game_over.wav   # Sonido de fin
```

Generados automáticamente por `generate_sounds.py`

---

### Personalización

Para cambiar sonidos:

1. Editar `generate_sounds.py`:
   - Cambiar frecuencias (Hz)
   - Ajustar duraciones (segundos)
   - Modificar envelopes (fade)

2. Regenerar:
   ```bash
   python generate_sounds.py
   ```

3. Ejecutar nuevamente

---

### Compilar con Sonidos

```bash
python build.py
```

El ejecutable incluirá automáticamente los archivos de sonido.

**Nota:** Si falta `assets/sounds/`, el juego funciona sin sonidos.

---

### Características del Sistema

-  Sonidos sin latencia
-  Activación/desactivación en tiempo real
-  Manejo de errores graceful
-  Generación automática de sonidos
-  Compatible con PyInstaller
-  Interfaz silenciosa si no hay sonidos

---
