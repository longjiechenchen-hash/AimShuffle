## Quick Start Guide - AimShuffle con Sonidos

### En 5 Minutos

### Paso 1: Setup Automático
```bash
python setup.py
```
✓ Instala todo y genera sonidos

### Paso 2: Jugar
```bash
python src/main.py
```
✓ ¡Listo! El juego incluye sonidos

### Paso 3: Compilar (Opcional)
```bash
python build.py
```
✓ Crea `dist/AimShuffle.exe` con sonidos incluidos

---

### Controles

```
SPACE     = Iniciar/Repetir
MOUSE     = Click en números
ESC       = Salir al menú (en cualquier momento)
M         = Sonido ON/OFF
```

---

## 🔊 Los 4 Sonidos del Juego

| # | Sonido | Momento |
|---|--------|---------|
| 1 | 🔔 click | Al hacer clic en número correcto |
| 2 | ✨ success | Al completar los 25 números |
| 3 | ▶ start | Al presionar SPACE para iniciar |
| 4 | ⏹ game_over | Al terminar la partida |

---

## 🛠️ Manual Completo de Sonidos

Ver: [SOUNDS.md](SOUNDS.md)

---

### Archivos Importantes

```
AimShuffle/
├── src/
│   ├── main.py           ← Juego principal
│   └── audio.py          ← Sistema de sonidos
├── generate_sounds.py    ← Crear sonidos
├── setup.py              ← Setup automático
├── build.py              ← Compilar ejecutable
└── assets/sounds/        ← Archivos WAV (auto-generados)
```

---

### Verificar Setup

```bash
# Verificar dependencias instaladas
python -m pip list | findstr pygame

# Verificar sonidos generados
dir assets\sounds\

# Probar código
python -m py_compile src/main.py src/audio.py
```

---

### Problemas Comunes

### "ModuleNotFoundError: No module named pygame"
```bash
pip install pygame
```

### "No se escuchan los sonidos"
```bash
python generate_sounds.py
```

### Ventana de consola en ejecutable
```bash
python build.py
```
(Usa `--windowed` automáticamente)

---

### Compartir el Juego

1. Crear ejecutable:
   ```bash
   python build.py
   ```

2. Archivo: `dist/AimShuffle.exe`
   -  Standalone (sin necesidad de Python)
   -  Incluye sonidos
   -  Lista para compartir

---
