import pygame
import consts

VEL = 5
BORDER = pygame.Rect(consts.WIDTH // 2 - 5, 0, 10, consts.HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


def soldier_handle_movement(keys_pressed, soldier):
    if keys_pressed[pygame.K_LEFT] and soldier.x - VEL > BORDER.x + BORDER.width:  # LEFT
        soldier.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and soldier.x + VEL + soldier.width < consts.WIDTH:  # RIGHT
        soldier.x += VEL
    if keys_pressed[pygame.K_UP] and soldier.y - VEL > 0:  # UP
        soldier.y -= VEL
    if keys_pressed[pygame.K_DOWN] and soldier.y + VEL + soldier.height < consts.HEIGHT - 15:  # DOWN
        soldier.y += VEL


keys_pressed = pygame.key.get_pressed()
soldier = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
soldier_handle_movement(keys_pressed, soldier)
