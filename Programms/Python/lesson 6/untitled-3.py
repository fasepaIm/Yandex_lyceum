numbers = int(input())
a = 0
b = 0
for i in range(numbers):
    c = int(input())
    if b == 0:
        a += c
        b += 1
        continue
    elif b > 0:
        a -= c
        b = 0
        continue
print(a)