import pygame
import consts
import os
pygame.init()  # Define some colors

grid = []
for row in range(25):
    grid.append([])
    for column in range(50):
        grid[row].append(0)

grid[1][5] = 1

pygame.init()

screen = pygame.display.set_mode(consts.WINDOW_SIZE)

pygame.display.set_caption("Array Backed Grid")

done = False

clock = pygame.time.Clock()


def add_flag1():
    flag_image = pygame.image.load(os.path.join('bin', 'flag.png'))
    flag = pygame.transform.scale(flag_image, (83, 62))
    screen.blit(flag, (968, 464))


def add_grass(list_cord):

    for i in list_cord:
        grass_image = pygame.image.load(os.path.join('bin', 'grass.png'))
        grass = pygame.transform.scale(grass_image, (41, 41))
        screen.blit(grass, i)


