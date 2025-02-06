import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Kotak")

surf = pygame.Surface((50, 50))
surf.fill((0, 0, 0))

rect = surf.get_rect(bottomright=(400,300))

gameLoop = True

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