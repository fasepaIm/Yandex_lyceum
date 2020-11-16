a = input()
matrix = []
z = 0
while a != '':
    b = [int(i) * -1 for i in a.split()]
    matrix.append(b)
    a = input()
for i in range(int(input())):
    a = input()
    matrix_ = []
    while a != '':
        b = [int(j) for j in a.split()]
        matrix_.append(b)
        a = input()
    if matrix == matrix_:
        for j in matrix_:
            print(' '.join(str(f) for f in j))
        z = 1
        break
if z == 0:
    print('НЕТ')