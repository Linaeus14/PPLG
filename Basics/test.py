import pygame

pygame.init()

# Menentukan dimensi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

class Objek(pygame.sprite.Sprite):
    def __init__(self, size, warna):
        super().__init__()
        self.size = size
        self.warna = warna
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA)  # Menambahkan alpha channel
        self.surface.fill((0, 0, 0, 0))  # Mengisi dengan transparansi
        self.rect = self.surface.get_rect()

class Kotak(Objek):
    def __init__(self, size, warna, x, y):
        super().__init__(size, warna)
        pygame.draw.rect(self.surface, self.warna, (0, 0, size, size))
        self.rect.topleft = (x, y)

class Lingkaran(Objek):
    def __init__(self, radius, warna, x, y):
        super().__init__(radius * 2, warna)
        pygame.draw.circle(self.surface, self.warna, (radius, radius), radius)
        self.rect.center = (x, y)

class Garis(Objek):
    def __init__(self, warna, titik1, titik2):
        super().__init__(max(titik1[0], titik2[0]), warna)
        pygame.draw.line(self.surface, self.warna, titik1, titik2)
        self.rect.topleft = (min(titik1[0], titik2[0]), min(titik1[1], titik2[1]))

# Membuat objek kotak, lingkaran, dan garis
kotak = Kotak(50, (255, 0, 0), 100, 100)
lingkaran = Lingkaran(25, (0, 0, 255), 200, 200)
garis = Garis((0, 255, 0), (0, 300), (800, 0))

gameLoop = True

while gameLoop:
    screen.fill((0, 0, 0))  # Mengisi layar dengan warna hitam
    screen.blit(kotak.surface, kotak.rect.topleft)
    screen.blit(lingkaran.surface, lingkaran.rect.topleft)
    screen.blit(garis.surface, garis.rect.topleft)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

pygame.quit()