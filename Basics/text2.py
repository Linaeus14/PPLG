import pygame
from pygame.locals import KEYDOWN

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Poem Pygame")

font1 = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 24)

title = ["Title 1", "Title 2", "Title 3"]
poem = [
    """
    This is the first line
    of the first poem.
    It has multiple lines
    to demonstrate the
    functionality of
    displaying text
    line by line.
    """,
    """
    Here is another poem
    with different lines.
    Each line is separated
    by a newline character.
    This helps in displaying
    the text properly.
    """,
    """
    The final poem is here
    with its own lines.
    This is to show how
    we can navigate through
    different pages of text
    using Pygame.
    """
]

# Split the poem into lines
poem_lines = [poem[i].strip().split('\n') for i in range(len(title))]

page = 1
while True:
    screen.fill((255, 255, 255))

    text = font1.render(title[page-1], True, (0, 0, 0))
    screen.blit(text, (200, 100))
    for i, line in enumerate(poem_lines[page-1]):
        text = font2.render(line.strip(), True, (0, 0, 0))
        screen.blit(text, (200, 150 + i * 30))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT and page < len(title):
                page += 1
            if event.key == pygame.K_LEFT and page > 1:
                page -= 1