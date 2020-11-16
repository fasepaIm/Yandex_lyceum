a = int(input())
matrix = []
for i in range(a):
    row = []
    for j in range(a):
        row.append(int(input()))
    matrix.append(row)
for i in range(int(input())):
    y = int(input())
    x = int(input())
    if y == 0 and x == 0:
        matrix[x][y] -= 8
        matrix[x][y + 1] -= 4
        matrix[x + 1][y] -= 4
        matrix[x + 1][y + 1] -= 4
    elif y == 0 and x == a - 1:
        matrix[x][y] -= 8
        matrix[x][y + 1] -= 4
        matrix[x - 1][y] -= 4
        matrix[x - 1][y + 1] -= 4
    elif y == a - 1 and x == 0:
        matrix[x][y] -= 8
        matrix[x][y - 1] -= 4
        matrix[x + 1][y] -= 4
        matrix[x - 1][y - 1] -= 4
    elif y == a - 1 and x == a - 1:
        matrix[x][y] -= 8
        matrix[x][y - 1] -= 4
        matrix[x - 1][y] -= 4
        matrix[x - 1][y - 1] -= 4
    elif x > 0 and x < a - 1 and y == 0:
        matrix[x][y] -= 8
        matrix[x - 1][y] -= 4
        matrix[x + 1][y] -= 4
        matrix[x][y + 1] -= 4
        matrix[x - 1][y + 1] -= 4
        matrix[x + 1][y + 1] -= 4
    elif x > 0 and x < a - 1 and y == a - 1:
        matrix[x][y] -= 8
        matrix[x - 1][y] -= 4
        matrix[x + 1][y] -= 4
        matrix[x][y - 1] -= 4
        matrix[x - 1][y - 1] -= 4
        matrix[x + 1][y - 1] -= 4
    elif x == 0 and y > 0 and y < a - 1:
        matrix[x][y] -= 8
        matrix[x][y - 1] -= 4
        matrix[x][y + 1] -= 4
        matrix[x + 1][y] -= 4
        matrix[x + 1][y + 1] -= 4
        matrix[x + 1][y - 1] -= 4
    elif x == a - 1 and y > 0 and y < a - 1:
        matrix[x][y] -= 8
        matrix[x][y - 1] -= 4
        matrix[x][y + 1] -= 4
        matrix[x - 1][y] -= 4
        matrix[x - 1][y + 1] -= 4
        matrix[x - 1][y - 1] -= 4
    else:
        matrix[x][y] -= 8
        matrix[x][y + 1] -= 4
        matrix[x][y - 1] -= 4
        matrix[x + 1][y] -= 4
        matrix[x - 1][y] -= 4
        matrix[x + 1][y + 1] -= 4
        matrix[x + 1][y - 1] -= 4
        matrix[x - 1][y + 1] -= 4
        matrix[x - 1][y - 1] -= 4
for i in range(a):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            matrix[i][j] = 0
    print(*matrix[i])