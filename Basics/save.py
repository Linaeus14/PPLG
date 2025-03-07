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
def save_number(number):
    with open(save_file, "w") as penyimpanan:
        json.dump({"number": number}, penyimpanan)

# Fungsi untuk memuat nomor dari file
def load_number():
    if os.path.exists(save_file):
        with open(save_file, "r") as penyimpanan:
            data = json.load(penyimpanan)
            return data.get("number", 0)
    return 0

# Inisialisasi nomor
number = load_number()

# Fungsi untuk menggambar nomor di layar
def draw_number(screen, number):
    screen.fill(black)
    text_surface = font.render(str(number), True, white)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

# Draw the initial number
draw_number(screen, number)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_number(number)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and number < 10:
                number += 1
            if event.key == pygame.K_DOWN and number > 0:
                number -= 1
            draw_number(screen, number)

    clock = pygame.time.Clock()
    clock.tick(30)

pygame.quit()