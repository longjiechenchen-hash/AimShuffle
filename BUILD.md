# AimShuffle - Build Instructions

## Prerequisites
- Python 3.7+
- pip

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

To run the game directly with Python:
```bash
python src/main.py
```

## Building as Executable

To create a standalone executable with PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=assets/images/icon.ico --name=AimShuffle src/main.py
```

Or use the provided build script:
```bash
python build.py
```

The executable will be in the `dist/` folder.

### PyInstaller Options Explained
- `--onefile`: Creates a single executable file
- `--windowed`: Removes console window (GUI only)
- `--icon`: Sets the application icon
- `--name`: Name of the executable

## Game Controls

- **SPACE**: Start game or play again
- **Mouse Click**: Click numbers 1-25 in order
- **ESC**: Return to menu from game over screen

## Troubleshooting

### pygame not found
Make sure you've installed requirements.txt properly:
```bash
pip install --upgrade -r requirements.txt
```

### PyInstaller errors
Ensure PyInstaller is properly installed:
```bash
pip install --upgrade pyinstaller
```
