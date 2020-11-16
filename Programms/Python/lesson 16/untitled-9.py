a = int(input())
massiv = [[1], [1, 1]]
for i in range(2, a):
    b = []
    b.append(1)
    for j in range(i - 1):
        b.append(massiv[i - 1][j] + massiv[i - 1][j + 1])
    b.append(1)
    massiv.append(b)
for i in range(a):
    for j in massiv[i]:
        print(j, end=' ')
    print()