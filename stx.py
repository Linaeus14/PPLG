import pygame
import random
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT, K_ESCAPE, K_RETURN

# Inisialisasi Pygame
pygame.init()

# Menentukan dimensi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Font
font = pygame.font.Font(None, 36)

# Kecepatan gerakan
speed = 20

def draw_text(screen, text, font, color, x, y):
    """Fungsi untuk menggambar teks di layar"""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main_menu():
    """Fungsi untuk menampilkan menu utama"""
    selected_option = 0
    options = ["Start Game", "Quit"]

    while True:
        screen.fill(black)
        draw_text(screen, "Main Menu", font, white, 350, 200)
        for i, option in enumerate(options):
            color = white if i == selected_option else (100, 100, 100)
            draw_text(screen, option, font, color, 350, 250 + i * 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:  # Start Game
                        return True
                    elif selected_option == 1:  # Quit
                        pygame.quit()
                        return False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return False
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)

def pause_menu():
    """Fungsi untuk menampilkan menu pause"""
    selected_option = 0
    options = ["Resume", "Main Menu", "Quit"]

    while True:
        overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Transparan hitam
        screen.blit(overlay, (0, 0))

        draw_text(screen, "Pause Menu", font, white, 350, 200)
        for i, option in enumerate(options):
            color = white if i == selected_option else (100, 100, 100)
            draw_text(screen, option, font, color, 350, 250 + i * 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:  # Resume
                        return True
                    elif selected_option == 1:  # Main Menu
                        return main_menu()
                    elif selected_option == 2:  # Quit
                        pygame.quit()
                        return False
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)

def game_over_menu(score):
    """Fungsi untuk menampilkan game over"""
    while True:
        screen.fill(black)
        draw_text(screen, f"Game Over! Score: {score}", font, white, 300, 250)
        draw_text(screen, "Press ENTER to return to Main Menu", font, white, 200, 300)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return main_menu()

def create_food(snake):
    """Fungsi untuk membuat makanan di posisi acak"""
    while True:
        x = random.randint(0, (screen_width // speed) - 1) * speed
        y = random.randint(0, (screen_height // speed) - 1) * speed
        food_rect = pygame.Rect(x, y, speed, speed)
        if food_rect not in snake:
            return food_rect

def handle_events(direction):
    """Fungsi untuk menangani event"""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return None
        if event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                # Cegah ular bergerak mundur
                if (event.key == K_UP and direction != K_DOWN) or \
                   (event.key == K_DOWN and direction != K_UP) or \
                   (event.key == K_LEFT and direction != K_RIGHT) or \
                   (event.key == K_RIGHT and direction != K_LEFT):
                    direction = event.key
            if event.key == K_ESCAPE:
                if not pause_menu():
                    return None
    return direction

def move_snake(direction, snake):
    """Fungsi untuk menggerakkan ular"""
    head = snake[0].copy()
    if direction == K_UP:
        head.y -= speed
    elif direction == K_DOWN:
        head.y += speed
    elif direction == K_LEFT:
        head.x -= speed
    elif direction == K_RIGHT:
        head.x += speed
    return head

def check_collisions(head, snake, food, score):
    """Fungsi untuk memeriksa tabrakan"""
    if head.x < 0 or head.x >= screen_width or head.y < 0 or head.y >= screen_height:
        return game_over_menu(score)
    if head in snake:
        return game_over_menu(score)
    if head.colliderect(food):
        return False
    return None

def main_game():
    """Fungsi utama untuk menjalankan game"""
    snake = [pygame.Rect(400, 300, speed, speed)]
    direction = pygame.K_RIGHT
    food = create_food(snake)
    score = 0

    while True:
        screen.fill(black)

        for segment in snake:
            pygame.draw.rect(screen, green, segment)

        pygame.draw.rect(screen, red, food)
        draw_text(screen, f"Score: {score}", font, white, 10, 10)
        pygame.display.flip()

        direction = handle_events(direction)
        if direction is None:
            return
        head = move_snake(direction, snake)

        collision = check_collisions(head, snake, food, score)
        if collision is True:
            return
        elif collision is False:
            score += 1
            food = create_food(snake)
            if score % 3 == 0:
                snake.append(snake[-1].copy())
        else:
            snake.pop()

        snake.insert(0, head)
        pygame.time.delay(100)

if main_menu():
    while True:
        main_game()
