import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Kotak Sederhana")

# Kecepatan frame
FPS = 60
clock = pygame.time.Clock()

# Posisi awal kotak
box_x = SCREEN_WIDTH // 2
box_y = SCREEN_HEIGHT // 2
box_size = 50
box_speed = 5

# Loop utama game
running = True
while running:
    # Mengatur kecepatan frame
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mendapatkan input dari keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        box_y -= box_speed
    if keys[pygame.K_DOWN]:
        box_y += box_speed
    if keys[pygame.K_LEFT]:
        box_x -= box_speed
    if keys[pygame.K_RIGHT]:
        box_x += box_speed

    # Membersihkan layar
    screen.fill(WHITE)

    # Menggambar kotak
    pygame.draw.rect(screen, BLUE, (box_x, box_y, box_size, box_size))

    # Update layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
sys.exit()
