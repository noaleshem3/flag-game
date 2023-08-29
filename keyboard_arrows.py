import pygame


def moves(coordinates):
    pygame.init()
    x = coordinates[0]
    y = coordinates[1]
    stay = True
    while stay:
        for i in pygame.event.get():
            if i.type == pygame.QUIT or i.type == pygame.K_RETURN:
                pygame.quit()
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    x -= 21
                if i.key == pygame.K_RIGHT:
                    x += 21
                if i.key == pygame.K_UP:
                    y -= 21
                if i.key == pygame.K_DOWN:
                    y += 21
                if i.type == pygame.K_RETURN:
                    pygame.quit()
                    exit()
