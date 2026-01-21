"""
Sound generator script for AimShuffle
Generates basic sound effects and saves them as WAV files
"""

import numpy as np
import os
from scipy.io import wavfile

def generate_tone(frequency, duration, sample_rate=44100):
    """Generate a sine wave at a specific frequency"""
    samples = int(duration * sample_rate)
    t = np.linspace(0, duration, samples)
    wave = np.sin(2 * np.pi * frequency * t)
    return (wave * 32767).astype(np.int16)

def generate_click_sound(filename, sample_rate=44100):
    """Generate a click sound effect"""
    # Quick beep-boop
    click = generate_tone(800, 0.05, sample_rate)
    # Add envelope (fade out)
    envelope = np.linspace(1, 0, len(click))
    click = (click * envelope).astype(np.int16)
    wavfile.write(filename, sample_rate, click)
    print(f"Generated: {filename}")

def generate_success_sound(filename, sample_rate=44100):
    """Generate a success/victory sound"""
    # Two ascending beeps
    beep1 = generate_tone(523, 0.1, sample_rate)  # C5
    beep2 = generate_tone(659, 0.1, sample_rate)  # E5
    beep3 = generate_tone(784, 0.2, sample_rate)  # G5
    
    # Concatenate
    success = np.concatenate([beep1, beep2, beep3])
    
    # Add envelope
    envelope = np.concatenate([
        np.linspace(1, 0.8, len(beep1)),
        np.linspace(0.8, 0.9, len(beep2)),
        np.linspace(0.9, 0, len(beep3))
    ])
    success = (success * envelope).astype(np.int16)
    wavfile.write(filename, sample_rate, success)
    print(f"Generated: {filename}")

def generate_start_sound(filename, sample_rate=44100):
    """Generate a start/begin sound"""
    # Low tone rising up
    start = generate_tone(440, 0.15, sample_rate)  # A4
    envelope = np.linspace(0, 1, len(start))
    start = (start * envelope).astype(np.int16)
    wavfile.write(filename, sample_rate, start)
    print(f"Generated: {filename}")

def generate_game_over_sound(filename, sample_rate=44100):
    """Generate a game over sound"""
    # Descending tones
    beep1 = generate_tone(523, 0.15, sample_rate)  # C5
    beep2 = generate_tone(392, 0.15, sample_rate)  # G4
    beep3 = generate_tone(262, 0.3, sample_rate)   # C4
    
    game_over = np.concatenate([beep1, beep2, beep3])
    
    # Add envelope
    envelope = np.concatenate([
        np.linspace(1, 0.8, len(beep1)),
        np.linspace(0.8, 0.9, len(beep2)),
        np.linspace(0.9, 0, len(beep3))
    ])
    game_over = (game_over * envelope).astype(np.int16)
    wavfile.write(filename, sample_rate, game_over)
    print(f"Generated: {filename}")

if __name__ == "__main__":
    sounds_dir = os.path.join("assets", "sounds")
    
    # Create directory if it doesn't exist
    os.makedirs(sounds_dir, exist_ok=True)
    
    print("Generating sound effects...\n")
    
    # Generate all sounds
    generate_click_sound(os.path.join(sounds_dir, "click.wav"))
    generate_success_sound(os.path.join(sounds_dir, "success.wav"))
    generate_start_sound(os.path.join(sounds_dir, "start.wav"))
    generate_game_over_sound(os.path.join(sounds_dir, "game_over.wav"))
    
    print("\n✓ All sounds generated successfully!")
    print(f"Sounds saved to: {sounds_dir}")
