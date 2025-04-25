import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 50, 50)
box = pygame.Rect(300, 100, 50, 50)
player_speed = 5

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    prev_player = player.copy()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    if player.colliderect(box):
        # Check which side the collision came from
        if prev_player.right <= box.left:
            box.x += player_speed
            player.right = box.left
        elif prev_player.left >= box.right:
            box.x -= player_speed
            player.left = box.right
        elif prev_player.bottom <= box.top:
            box.y += player_speed
            player.bottom = box.top
        elif prev_player.top >= box.bottom:
            box.y -= player_speed
            player.top = box.bottom

    # Drawing
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), box)
    pygame.display.flip()

pygame.quit()
