d = int(input())
m = int(input())
a = int(input())
if m == 1 or m == 2:
    m += 10
    a -= 1
else:
    m -= 2
y = a % 100
c = a // 100
k = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777))
x = k % 7
print(x)