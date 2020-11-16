def transpose(matrix):
    matrix1 = []
    for i in range(len(matrix[0])):
        lol = []
        for j in range(len(matrix)):
            lol += [matrix[j][i]]
        matrix1.append(lol)
    del matrix[:]
    matrix += matrix1