n = int(input())
v = "Евразия"
m = "Остазия"
for i in range(n):
    b = input()
    if b == "С кем война?":
        print(v)
    elif b == "С кем мир?":
        print(m)
    elif b == "Меняем":
        v, m = m, v