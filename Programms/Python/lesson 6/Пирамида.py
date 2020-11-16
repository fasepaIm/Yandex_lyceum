n = int(input())
x = n - 1
y = "*"
for i in range(n):
    print(x * " " + y)
    x -= 1
    y = y + "*" + "*"