a, b = 0, 1
n = int(input())
for i in range(n):
    c, d = int(input()), int(input())
    a = a * d + c * b
    b *= d
x, y = a, b
while y > 0:
    x, y = y, x % y
print(a // x, "/", b // x, sep='')