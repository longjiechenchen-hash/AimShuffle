#!/usr/bin/env python
"""
Quick setup script for AimShuffle
Installs dependencies and generates sound files
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a shell command and report progress"""
    print(f"\n{'='*50}")
    print(f"► {description}")
    print(f"{'='*50}")
    try:
        result = subprocess.run(cmd, check=True, shell=True)
        print(f"✓ {description} - Completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} - Fallido")
        return False

def main():
    print("="*50)
    print("AimShuffle - Setup Wizard")
    print("="*50)
    
    # Install dependencies
    success = run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Instalando dependencias"
    )
    
    if not success:
        print("\n✗ No se pudieron instalar las dependencias")
        return 1
    
    # Generate sounds
    success = run_command(
        f"{sys.executable} generate_sounds.py",
        "Generando archivos de sonido"
    )
    
    if not success:
        print("\n⚠ Advertencia: No se pudieron generar los sonidos")
        print("Puedes intentar generarlos manualmente después")
    
    print("\n" + "="*50)
    print("✓ Setup completado!")
    print("="*50)
    print("\nPuedes ejecutar el juego con:")
    print("  python src/main.py")
    print("\nOcompilarlo a ejecutable con:")
    print("  python build.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
