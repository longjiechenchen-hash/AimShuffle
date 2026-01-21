"""
Audio manager for AimShuffle game
Handles loading and playing sound effects
"""

import pygame
import os

class SoundManager:
    """Manage all sound effects for the game"""
    
    def __init__(self, sounds_dir="assets/sounds", enabled=True):
        """
        Initialize sound manager
        
        Args:
            sounds_dir: Directory where sound files are stored
            enabled: Whether sounds are enabled
        """
        self.sounds_dir = sounds_dir
        self.enabled = enabled
        self.sounds = {}
        
        # Initialize mixer
        try:
            pygame.mixer.init()
        except Exception as e:
            print(f"Warning: Could not initialize audio: {e}")
            self.enabled = False
        
        # Load sounds
        self._load_sounds()
    
    def _load_sounds(self):
        """Load all available sounds from the sounds directory"""
        if not self.enabled:
            return
        
        sound_files = {
            'click': 'click.wav',
            'success': 'success.wav',
            'game_over': 'game_over.wav',
            'start': 'start.wav',
        }
        
        for sound_name, filename in sound_files.items():
            filepath = os.path.join(self.sounds_dir, filename)
            try:
                if os.path.exists(filepath):
                    self.sounds[sound_name] = pygame.mixer.Sound(filepath)
                    print(f"✓ Loaded sound: {sound_name}")
                else:
                    print(f"⚠ Sound not found: {filepath}")
            except Exception as e:
                print(f"✗ Error loading sound {sound_name}: {e}")
    
    def play(self, sound_name):
        """
        Play a sound effect
        
        Args:
            sound_name: Name of the sound to play
        """
        if not self.enabled or sound_name not in self.sounds:
            return
        
        try:
            self.sounds[sound_name].play()
        except Exception as e:
            print(f"Error playing sound {sound_name}: {e}")
    
    def toggle(self):
        """Toggle sounds on/off"""
        self.enabled = not self.enabled
        return self.enabled
    
    def stop_all(self):
        """Stop all playing sounds"""
        try:
            pygame.mixer.stop()
        except Exception:
            pass
