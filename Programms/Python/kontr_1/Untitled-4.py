a = input()
matrix = []
z = 0
while a != '':
    b = [int(i) for i in a.split()]
    matrix.append(b)
    a = input()
for i in range(int(input())):
    x = 0
    z = 0
    a = input()
    matrix_ = []
    while a != '':
        b = [int(j) for j in a.split()]
        matrix_.append(b)
        a = input()
    if len(matrix_) == len(matrix):
        for j in range(len(matrix_)):
            if len(matrix_[j]) == len(matrix[j]):
                for m in range(len(matrix_[j])):
                    if matrix[j][m] + 2 == matrix_[j][m] or matrix[j][m] - 2 == matrix_[j][m]:
                        if x == 0:
                            z += 1
                    else:
                        z = 0
                        x += 1
                        break
            else:
                break
    else:
        x += 1
        continue
    if z != 0 and x == 0:
        for j in matrix_:
            print(' '.join(str(f) for f in j))
        break
if z == 0 and x != 0:
    print('Неправильные знамения')