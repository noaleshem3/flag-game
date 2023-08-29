import functions
import bombs
import try_screen
import pygame
import consts
import keyboard_arrows
# create matrix
matrix = functions.creating_matrix()
# get index of grass location, add grass to matrix
matrix = functions.add_flag(matrix)
list_index_bombs, matrix = bombs.rand_bombs(matrix)

matrix, list_index_grass = functions.add_grass(matrix)
cord_grass = functions.trans_index_to_cordinata(list_index_grass)
cord_bombs = functions.trans_index_to_cordinata(list_index_bombs)

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
        # drew_bombs(screen)

        try_screen.add_grass(cord_grass)
        try_screen.add_flag1()
        coordinates = try_screen.soldier_in_beginning()
        bombs.night(cord_bombs, screen)
        # try_screen.move_soldier(coordinates)
        # # Draw the grid
        # for row in range(25):
        #     for column in range(50):
        #         if grid[row][column] == "x":
        #             color = consts.WHITE
        #         else:
        #             color = consts.BLACK
        #         pygame.draw.rect(screen,
        #                          color,
        #                          [(
        #                                   consts.MARGIN + consts.WIDTH) * column + consts.MARGIN,
        #                           (
        #                                   consts.MARGIN + consts.HEIGHT) * row + consts.MARGIN,
        #                           consts.WIDTH,
        #                           consts.HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.

pygame.quit()

# matrix = creating_matrix()
# matrix = add_flag(matrix)
# for row in matrix:
#     print(row)




