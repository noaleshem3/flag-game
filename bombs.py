import random
import consts
import functions

def rand_bombs(matrix):
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
            add_bomb_index = [rand_rwo, rand_col]
            list_bombs_index.append(tuple(add_bomb_index))
            for j in range(consts.LEN_BOMB):
                matrix[rand_rwo][rand_col + j] = 'bomb'

            num_bombs += 1

    list_bombs_index = list_bombs_index
    matrix, index_grass = functions.add_grass(matrix)
    # print(list_bombs_index)
    # for row in matrix:
    #     for col in row:
    #         print(col, end=' ')
    #     print()
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()

    return list_bombs_index, index_grass

