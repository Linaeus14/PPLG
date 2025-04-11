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
blue = (0, 0, 255)

# Daftar warna untuk bola
colors = [white, red, blue]

# Frame rate
clock = pygame.time.Clock()
fps = 144

# Membuat kelas Bola sebagai contoh sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()  # Memanggil konstruktor dari pygame.sprite.Sprite
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Membuat permukaan transparan
        pygame.draw.circle(self.image, color, (radius, radius), radius)  # Menggambar lingkaran di permukaan
        self.rect = self.image.get_rect(center=(x, y))  # Mendapatkan rect untuk posisi
        self.speed_x = random.choice([-1, 1])  # Kecepatan horizontal acak di range [-1, 1]
        self.speed_y = random.choice([-1, 1])  # Kecepatan vertikal acak di range [-1, 1]
        self.color = color  # Menyimpan warna bola
        self.radius = radius  # Menyimpan radius bola

    def update(self):
        # Memperbarui posisi bola
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Memantul jika mengenai tepi layar
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x *= -1  # Membalik arah horizontal
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1  # Membalik arah vertikal

    def change_color(self):
        # Mengubah warna bola ke warna berikutnya dalam daftar
        current_index = colors.index(self.color)  # Mendapatkan indeks warna saat ini
        next_index = (current_index + 1) % len(colors)  # Menghitung indeks warna berikutnya
        self.color = colors[next_index]  # Mengatur warna baru
        self.image.fill((0, 0, 0, 0))  # Membersihkan permukaan
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Deteksi klik mouse
            mouse_pos = event.pos  # Mendapatkan posisi mouse
            for sprite in all_sprites:
                if sprite.rect.collidepoint(mouse_pos):  # Cek apakah mouse mengenai bola
                    sprite.change_color()  # Ubah warna bola ke warna berikutnya

    # Memperbarui semua sprite di grup
    all_sprites.update()

    # Menggambar semua sprite di layar
    screen.fill(black)  # Membersihkan layar
    all_sprites.draw(screen)  # Menggambar semua sprite di grup
    pygame.display.flip()  # Memperbarui layar

    # Membatasi frame rate
    clock.tick(fps)

pygame.quit()