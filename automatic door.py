import pygame
import numpy as np

pygame.init()

# Screen
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smart Door Game UI")

clock = pygame.time.Clock()

# Colors
WHITE = (245, 245, 245)
GRAY = (200, 200, 200)
BLUE = (50, 150, 255)
GREEN = (0, 200, 100)
RED = (200, 50, 50)
BLACK = (30, 30, 30)

# Player
person_x = 50
person_y = 260
speed = 2

# Door
door_x = 600
door_open = False

# RL Policy
policy = {
    "NoPerson": 1,
    "Approaching": 2,
    "AtDoor": 0,
    "Leaving": 2
}

def get_state():
    if person_x < 300:
        return "NoPerson"
    elif person_x < 500:
        return "Approaching"
    elif person_x < 650:
        return "AtDoor"
    else:
        return "Leaving"

# Draw grid background
def draw_floor():
    tile_size = 40
    for x in range(0, width, tile_size):
        for y in range(200, height, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(screen, (230,230,230), rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Draw player (better style)
def draw_player():
    pygame.draw.circle(screen, BLUE, (person_x, person_y), 18)
    pygame.draw.circle(screen, WHITE, (person_x, person_y), 10)

# Draw door with animation feel
def draw_door():
    if door_open:
        pygame.draw.rect(screen, GREEN, (door_x, 200, 20, 120))
        pygame.draw.rect(screen, GREEN, (door_x+30, 200, 20, 120))
    else:
        pygame.draw.rect(screen, RED, (door_x, 200, 50, 120))

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move person
    person_x += speed
    if person_x > width:
        person_x = 0

    # RL decision
    state = get_state()
    action = policy[state]

    if action == 0:
        door_open = True
    elif action == 1:
        door_open = False

    # Draw environment
    draw_floor()
    draw_player()
    draw_door()

    # UI Panel
    pygame.draw.rect(screen, BLACK, (0, 0, width, 80))

    font = pygame.font.SysFont("Arial", 24, bold=True)
    text = font.render(f"State: {state} | Action: {['Open','Close','Wait'][action]}", True, WHITE)
    screen.blit(text, (20, 25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
