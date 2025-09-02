# player.py
import pygame

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy, grid_size):
        self.x = max(0, min(self.x + dx, grid_size - 1))
        self.y = max(0, min(self.y + dy, grid_size - 1))

    def draw(self, screen, cell_size):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x * cell_size, self.y * cell_size, cell_size, cell_size))
