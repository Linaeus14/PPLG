import pygame

pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Kotak")

surf = pygame.Surface((400, 300))
surf.fill((0, 0, 0))

rect = surf.get_rect()

gameLoop = True

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
