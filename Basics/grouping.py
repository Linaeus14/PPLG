import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Menentukan dimensi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Demonstrasi Sprite Groups")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Frame rate
clock = pygame.time.Clock()
fps = 60

# Membuat kelas Bola sebagai contoh sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()  # Memanggil konstruktor dari pygame.sprite.Sprite
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Membuat permukaan transparan
        pygame.draw.circle(self.image, color, (radius, radius), radius)  # Menggambar lingkaran di permukaan
        self.rect = self.image.get_rect(center=(x, y))  # Mendapatkan rect untuk posisi
        self.speed_x = random.choice([-3, 3])  # Kecepatan horizontal acak
        self.speed_y = random.choice([-3, 3])  # Kecepatan vertikal acak

    def update(self):
        # Memperbarui posisi bola
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Memantul jika mengenai tepi layar
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x *= -1  # Membalik arah horizontal
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1  # Membalik arah vertikal

# Membuat grup sprite
all_sprites = pygame.sprite.Group()

# Menambahkan beberapa bola ke grup sprite
for _ in range(10):  # Membuat 10 bola
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    ball = Ball(x, y, red, 20)  # Membuat bola dengan radius 20
    all_sprites.add(ball)  # Menambahkan bola ke grup sprite

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui semua sprite di grup
    all_sprites.update()

    # Menggambar semua sprite di layar
    screen.fill(black)  # Membersihkan layar
    all_sprites.draw(screen)  # Menggambar semua sprite di grup
    pygame.display.flip()  # Memperbarui layar

    # Membatasi frame rate
    clock.tick(fps)

pygame.quit()