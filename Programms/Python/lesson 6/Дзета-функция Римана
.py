n = int(input())
x = 0
for i in range(n + 1):
    if i > 0:
        b = 1 / i ** 2
        x += b
p = 3.141592653589793 ** 2
z = p / x
print(z)