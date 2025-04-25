import pygame
import random

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
grey = (100, 100, 100)
red = (255, 0, 0)

# Kecepatan gerakan
speed = 50


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color

    def constrain_to_bounds(self, min_x, max_x, min_y, max_y):
        self.rect.x = max(min_x, min(self.rect.x, max_x))
        self.rect.y = max(min_y, min(self.rect.y, max_y))


class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.size = random.randint(2, 5)
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.lifetime = random.randint(15, 30)
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]

        pygame.draw.circle(self.image, color, (5, 5), 5)

    def update(self):
        self.lifetime -= 1
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.lifetime <= 0:
            self.kill()


# Game loop
clock = pygame.time.Clock()
running = True

# Membuat tombol
buttonAtas = Box(50 * 2, 50 * 8, 50, 50, green)
buttonKiri = Box(50, 50 * 9, 50, 50, green)
buttonKanan = Box(50 * 3, 50 * 9, 50, 50, green)
buttonBawah = Box(50 * 2, 50 * 10, 50, 50, green)
buttonReset = Box(50 * 14, 50 * 9, 50, 50, green)

# Membuat pagar
pagarAtas = Box(0, 0, 50 * 16, 50, red)
pagarBawah = Box(0, 50 * 7, 50 * 16, 50, red)
pagarKiri = Box(0, 50, 50, 50 * 6, red)
pagarKanan = Box(50 * 15, 50, 50, 50 * 6, red)

spriteGroup = pygame.sprite.Group()
spriteGroup.add(pagarAtas, pagarBawah, pagarKiri, pagarKanan)
spriteGroup.add(buttonAtas, buttonKiri, buttonKanan, buttonBawah, buttonReset)

# wall level1
wall1_1 = Box(50, 50, 50 * 2, 50 * 7, red)
wall1_2 = Box(50 * 7, 50, 50 * 8, 50 * 7, red)

groupWall1 = pygame.sprite.Group()
groupWall1.add(wall1_1, wall1_2)

# wall level2
wall2_1 = Box(50 * 3, 50, 50, 50 * 5, red)
wall2_2 = Box(50 * 7, 50 * 3, 50 * 8, 50, red)
wall2_3 = Box(50 * 7, 50 * 4, 50 * 6, 50, red)
wall2_4 = Box(50 * 11, 50 * 6, 50, 50, red)

groupWall2 = pygame.sprite.Group()
groupWall2.add(wall2_1, wall2_2, wall2_3, wall2_4)

# wall level3
wall3_1 = Box(50 * 11, 50, 50 * 2, 50 * 3, red)
wall3_2 = Box(50 * 12, 50 * 6, 50 * 3, 50, red)
wall3_3 = Box(50 * 2, 50 * 2, 50 * 7, 50, red)
wall3_4 = Box(50 * 1, 50 * 3, 50 * 9, 50 * 3, red)

groupWall3 = pygame.sprite.Group()
groupWall3.add(wall3_1, wall3_2, wall3_3, wall3_4)

groups = [groupWall1, groupWall2, groupWall3]

# Map buttons to movement directions
button_actions = {
    buttonAtas: (0, -speed),
    buttonKiri: (-speed, 0),
    buttonKanan: (speed, 0),
    buttonBawah: (0, speed),
    buttonReset: (0, 0)
}

particleGroup = pygame.sprite.Group()


level = 0
while running:
    groupMain = pygame.sprite.Group()
    if level == 0:
        player = Box(50 * 4, 50 * 2, 50, 50, blue)
        box = Box(50 * 5, 50 * 2, 50, 50, yellow)
        win = Box(50 * 5, 50 * 6, 50, 50, grey)
    elif level == 1:
        player = Box(50, 50, 50, 50, blue)
        box = Box(50 * 13, 50 * 2, 50, 50, yellow)
        win = Box(50 * 14, 50 * 6, 50, 50, grey)
    else:
        player = Box(50, 50 * 2, 50, 50, blue)
        box = Box(50 * 13, 50 * 2, 50, 50, yellow)
        win = Box(50, 50 * 6, 50, 50, grey)
    groupMain.add(win)
    groupMain.add(player, box)
    running2 = True
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                posisi_mouse = event.pos

                # Mengangani klik pada tombol
                for button, (dx, dy) in button_actions.items():
                    if button.rect.collidepoint(posisi_mouse):
                        if dx != 0 or dy != 0:
                            for _ in range(5):
                                particle = Particle(
                                    player.rect.centerx, player.rect.centery, player.color)
                                particleGroup.add(particle)

                        player.rect.x += dx
                        player.rect.y += dy

                        # Batasi gerakan player agar tidak keluar dari batas layar
                        player.constrain_to_bounds(
                            50,
                            screen_width - 50 * 2,
                            50,
                            screen_height - 50 * 6
                        )

                        # Cek tabrakan dengan dinding
                        for wall in groups[level]:
                            if player.rect.colliderect(wall):
                                player.rect.x -= dx
                                player.rect.y -= dy

                        # Cek tabrakan player dengan box untuk mendorong box
                        if player.rect.topleft == box.rect.topleft:
                            if dx != 0 or dy != 0:
                                for _ in range(5):
                                    particle = Particle(
                                        box.rect.centerx, box.rect.centery, box.color)
                                    particleGroup.add(particle)

                            prev_x = box.rect.x
                            prev_y = box.rect.y

                            box.rect.x += dx
                            box.rect.y += dy

                            # Batasi gerakan box agar tidak keluar dari batas layar
                            box.constrain_to_bounds(
                                50,
                                screen_width - 50 * 2,
                                50,
                                screen_height - 50 * 6
                            )

                            # Cek tabrakan dengan dinding
                            for wall in groups[level]:
                                if box.rect.colliderect(wall):
                                    box.rect.x -= dx
                                    box.rect.y -= dy

                            # Cek tabrakan box dengan player saat box bertabrakan dengan dinding
                            if prev_x == box.rect.x and prev_y == box.rect.y:
                                player.rect.x -= dx
                                player.rect.y -= dy

                        # Cek apakah tombol reset ditekan
                        if dx == dy:
                            running2 = False

            if event.type == pygame.QUIT:
                running = False
                running2 = False

        # Update particles
        particleGroup.update()

        # Memperbarui layar
        screen.fill(white)
        spriteGroup.draw(screen)
        groupMain.draw(screen)
        groups[level].draw(screen)
        particleGroup.draw(screen)  # Draw particles
        pygame.display.flip()
        clock.tick(60)

        # Kondisi menang
        if box.rect.topleft == win.rect.topleft:
            level += 1
            if level == 3:
                print("Player menang!")
                running = False
                running2 = False
            running2 = False
pygame.quit()
