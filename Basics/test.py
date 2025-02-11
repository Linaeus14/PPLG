import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_ESCAPE, K_DOWN, K_UP


def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main_menu():
    selected_option = 0
    options = ["Start Game", "Quit"]

    while True:
        screen.fill((0,0,0))
        draw_text(screen, "Main Menu", font, (255,255,255), 350, 200)

        for i, option in enumerate(options):
            color = (255,255,255) if i == selected_option else (100,100,100)
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
                    print(selected_option)
                if event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Basics/assets/bgm.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

sfx_move = pygame.mixer.Sound("Basics/assets/move.wav")
sfx_move.set_volume(1)
sfx_move.play()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Kotak")

surf = pygame.Surface((50, 50))
surf.fill((0, 0, 0))

rect = surf.get_rect(bottomright=(400, 300))

font = pygame.font.Font(None, 36)

gameLoop = main_menu()

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    screen.fill((255, 255, 255))
    screen.blit(surf, rect.bottomright)
    screen.blit(surf, rect.topleft)
    screen.blit(surf, rect.topright)
    screen.blit(surf, rect.bottomleft)

    pygame.display.flip()
pygame.quit()
