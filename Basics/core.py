import pygame

# Inisialisasi Pygame/awali
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600

# Membuat layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Contoh Pygame")

# Warna
white = (255, 255, 255)
blue = (0, 0, 255)

# Membuat permukaan (surface)
surface = pygame.Surface((50, 50))
surface.fill(blue)

# Membuat persegi panjang (rectangle)
rect = surface.get_rect()
rect.topleft = (375, 275)

# Game loop
running = True
while running:
    # Mengambil semua event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mengisi layar dengan warna putih
    screen.fill(white)

    # Menggambar permukaan ke layar
    screen.blit(surface, rect)

    # Memperbarui layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
