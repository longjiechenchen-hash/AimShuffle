"""
AimShuffle - Shuffle Table Game
Un juego de destreza donde puedes entrenar tu rapidez y precisión haciendo clicks en una tabla.
"""

import pygame
import sys
import random
import time
import os
from enum import Enum
from pathlib import Path
from audio import SoundManager

# Detectar si se ejecuta desde PyInstaller
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).parent.parent

# Constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
GRID_SIZE = 5
CELL_SIZE = 120
GRID_OFFSET_X = (WINDOW_WIDTH - GRID_SIZE * CELL_SIZE) // 2
GRID_OFFSET_Y = 150

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (240, 240, 240)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
YELLOW = (241, 196, 15)
ORANGE = (255, 165, 0)
DARK_GRAY = (50, 50, 50)

# Game States
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3

class ShuffleGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AimShuffle - Shuffle Table Game")
        
        # Load icon - handle both exe and script execution
        try:
            icon_path = BASE_DIR / "assets" / "images" / "icon.png"
            icon = pygame.image.load(str(icon_path))
            pygame.display.set_icon(icon)
        except Exception as e:
            print(f"Warning: Could not load icon: {e}")
        
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font(str(BASE_DIR / 'assets/fonts/BitcountSingle_Roman-Bold.ttf'), 60)
        self.font_large = pygame.font.Font(str(BASE_DIR / 'assets/fonts/BitcountSingle-Bold.ttf'), 40)
        self.font_medium = pygame.font.Font(str(BASE_DIR / 'assets/fonts/Ubuntu-Regular.ttf'), 32)
        self.font_small = pygame.font.Font(str(BASE_DIR / 'assets/fonts/Ubuntu-Regular.ttf'), 24)
        
        # Initialize sound manager
        self.sound_manager = SoundManager()
        
        self.state = GameState.MENU
        self.reset_game()
        
    def reset_game(self):
        """Initialize/Reset game variables"""
        self.numbers = list(range(1, 26))
        random.shuffle(self.numbers)
        self.grid = []
        self._create_grid()
        
        self.current_number = 0
        self.start_time = None
        self.elapsed_time = 0
        self.game_over = False
        
    def _create_grid(self):
        """Create grid of cell objects"""
        self.grid = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                number = self.numbers[i * GRID_SIZE + j]
                cell = {
                    'number': number,
                    'x': GRID_OFFSET_X + j * CELL_SIZE,
                    'y': GRID_OFFSET_Y + i * CELL_SIZE,
                    'width': CELL_SIZE,
                    'height': CELL_SIZE,
                    'clicked': False
                }
                row.append(cell)
            self.grid.append(row)
    
    def handle_click(self, pos):
        """Handle mouse click on grid"""
        if self.state != GameState.PLAYING:
            return
            
        x, y = pos
        for row in self.grid:
            for cell in row:
                if (cell['x'] <= x <= cell['x'] + cell['width'] and
                    cell['y'] <= y <= cell['y'] + cell['height']):
                    
                    if not cell['clicked'] and cell['number'] == self.current_number+1:
                        cell['clicked'] = True
                        self.current_number += 1
                        
                        # Play click sound
                        self.sound_manager.play('click')
                        
                        if self.current_number >= 25:
                            self.game_over = True
                            self.state = GameState.GAME_OVER
                            # Play game over sound
                            self.sound_manager.play('success')
                    break
    
    def update(self):
        """Update game state"""
        if self.state == GameState.PLAYING and self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time
    
    def draw_menu(self):
        """Draw main menu"""
        self.screen.fill(WHITE)
        
        # Title
        title = self.font_title.render("AimShuffle", True, ORANGE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.font_medium.render("Shuffle Table Game", True, ORANGE)
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 180))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Sound status
        sound_status = "ON" if self.sound_manager.enabled else "OFF"
        sound_text = self.font_small.render(f"Sound: {sound_status} (Press M to toggle)", True, BLUE)
        sound_rect = sound_text.get_rect(bottomleft=(40 , WINDOW_HEIGHT - 20))
        self.screen.blit(sound_text, sound_rect)
        
        # Instructions
        instructions = [
            "Press SPACE to Start",
            "",
            "Click the numbers from 1 to 25 as fast as you can!",
            "Test your speed and accuracy."
        ]
        
        y_offset = 200
        for instruction in instructions:
            text = self.font_small.render(instruction, True, BLUE)
            text_rect = text.get_rect(bottomright=(WINDOW_WIDTH - 70, WINDOW_HEIGHT-y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
    
    def draw_game(self):
        """Draw game screen"""
        self.screen.fill(WHITE)
        
        # Draw header
        header_text = f"Find: {self.current_number} | Time: {self.elapsed_time:.2f}s"
        header = self.font_medium.render(header_text, True, ORANGE)
        header_rect = header.get_rect(center=(WINDOW_WIDTH // 2, 50))
        self.screen.blit(header, header_rect)
        
        # Draw grid
        for row in self.grid:
            for cell in row:
                self._draw_cell(cell)
        
        # Draw exit button hint
        exit_text = self.font_small.render("Press ESC to reset", True, RED)
        exit_rect = exit_text.get_rect(topleft=(10, 10))
        self.screen.blit(exit_text, exit_rect)
    
    def _draw_cell(self, cell):
        """Draw a single cell"""
        x, y = cell['x'], cell['y']
        width, height = cell['width'], cell['height']
        
        # Cell background
        if cell['clicked']:
            color = BLUE
            text_color = WHITE
        else:
            color = BLUE
            text_color = WHITE
        
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        pygame.draw.rect(self.screen, WHITE, (x, y, width, height), 3)
        
        # Cell number
        number_text = self.font_large.render(str(cell['number']), True, text_color)
        text_rect = number_text.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(number_text, text_rect)
    
    def draw_game_over(self):
        """Draw game over screen"""
        self.screen.fill(DARK_GRAY)
        
        # Title
        title = self.font_title.render("GAME OVER!", True, GREEN)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        # Time result
        time_text = self.font_large.render(f"Time: {self.elapsed_time:.2f} seconds", True, YELLOW)
        time_rect = time_text.get_rect(center=(WINDOW_WIDTH // 2, 250))
        self.screen.blit(time_text, time_rect)
        
        # Instructions
        restart_text = self.font_medium.render("Press SPACE to play again", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, 400))
        self.screen.blit(restart_text, restart_rect)
        
        esc_text = self.font_small.render("Press ESC to go to menu", True, LIGHT_GRAY)
        esc_rect = esc_text.get_rect(center=(WINDOW_WIDTH // 2, 500))
        self.screen.blit(esc_text, esc_rect)
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.state == GameState.MENU:
                            self.state = GameState.PLAYING
                            self.reset_game()
                            self.start_time = time.time()
                            self.sound_manager.play('start')
                        elif self.state == GameState.GAME_OVER:
                            self.state = GameState.PLAYING
                            self.reset_game()
                            self.start_time = time.time()
                            self.sound_manager.play('start')
                    elif event.key == pygame.K_ESCAPE:
                        if self.state == GameState.GAME_OVER:
                            self.state = GameState.MENU
                        elif self.state == GameState.PLAYING:
                            # Exit to menu during game
                            self.state = GameState.MENU
                    elif event.key == pygame.K_m:
                        # Toggle sound
                        self.sound_manager.toggle()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.handle_click(event.pos)
            
            self.update()
            
            # Draw screen
            if self.state == GameState.MENU:
                self.draw_menu()
            elif self.state == GameState.PLAYING:
                self.draw_game()
            elif self.state == GameState.GAME_OVER:
                self.draw_game_over()
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = ShuffleGame()
    game.run()
