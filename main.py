import pygame
from os.path import join
import random


# general setup
pygame.init()
WIDTH = 1280
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invader')
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')

# importing an image
# img_path = join('images', 'player.png')
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
x = 100
# player_surf = player_surf.convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_pos = []

# random position for stars
for i in range(50):
    star_pos.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# print(star_pos)
while running:
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill('grey12')
    # stars
    for pos in star_pos:
        screen.blit(star_surf, pos)
    # player
    x += 0.1
    screen.blit(player_surf, (x, 150))
    
    
    # update the display
    pygame.display.update()

pygame.quit()