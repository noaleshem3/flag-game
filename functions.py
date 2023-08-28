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

