import consts
import random


def creating_matrix():
    matrix = []
    for hours in range(25):
        new = []
        for days in range(50):
            new.append("empty")
        matrix.append(new)
    return matrix


def add_flag(matrix):
    for i in range(22, 25):
        for j in range(46, 50):
            matrix[i][j] = 'flag'
    return matrix


def add_grass(matrix):
    num_grass = 0
    list_of_grass = []
    while num_grass < consts.NUM_BOMBS:
        rand_rwo = random.randint(0, consts.ROW_NUM - 1)
        rand_col = random.randint(0, consts.COL_NUM - 3)
        if matrix[rand_rwo][rand_col] == 'empty':
            matrix[rand_rwo][rand_col] = 'grass'
            index_grass = [rand_rwo, rand_col]
            list_of_grass.append(tuple(index_grass))
            num_grass += 1
    return list_of_grass
