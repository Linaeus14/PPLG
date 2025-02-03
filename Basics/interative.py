# sourcery skip: min-max-identity
import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Contoh Pygame")

# Warna
white = (255, 255, 255)
blue = (0, 0, 255)

# Membuat objek persegi
square_size = 50
square_x = screen_width // 2 - square_size // 2
square_y = screen_height // 2 - square_size // 2

# Kecepatan gerakan
speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mendapatkan input dari keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    # Deteksi tabrakan dengan batas layar
    if square_x < 0:
        square_x = 0
    if square_x + square_size > screen_width:
        square_x = screen_width - square_size
    if square_y < 0:
        square_y = 0
    if square_y + square_size > screen_height:
        square_y = screen_height - square_size

    # Menggambar objek
    screen.fill(white)
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))

    # Memperbarui layar
    pygame.display.flip()
    clock.tick(60)
