#!/usr/bin/env python
"""
Simple packaging script - Creates a distributable ZIP archive
"""

import shutil
import os
from pathlib import Path

def create_release():
    """Create a distributable package"""
    
    print("=" * 50)
    print("AimShuffle - Creating Release Package")
    print("=" * 50)
    
    # Define what to include
    include_dirs = ['src', 'assets']
    include_files = ['requirements.txt', 'QUICKSTART.md', 'README.md', 'LICENSE']
    
    # Create releases directory
    releases_dir = Path('releases')
    releases_dir.mkdir(exist_ok=True)
    
    # Create ZIP archive
    package_name = 'AimShuffle-v1.0'
    try:
        base_path = releases_dir / package_name
        
        # Clean previous release
        if base_path.exists():
            shutil.rmtree(base_path)
        
        base_path.mkdir(exist_ok=True)
        
        # Copy directories
        for dir_name in include_dirs:
            src = Path(dir_name)
            dst = base_path / dir_name
            if src.exists():
                shutil.copytree(src, dst)
                print(f"✓ Copied: {dir_name}")
        
        # Copy files
        for file_name in include_files:
            src = Path(file_name)
            if src.exists():
                shutil.copy2(src, base_path / file_name)
                print(f"✓ Copied: {file_name}")
        
        # Create ZIP
        zip_path = releases_dir / f'{package_name}'
        shutil.make_archive(str(zip_path), 'zip', base_path.parent, base_path.name)
        
        print("\n" + "=" * 50)
        print("✓ Package created successfully!")
        print("=" * 50)
        print(f"Package location: releases/{package_name}.zip")
        print(f"\nTo run:")
        print("1. Extract the ZIP file")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Run: python src/main.py")
        return 0
    
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(create_release())
