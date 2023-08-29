import pygame


def moves(coordinates):
    pygame.init()
    x = coordinates[0]
    y = coordinates[1]
    stay = True
    while stay:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    x -= 20
                elif i.key == pygame.K_RIGHT:
                    x += 20
                elif i.key == pygame.K_UP:
                    y -= 20
                elif i.key == pygame.K_DOWN:
                    y += 20
                elif i.type == pygame.K_RETURN:
                    pygame.quit()
                    exit()

    return (x, y)