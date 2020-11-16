import numpy as np


def snake(rows, cols):
    matrix = np.arange(1, rows * cols + 1).reshape(rows, cols)
    for i in range(1, rows, 2):
        matrix[i] = list(reversed(matrix[i]))
    return matrix