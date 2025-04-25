import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle and Transition Demo")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR_1 = (30, 144, 255)  # Dodger Blue
COLOR_2 = (255, 69, 0)    # Red-Orange

# Particle class
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 6)
        self.color = random.choice([WHITE, COLOR_1, COLOR_2])
        self.lifetime = random.randint(40, 100)
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.lifetime -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Transition variables
transition_alpha = 0
transition_speed = 2
transition_direction = 1  # 1 for fade-in, -1 for fade-out

# Particle list
particles = []

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Particle generation at mouse position
    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for _ in range(5):  # Generate multiple particles
            particles.append(Particle(mouse_x, mouse_y))

    # Update and draw particles
    for particle in particles[:]:
        particle.update()
        particle.draw(screen)
        if particle.lifetime <= 0:
            particles.remove(particle)

    # Transition effect
    transition_alpha += transition_speed * transition_direction
    if transition_alpha >= 255 or transition_alpha <= 0:
        transition_direction *= -1  # Reverse direction
        transition_alpha = max(0, min(255, transition_alpha))

    transition_surface = pygame.Surface((WIDTH, HEIGHT))
    transition_surface.set_alpha(transition_alpha)
    transition_surface.fill(COLOR_1 if transition_direction == 1 else COLOR_2)
    screen.blit(transition_surface, (0, 0))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()