import pygame

pygame.init()
screen = pygame.display.set_mode((500, 450))
x1, y1 = 300, 350
while True:
    # screen.fill((0, 0, 0))
    circle1 = pygame.draw.circle(screen, (249, 246, 238), (x1, y1), 35)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x1 -= 10
                print('left')
            if i.key == pygame.K_RIGHT:
                x1 += 10
                print('right')
            if i.key == pygame.K_UP:
                y1 -= 10
                print("up")
            if i.key == pygame.K_DOWN:
                y1 += 10
                print('down')
            if i.key == pygame.K_RETURN:
                pygame.quit()
                exit()
    pygame.display.update()



