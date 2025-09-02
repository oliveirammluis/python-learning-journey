# game.py

import pygame
from grid import GRID_SIZE, CELL_SIZE, grid

pygame.init()

# window dimensions
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PaintMap")

# function to draw the grid
def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = (0, 0, 255) if grid[y][x] == 1 else (255, 255, 255)  # blue if painted, white if not
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # black border

# main loop
running = True
while running:
    screen.fill((255, 255, 255))  # fill background with white
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
