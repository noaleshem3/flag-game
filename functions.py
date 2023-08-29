import consts
import random
import bombs
HEIGHT_GRASS = 1
WIDTH_GRASS = 2


def trans_index_to_cordinata(list_of_index):
    list_of_cord = []
    for set_of_index in list_of_index:
        cordinata_x = set_of_index[1] * (consts.WIDTH + consts.MARGIN)
        cordinata_y = set_of_index[0] * (consts.WIDTH + consts.MARGIN)
        set_of_cord = (cordinata_x, cordinata_y)
        list_of_cord.append(set_of_cord)

    return list_of_cord



def creating_matrix():
    matrix = []
    for hours in range(25):
        new = []
        for days in range(50):
            new.append("empty")
        matrix.append(new)
    # add_grass(matrix)
    return matrix


def add_flag(matrix):
    for i in range(22, 25):
        for j in range(46, 50):
            matrix[i][j] = 'flag'
    return matrix


def add_grass(matrix):
    num_grass = 0
    list_of_grass = []
    while num_grass < 20:
        rand_row = random.randint(1, consts.ROW_NUM - 1)
        rand_col = random.randint(1, consts.COL_NUM - 1)
        if matrix[rand_row][rand_col] == 'empty' and matrix[rand_row][rand_col + 1] == 'empty':
            index = [rand_row, rand_col]
            list_of_grass.append(tuple(index))
            matrix[rand_row][rand_col] = 'grass'
            matrix[rand_row][rand_col + 1] = 'grass'
            num_grass += 1
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    trans_index_to_cordinata(list_of_grass)
    return matrix, list_of_grass

