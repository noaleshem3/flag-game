import random
import functions
import consts


def rand_bombs():
    matrix = functions.creating_matrix()
    matrix = functions.add_flag(matrix)
    list_bombs_index = []
    num_bombs = 0
    while num_bombs < consts.NUM_BOMBS:
        rand_rwo = random.randint(0, consts.ROW_NUM - 1)
        rand_col = random.randint(0, consts.COL_NUM - 3)
        count = 0
        for i in range(consts.LEN_BOMB):
            if matrix[rand_rwo][rand_col + i] == 'empty':
                count += 1
        if count == consts.LEN_BOMB:
            for j in range(consts.LEN_BOMB):
                matrix[rand_rwo][rand_col + j] = 'bomb'
                add_bomb_index = [rand_rwo, rand_col + j]
                list_bombs_index.append(add_bomb_index)
            num_bombs += 1

    list_bombs_index = tuple(list_bombs_index)
    random_grass = functions.add_grass()

    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()


rand_bombs()

