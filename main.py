## main file for running the game and visualization
import time

import pygame
import sys
from chat import next_move
from prompts import INIT_STATE
import os

os.makedirs('screenshots', exist_ok=True)

DISPLAY_BLOCKS = True

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

pygame.font.init()  # Initialize font module
font_size = 30  # Choose an appropriate font size
game_font = pygame.font.Font(None, font_size)  # Use default font; you can also specify a path to a .ttf file

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
display_command = "Start State"
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
        elif event.key == pygame.K_s:  # Check if 'S' is pressed
            screenshot_path = os.path.join('screenshots', f'screenshot_{int(time.time())}.png')
            pygame.image.save(screen, screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
        display_command = command if command else "No command"

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

            if DISPLAY_BLOCKS:
                # Draw red rectangle around the block
                pygame.draw.rect(screen, (255, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 3)  # 3 is the thickness of the outline

                # Render the character in the center of the block
                text_surface = game_font.render(char, True, (255, 0, 0))  # True for antialiasing
                text_rect = text_surface.get_rect(center=((x * BLOCK_SIZE + BLOCK_SIZE // 2), (y * BLOCK_SIZE + BLOCK_SIZE // 2)))
                screen.blit(text_surface, text_rect)

    # Display the current command at the bottom of the screen
    command_surface = game_font.render(f"Command: {display_command}", True, BLACK)
    command_rect = command_surface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - font_size // 2))
    screen.blit(command_surface, command_rect)
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