import pygame
import consts
import os

import keyboard_arrows

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


def soldier_in_beginning():
    soldier_image = pygame.image.load(os.path.join('bin', 'soldier.png'))
    soldier = pygame.transform.scale(soldier_image, (83, 41))
    screen.blit(soldier, (20, 20))
    


def move_soldier(coordinates):
    while True:
        screen.fill(consts.GREEN)
        soldier_image = pygame.image.load(os.path.join('bin', 'soldier.png'))
        soldier = pygame.transform.scale(soldier_image, (83, 41))
        screen.blit(soldier)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x += 20
                if event.key == pygame.K_LEFT:
                    x -= 20
                if event.key == K_UP:
                    y = y - 5
                if event.key == K_DOWN:
                    y = y + 5
                pygame.display.update()
    # soldier_image = pygame.image.load(os.path.join('bin', 'soldier.png'))
    # soldier = pygame.transform.scale(soldier_image, (83, 41))
    # coordinates = keyboard_arrows.moves(coordinates)
    # screen.blit(soldier, coordinates)
