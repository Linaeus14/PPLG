import pygame
import json
import os

# Inisialisasi Pygame
pygame.init()

# Menentukan dimensi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Number Display")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Font
font = pygame.font.SysFont("Verdana", 100)

# File path for saving/loading the number
save_file = "Basics/assets/save.json"

# Fungsi untuk menyimpan nomor ke file
def save_number(number, name):
    with open(save_file, "w") as penyimpanan:
        json.dump({"number": number, "name": name}, penyimpanan)

# Fungsi untuk memuat nomor dari file
def load_number():
    if os.path.exists(save_file):
        with open(save_file, "r") as penyimpanan:
            nilai = json.load(penyimpanan)
            return [nilai.get("number", 0), nilai.get("name", "Tidak Terbaca")]
    return 0


# Inisialisasi data
data = load_number()
number = data[0]
name = data[1]


def draw(screen, text, x, y):
    text_surface = font.render(str(text), True, white)
    screen.blit(text_surface, (x, y))


# Main loop
running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_number(number, "John")
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and number < 10:
                number += 1
            if event.key == pygame.K_DOWN and number > 0:
                number -= 1
    draw(screen, number, 300, 200)
    draw(screen, name, 300, 300)
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(30)

pygame.quit()
