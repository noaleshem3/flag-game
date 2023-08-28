import random

LEN_BOMB = 3
ROW_NUM = 22
COL_NUM = 46
NUM_BOMBS = 20


def creating_matrix():
    matrix = []
    for hours in range(25):
        new = []
        for days in range(50):
            new.append("empty")
        matrix.append(new)
    return matrix


def rand_bombs():
    matrix = creating_matrix()
    num_bombs = 0
    while num_bombs < NUM_BOMBS:
        rand_rwo = random.randint(0, ROW_NUM - 1)
        rand_col = random.randint(0, COL_NUM - 3)
        count = 0
        for i in range(LEN_BOMB):
            if matrix[rand_rwo][rand_col + i] == 'empty':
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