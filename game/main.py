import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lily and Paws")
clock = pygame.time.Clock()

# Create player instance
player = Player("assets/images/lily.png")  # Replace with your own placeholder image path

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    screen.fill((135, 206, 250))  # Sky blue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
