import pygame
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_ESCAPE, QUIT, KEYDOWN

# Inisialisasi Pygame
pygame.init()

# Menentukan ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Contoh Menu Pygame")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)

# Font
font = pygame.font.Font(None, 36)

# Fungsi untuk menggambar teks di layar
def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Fungsi untuk menampilkan menu utama
def main_menu():
    selected_option = 0
    options = ["Start Game", "Quit"]

    while True:
        screen.fill(black)
        draw_text(screen, "Main Menu", font, white, 350, 200)
        for i, option in enumerate(options):
            color = white if i == selected_option else gray
            draw_text(screen, option, font, color, 350, 250 + i * 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:  # Start Game
                        return True
                    elif selected_option == 1:  # Quit
                        return False

                if event.key == K_ESCAPE:
                    return False

                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)

# Fungsi untuk menampilkan menu pause
def pause_menu():
    selected_option = 0
    options = ["Resume", "Main Menu", "Quit"]

    while True:
        # Menggambar layar transparan di atas gameplay
        overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Transparan hitam
        screen.blit(overlay, (0, 0))

        # Menggambar teks menu pause
        draw_text(screen, "Pause Menu", font, white, 350, 200)
        for i, option in enumerate(options):
            color = white if i == selected_option else gray
            draw_text(screen, option, font, color, 350, 250 + i * 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:  # Resume
                        return True
                    elif selected_option == 1:  # Main Menu
                        main_menu()
                        return True
                    elif selected_option == 2:  # Quit
                        return False

                if event.key == K_ESCAPE:
                    return True
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)

# Loop game utama (hanya untuk demonstrasi transisi menu) dan Menampilkan menu utama sebelum memulai game
running = main_menu()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
                pause_menu()

    screen.fill(black)
    draw_text(screen, "Tekan ESC untuk Pause Menu", font, white, 250, 300)
    pygame.display.flip()

pygame.quit()
