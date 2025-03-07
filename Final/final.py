import pygame
import sys
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
fontTitle = pygame.font.SysFont("Verdana", 36)
fontText = pygame.font.SysFont("Roboto", 34)

# Ukuran Objek
size = 30

# Frame rate / Kecepatan
fps = 8
clock = pygame.time.Clock()


class Drawable:
    def draw(self, screen):
        raise NotImplementedError("Subclasses should implement this!")


class Text(Drawable):
    def __init__(self, text, font, color, x, y):
        self.text = text
        self.font = font
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))


class Snake(Drawable):
    def __init__(self, x, y, size, color):
        self.segments = [pygame.Rect(x, y, size, size)]
        self.color = color
        self.size = size
        self.direction = K_RIGHT

    def move(self):
        head = self.segments[0].copy()
        if self.direction == K_UP:
            head.y -= self.size
        elif self.direction == K_DOWN:
            head.y += self.size
        elif self.direction == K_LEFT:
            head.x -= self.size
        elif self.direction == K_RIGHT:
            head.x += self.size
        self.segments.insert(0, head)
        self.segments.pop()

    def change_direction(self, new_direction):
        if (new_direction == K_UP and self.direction != K_DOWN) or \
           (new_direction == K_DOWN and self.direction != K_UP) or \
           (new_direction == K_LEFT and self.direction != K_RIGHT) or \
           (new_direction == K_RIGHT and self.direction != K_LEFT):
            self.direction = new_direction

    def grow(self):
        self.segments.append(self.segments[-1].copy())

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, self.color, segment)

    def check_collision(self, obj):
        return self.segments[0].colliderect(obj.rect)

    def check_self_collision(self):
        head = self.segments[0]
        return head in self.segments[1:]


class Food(Drawable):
    def __init__(self, x, y, diameter, color):
        self.rect = pygame.Rect(x, y, diameter, diameter)
        self.diameter = diameter
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           self.rect.center, self.diameter // 2)


class Fence(Drawable):
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Game:
    def __init__(self):
        self.snake = Snake(400, 300, size, green)
        self.food = self.create_food()
        self.border = [
            Fence(0, 80, screen_width, 5, white),  # Top
            Fence(0, 80, 5, screen_height, white),  # Left
            Fence(0, screen_height - 5, screen_width, 5, white),  # Bottom
            Fence(screen_width - 5, 80, 5, screen_height, white)  # Right
        ]
        self.score = 0

    def create_food(self):
        while True:
            x = random.randint(
                (0 // size) + 1, (screen_width // size) - 1) * size
            y = random.randint(
                (80 // size) + 1, ((screen_height) // size) - 1) * size
            food = Food(x, y, size, red)
            if not any(segment.colliderect(food.rect) for segment in self.snake.segments):
                return food

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    self.snake.change_direction(event.key)
                if event.key == K_ESCAPE and not pause_menu():
                    self.__init__()
                    return main_menu()
        return True

    def update(self):
        self.snake.move()
        if self.snake.check_collision(self.food):
            self.score += 1
            self.snake.grow()
            self.food = self.create_food()
        if (self.score != 1 and self.snake.check_self_collision()) or \
                any(self.snake.check_collision(fence) for fence in self.border):
            score = self.score
            self.__init__()
            return game_over_menu(score)
        return True

    def draw(self, screen):
        screen.fill(black)
        self.snake.draw(screen)
        self.food.draw(screen)
        draw_text(screen, f"Score: {self.score}", fontTitle, white, 10, 10)
        for fence in self.border:
            fence.draw(screen)
        pygame.display.flip()


def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main_menu():
    selected_option = 0
    options = ["Start Game", "Quit"]

    while True:
        screen.fill(black)
        draw_text(screen, "Snake", fontTitle, white, 100, 200)
        for i, option in enumerate(options):
            color = white if i == selected_option else (100, 100, 100)
            draw_text(screen, option, fontText, color, 100, 255 + i * 35)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:
                        return True
                    elif selected_option == 1:
                        pygame.quit()
                        sys.exit()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)


def pause_menu():
    selected_option = 0
    options = ["Resume", "Main Menu", "Quit"]

    while True:
        overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        screen.blit(overlay, (0, 0))

        draw_text(screen, "Game Paused", fontTitle, white, 300, 180)
        for i, option in enumerate(options):
            color = white if i == selected_option else (100, 100, 100)
            draw_text(screen, option, fontText, color, 300, 250 + i * 35)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:
                        return True
                    elif selected_option == 1:
                        return main_menu()
                    elif selected_option == 2:
                        pygame.quit()
                        sys.exit()
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)


def game_over_menu(score):
    selected_option = 0
    options = ["Restart", "Main Menu"]

    while True:
        screen.fill(black)
        draw_text(screen, "Game Over!", fontTitle, white, 300, 200)
        for i, option in enumerate(options):
            color = white if i == selected_option else (100, 100, 100)
            draw_text(screen, option, fontText, color, 300, 260 + i * 35)
        draw_text(screen, f"Score: {score}", fontText, white, 300, 270 + len(options) * 35)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if selected_option == 0:
                        return False
                    elif selected_option == 1:
                        score = 0
                        return main_menu()
                if event.key == K_ESCAPE:
                    return main_menu()
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)


game = Game()
if main_menu():
    while game.handle_events():
        if not game.update():
            game = Game()
        try:
            game.draw(screen)
        finally:
            clock.tick(fps)
