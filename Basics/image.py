import pygame
import os

# Inisialisasi Pygame
pygame.init()

# Menentukan dimensi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Display")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Path to the image file
image_path = "Basics/assets/image.jpg"

# Load the image
if os.path.exists(image_path):
    image = pygame.image.load(image_path)
else:
    print(f"Image file not found: {image_path}")
    pygame.quit()
    exit()

# Scale the image to fit the screen
image = pygame.transform.scale(image, (screen_width, screen_height))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the image as the background
    screen.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()