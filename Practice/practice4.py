import pygame

# Inisialisasi Pygame
pygame.init()

# Dimensi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Belajar Pygame: Persegi Panjang")

# Warna
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
colors = [red, blue]  # Daftar warna untuk persegi panjang

# Persegi panjang
rect_width = 100
rect_height = 50
rect_x = (screen_width - rect_width) // 2  # Posisi tengah layar
rect_y = (screen_height - rect_height) // 2
rect_color = red  # Warna awal

# Frame rate
clock = pygame.time.Clock()
fps = 60

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Deteksi klik mouse
            mouse_pos = event.pos
            # Cek apakah mouse mengenai persegi panjang
            if rect_x <= mouse_pos[0] <= rect_x + rect_width and rect_y <= mouse_pos[1] <= rect_y + rect_height:
                # Ubah warna persegi panjang
                rect_color = colors[(colors.index(rect_color) + 1) % len(colors)]

    # Menggambar di layar
    screen.fill(black)  # Membersihkan layar
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))  # Menggambar persegi panjang
    pygame.display.flip()  # Memperbarui layar

    # Membatasi frame rate
    clock.tick(fps)

pygame.quit()