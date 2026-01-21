# 🔊 Guía de Sonidos - AimShuffle

## Inicio Rápido

### Opción 1: Generar sonidos automáticamente (Recomendado)

```bash
python generate_sounds.py
```

Esto crea 4 archivos de sonido en `assets/sounds/`:
- `click.wav` - Sonido al hacer clic en un número correcto
- `success.wav` - Sonido al completar el juego
- `start.wav` - Sonido al iniciar una partida
- `game_over.wav` - Sonido de final de juego

### Opción 2: Usar sonidos personalizados

Coloca tus propios archivos WAV en `assets/sounds/` con los nombres anteriores.

---

## Sonidos Incluidos

| Archivo | Momento | Descripción |
|---------|---------|------------|
| `click.wav` | Al hacer clic correcto | Beep corto y agudo |
| `success.wav` | Completar juego | Tres tonos ascendentes |
| `start.wav` | Iniciar partida | Tono ascendente suave |
| `game_over.wav` | Fin de juego | Tres tonos descendentes |

---

## Controles de Sonido

- **Presiona M** en cualquier momento para activar/desactivar sonidos
- El estado del sonido se muestra en el menú principal

---

## Solución de Problemas

### Los sonidos no se reproducen
1. Verifica que los archivos están en `assets/sounds/`
2. Genera los sonidos con `python generate_sounds.py`
3. Asegúrate de tener NumPy y SciPy instalados: `pip install numpy scipy`

### Error: "No module named scipy"
```bash
pip install scipy numpy
```

### Compilar ejecutable sin sonidos
El script `build.py` incluye automáticamente los sonidos en el ejecutable.

---

## Personalización de Sonidos

Puedes editar `generate_sounds.py` para cambiar:
- Frecuencias de los tonos
- Duración de los sonidos
- Envelopes (fade in/out)

Ejemplo modificar frecuencia del click:
```python
def generate_click_sound(filename, sample_rate=44100):
    click = generate_tone(1000, 0.05, sample_rate)  # Cambiar 800 a 1000
    # ...
```

Luego regenera: `python generate_sounds.py`
