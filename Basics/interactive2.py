import pygame

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
green = (10, 255, 10)

# Membuat objek persegi
square_size = 50
square_x = screen_width // 2 - square_size // 2
square_y = screen_height // 2 - square_size // 2

# Kecepatan gerakan
speed = 5


class Button():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# Game loop
clock = pygame.time.Clock()
running = True

# Membuat tombol
buttonAtas = Button(100, 400, square_size, square_size, green)
buttonKiri = Button(45, 450, square_size, square_size, green)
buttonKanan = Button(155, 450, square_size, square_size, green)
buttonBawah = Button(100, 500, square_size, square_size, green)

while running:
    screen.fill(white)

    # Deteksi tabrakan dengan batas layar
    square_x = max(square_x, 0)
    if square_x + square_size > screen_width:
        square_x = screen_width - square_size
    square_y = max(square_y, 0)
    if square_y + square_size > screen_height:
        square_y = screen_height - square_size

    # Menggambar objek
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))
    buttonAtas.draw(screen)
    buttonKiri.draw(screen)
    buttonKanan.draw(screen)
    buttonBawah.draw(screen)

    # Deteksi tekanan mouse terus-menerus
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if mouse_pressed[0]:
        if buttonAtas.rect.collidepoint(mouse_pos):
            square_y -= speed
        if buttonKiri.rect.collidepoint(mouse_pos):
            square_x -= speed
        if buttonKanan.rect.collidepoint(mouse_pos):
            square_x += speed
        if buttonBawah.rect.collidepoint(mouse_pos):
            square_y += speed

    # Memperbarui layar
    pygame.display.flip()
    clock.tick(60)

    # Menangani event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
