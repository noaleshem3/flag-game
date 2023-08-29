import consts
import random

HEIGHT_GRASS = 1
WIDTH_GRASS = 2


def trans_index_to_cordinata(list_of_index):
    list_of_cord = []
    for set_of_index in list_of_index:
        cordinata_x = set_of_index[0] * (20 + 1)
        cordinata_y = set_of_index[1] * (20 + 1)
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
    add_grass(matrix)
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
        rand_rwo = random.randint(0, consts.ROW_NUM - 3)
        rand_col = random.randint(0, consts.COL_NUM - 2)
        if matrix[rand_rwo][rand_col] == 'empty' and matrix[rand_rwo][rand_col + 1] == 'enpty':
            matrix[rand_rwo][rand_col] = 'grass'
            index_grass = [rand_rwo, rand_col]
            list_of_grass.append(tuple(index_grass))
            num_grass += 1
    trans_index_to_cordinata(list_of_grass)
    return list_of_grass


creating_matrix()
