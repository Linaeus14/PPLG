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
yellow = (255, 255, 0)

# Kecepatan gerakan
speed = 5

class Box():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))

# Game loop
clock = pygame.time.Clock()
running = True

# Membuat tombol
buttonAtas = Box(100, 400, 50, 50, green)
buttonKiri = Box(45, 450, 50, 50, green)
buttonKanan = Box(155, 450, 50, 50, green)
buttonBawah = Box(100, 500, 50, 50, green)

player = Box(100, 100, 50, 50, blue)
box = Box(300, 100, 50, 50, yellow)
boxOnBorder = False

while running:
    # Menangani event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Deteksi tabrakan dengan batas layar
    player.rect.x = max(player.rect.x, 0)
    if player.rect.x + 50 > screen_width:
        player.rect.x = screen_width - 50
    player.rect.y = max(player.rect.y, 0)
    if player.rect.y + 50 > screen_height:
        player.rect.y = screen_height - 50

    # Deteksi tabrakan dengan batas layar
    box.rect.x = max(box.rect.x, 0)
    if box.rect.x + 50 > screen_width:
        box.rect.x = screen_width - 50
        boxOnBorder = True
    box.rect.y = max(box.rect.y, 0)
    if box.rect.y + 50 > screen_height:
        boxOnBorder = True
        box.rect.y = screen_height - 50

    # Deteksi tekanan mouse terus-menerus
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    prev_player = player.rect.copy()
    if mouse_pressed[0]:
        if buttonAtas.rect.collidepoint(mouse_pos):
            player.rect.y -= speed
        if buttonKiri.rect.collidepoint(mouse_pos):
            player.rect.x -= speed
        if buttonKanan.rect.collidepoint(mouse_pos):
            player.rect.x += speed
        if buttonBawah.rect.collidepoint(mouse_pos):
            player.rect.y += speed

    if player.rect.colliderect(box.rect):
        if prev_player.right <= box.rect.left:
            box.rect.x += speed
            player.rect.right = box.rect.left
        elif prev_player.left >= box.rect.right:
            box.rect.x -= speed
            player.rect.left = box.rect.right
        elif prev_player.bottom <= box.rect.top:
            box.rect.y += speed
            player.rect.bottom = box.rect.top
        elif prev_player.top >= box.rect.bottom:
            box.rect.y -= speed
            player.rect.top = box.rect.bottom

    # Memperbarui layar
    screen.fill(white)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, yellow, box)
    buttonAtas.draw(screen)
    buttonKiri.draw(screen)
    buttonKanan.draw(screen)
    buttonBawah.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
