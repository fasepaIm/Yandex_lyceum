import numpy as np


def make_field(size):
    mat = np.fromfunction(lambda x, y: x * 0, (size, size), dtype=np.int8)
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            mat[i][j] = 1
    for i in range(1, size, 2):
        for j in range(1, size, 2):
            mat[i][j] = 1 
    return mat