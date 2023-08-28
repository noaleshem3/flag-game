import random

import main

LEN_BOMB = 3
ROW_NUM = 22
COL_NUM = 46
NUM_BOMBS = 20




def rand_bombs():
    matrix = main.creating_matrix()
    matrix = main.add_flag(matrix)
    num_bombs = 0
    while num_bombs < NUM_BOMBS:
        rand_rwo = random.randint(0, ROW_NUM - 1)
        rand_col = random.randint(0, COL_NUM - 3)
        count = 0
        for i in range(LEN_BOMB):
            if matrix[rand_rwo][rand_col + i] == 'empty' and matrix[rand_rwo][rand_col + i] != 'flag':
                count += 1
        if count == LEN_BOMB:
            for j in range(LEN_BOMB):
                matrix[rand_rwo][rand_col + j] = 'bomb'
            num_bombs += 1

    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()


rand_bombs()
