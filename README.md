# AimShuffle

### Descripción

**AimShuffle** es un juego de entretenimiento y entrenamiento de velocidad basado en el concepto de "Shuffle Table". El objetivo es hacer clic en los números del 1 al 25 en orden secuencial en una tabla de 5x5 lo más rápido posible.

### Características
-  Tabla de 25 números aleatorios (5x5)
-  Sistema de conteo de tiempo en tiempo real
-  Interfaz gráfica moderna con Pygame
-  Menú principal, pantalla de juego y pantalla de resultados
-  🔊 Efectos de sonido personalizados
-  Compilable a ejecutable con PyInstaller

---

### Requisitos

- **Python 3.7+**
- **pip** (gestor de paquetes)

---

### Instalación

### 1. Clonar o descargar el proyecto
```bash
git clone https://github.com/tu-usuario/AimShuffle.git
cd AimShuffle
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Generar archivos de sonido (Opcional pero recomendado)
```bash
python generate_sounds.py
```

Esto crea automáticamente los efectos de sonido en `assets/sounds/`

---


### Ejecutar directamente con Python
```bash
python src/main.py
```

### Controles
|         Acción         |  Tecla/Entrada  |
|  ---------------------|---------------  |
| Iniciar juego          |    **SPACE**    |
| Click en número        | **Mouse Click** |
| Jugar de nuevo         |   **SPACE**     |
| Volver al menú (juego) |    **ESC**      |
| Volver al menú (fin)   |    **ESC**      |
| Sonido ON/OFF          |     **M**       |

### Objetivo del Juego
1. Presiona **SPACE** en el menú para iniciar
2. Haz clic en los números **del 1 al 25 en orden**
3. Los números están desordenados en la tabla
4. Completa la tabla lo más rápido posible
5. Tu tiempo se mostrará al finalizar

---

### Crear Ejecutable

### Opción 1: Usar el script de build (Recomendado)
```bash
python build.py
```

### Opción 2: Comando PyInstaller directo
```bash
pyinstaller --onefile --windowed --name=AimShuffle src/main.py
```

El ejecutable se creará en la carpeta `dist/`

**Nota:** Para incluir un ícono, coloca un archivo `icon.ico` en `assets/images/` antes de compilar.

---

### Estructura del Proyecto

```
AimShuffle/
├── src/
│   ├── main.py              # Código principal del juego
│   └── audio.py             # Gestor de sonidos
├── assets/
│   ├── images/              # Imágenes e ícono
│   ├── sounds/              # Archivos de sonido (generados)
│   └── fonts/               # Fuentes (futuro)
├── README.md                # Este archivo
├── requirements.txt         # Dependencias Python
├── build.py                 # Script para compilar ejecutable
├── generate_sounds.py       # Script para generar sonidos
└── LICENSE                  # Licencia del proyecto
```

---

## 🛠️ Dependencias

| Paquete | Versión | Propósito |
|---------|---------|----------|
| `pygame` | 2.x+ | Motor gráfico |
| `pyinstaller` | 5.x+ | Compilador a ejecutable |
| `numpy` | 1.20+ | Procesamiento de arrays |
| `scipy` | 1.7+ | Generación de sonidos WAV |

---

### Solución de Problemas

### "pygame not found"
```bash
pip install --upgrade pygame
```

### "pyinstaller: command not found"
```bash
pip install --upgrade pyinstaller
```

### Ventana de consola aparece en el ejecutable
Asegúrate de usar el flag `--windowed` al compilar:
```bash
python build.py
```

---

### Mejoras Futuras

- [ ] Sistema de puntuaciones global
- [ ] Diferentes modos de dificultad
- [ ] Estadísticas de rendimiento
- [ ] Temas visuales

---

### Licencia

Este proyecto está bajo la licencia especificada en [LICENSE](LICENSE)

---

### Autor

Creado con ❤️ para entrenar velocidad y precisión

---

### Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de hacer fork y crear pull requests.
