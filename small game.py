import pygame
import sys

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 5, 5
CELL = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Game")

# Colors
WHITE = (240, 240, 240)
BLUE = (0, 150, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Player start
player = [0, 0]

# Goal
goal = [4, 4]

# Obstacles (like water blocks)
obstacles = [[1,1], [1,3], [2,3], [3,0]]

# Draw grid
def draw():
    screen.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c*CELL, r*CELL, CELL, CELL)
            pygame.draw.rect(screen, BLACK, rect, 1)

            # Obstacles
            if [r,c] in obstacles:
                pygame.draw.rect(screen, BLUE, rect)

            # Goal
            if [r,c] == goal:
                pygame.draw.rect(screen, GREEN, rect)

            # Player
            if [r,c] == player:
                pygame.draw.circle(screen, RED,
                                   (c*CELL + CELL//2, r*CELL + CELL//2),
                                   CELL//3)

    pygame.display.update()

# Game loop
while True:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            new_pos = player.copy()

            if event.key == pygame.K_UP:
                new_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                new_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                new_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                new_pos[1] += 1

            # Boundary check
            if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS:
                # Avoid obstacles
                if new_pos not in obstacles:
                    player = new_pos

    # Win condition
    if player == goal:
        print("You reached the goal 🎉")
        pygame.quit()
        sys.exit()
