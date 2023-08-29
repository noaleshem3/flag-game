import pygame
import consts

arrow = pygame.image.load('bin/flag.png')
sized_arrow = pygame.transform.scale(arrow, (
    consts.WIDTH, consts.HEIGHT))

# Create a box to put the arrow in, so that the rotation will be around
# it's bottom (the box's center)
arrow_box = pygame.Surface(
    (consts.WIDTH, consts.HEIGHT * 2), )
arrow_box.fill(consts.WHITE)
arrow_box.blit(sized_arrow, (0, 0))
print(arrow_box)
