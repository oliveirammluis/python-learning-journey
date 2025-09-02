# game.py
import pygame
from player import Player

# --- CONFIG ---
GRID_SIZE = 5
CELL_SIZE = 100
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

# --- INIT ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PaintMap")

# --- GRID ---
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# --- PLAYER ---
player = Player()

# --- MAIN LOOP ---
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Movement
            if event.key == pygame.K_LEFT:
                player.move(-1, 0, GRID_SIZE)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0, GRID_SIZE)
            elif event.key == pygame.K_UP:
                player.move(0, -1, GRID_SIZE)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1, GRID_SIZE)
            # Toggle paint
            elif event.key == pygame.K_SPACE:
                grid[player.y][player.x] = 1 - grid[player.y][player.x]

    # --- DRAW ---
    screen.fill((255, 255, 255))
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = (0, 0, 255) if grid[y][x] == 1 else (255, 255, 255)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # border

    # Draw player
    player.draw(screen, CELL_SIZE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
