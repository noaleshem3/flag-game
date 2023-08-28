import pygame
import os
import consts

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

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (consts.WIDTH + consts.MARGIN)
            row = pos[1] // (consts.HEIGHT + consts.MARGIN)
            # Set that location to one
            grid[row][column] = "x"
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(consts.GREEN)

    # Draw the grid
    for row in range(25):
        for column in range(50):
            if grid[row][column] == "x":
                color = consts.WHITE
            else:
                color = consts.BLACK
            pygame.draw.rect(screen,
                             color,
                             [(consts.MARGIN + consts.WIDTH) * column + consts.MARGIN,
                              (consts.MARGIN + consts.HEIGHT) * row + consts.MARGIN,
                              consts.WIDTH,
                              consts.HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

flag_image = pygame.image.load(os.path.join('bin', 'flag.png'))
screen.blit(flag_image, (1042, 492))
