## main file for running the game and visualization
import time

import pygame
import sys
from chat import next_move
from game_prompts import INIT_STATE

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define constants
BLOCK_SIZE = 65
WIDTH = 11
HEIGHT = 9
SCREEN_SIZE = (WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE)
clock = pygame.time.Clock()

# Load and resize images
def load_and_resize_image(image_path):
    image = pygame.image.load(image_path).convert_alpha()
    return pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

def string_to_game_state(game_string):
    game_state = [[char for char in row if char not in ['{','}',"'", "\\", "n"]] for row in game_string.strip().split('\n') if row]
    return game_state

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Flappy Bird")

# Load images
background_image = load_and_resize_image(r"assets/sky.png")
pipe_image = load_and_resize_image(r"assets/pipe.png")
bird_image = load_and_resize_image(r"assets/bird.png")

# Map characters to images
char_to_image = {
    '0': background_image,
    '|': pipe_image,
    '>': bird_image
}

current_state = INIT_STATE

# Main loop
command = None
running = True
steps = 0

while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            command = "UP"
        elif event.key == pygame.K_RIGHT:
            command = "NEXT"
    else:
        pass

    steps += 1

    if current_state == 'DEAD' : break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Parse game string state
    current_state = current_state.replace("\\n", "\n")
    parsed_state = string_to_game_state(current_state)
    # Draw game state
    for y, row in enumerate(parsed_state):
        for x, char in enumerate(row):
            if char in ['{','}',"'", "\\", "n"]: continue
            image = char_to_image[char]
            screen.blit(image, (x * BLOCK_SIZE, y * BLOCK_SIZE))

    pygame.display.flip()

    if command:
        ## our logic for running the game
        current_state = next_move(current_state, user_command=command)

    # Reset command
    command = None

    # Control frame rate
    clock.tick(30)

pygame.quit()
sys.exit()