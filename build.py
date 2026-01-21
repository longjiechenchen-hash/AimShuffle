#!/usr/bin/env python
"""
Build script for AimShuffle using PyInstaller
Run: python build.py
"""

import subprocess
import sys
import os

def build():
    """Build executable using PyInstaller"""
    
    print("=" * 50)
    print("AimShuffle - Building Executable")
    print("=" * 50)
    
    # Define PyInstaller command
    icon_path = os.path.join("assets", "images", "icon.ico")
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=AimShuffle",
        "--distpath=dist",
        "--workpath=build",
        "--specpath=.",
        "src/main.py"
    ]
    
    # Add icon if it exists
    if os.path.exists(icon_path):
        cmd.insert(2, f"--icon={icon_path}")
        print(f"✓ Icon found: {icon_path}")
    else:
        print(f"⚠ Icon not found at {icon_path} (optional)")
    
    print(f"\nRunning: {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n" + "=" * 50)
        print("✓ Build completed successfully!")
        print("=" * 50)
        print(f"Executable location: dist/AimShuffle.exe")
        return 0
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 50)
        print("✗ Build failed!")
        print("=" * 50)
        return 1
    except FileNotFoundError:
        print("\n✗ PyInstaller not found!")
        print("Install it with: pip install pyinstaller")
        return 1

if __name__ == "__main__":
    sys.exit(build())
