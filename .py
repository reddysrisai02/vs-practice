import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)

# Create window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set window title
pygame.display.set_caption("Beating 3D Heart")

# Function to draw 3D heart
def draw_heart(surface, x, y, radius, depth):
    num_segments = 32
    for i in range(num_segments):
        angle = 2 * math.pi * i / num_segments
        x_outer = x + radius * math.cos(angle)
        y_outer = y + radius * math.sin(angle)
        x_inner = x + (radius - depth) * math.cos(angle)
        y_inner = y + (radius - depth) * math.sin(angle)
        pygame.draw.aaline(surface, RED, (int(x_inner), int(y_inner)), (int(x_outer), int(y_outer)))

# Function to draw twinkling spots
def draw_twinkling_spots(surface, x, y, radius):
    for _ in range(30):
        angle = random.uniform(0, math.pi * 2)
        distance = random.uniform(radius, radius * 1.2)
        spot_x = x + distance * math.cos(angle)
        spot_y = y + distance * math.sin(angle)
        pygame.draw.circle(surface, PINK, (int(round(spot_x)), int(round(spot_y))), 5)

# Main loop
clock = pygame.time.Clock()
beat_rate = 60
beat_time = 0

heart_radius = 200
radius_delta = 50  # Initial radius delta

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Calculate heart beat animation
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - beat_time
    if elapsed_time >= 60000 / beat_rate:
        beat_time = current_time
        heart_radius += radius_delta
        if heart_radius >= 250 or heart_radius <= 150:  # Limit the heart's expansion and contraction
            radius_delta = -radius_delta

    # Clear the screen
    window.fill(BLACK)

    # Draw twinkling spots around the heart
    twinkling_spots_radius = 250 + 10 * math.sin(current_time / 1000)
    draw_twinkling_spots(window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, twinkling_spots_radius)

    # Draw 3D heart with pulsating effect
    draw_heart(window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, heart_radius, 100 + 50 * math.sin(current_time / 1000))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
