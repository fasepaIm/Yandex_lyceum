n = int(input())
i = 0
while n >= 1:
    if n == 1:
        break
    elif n % 2 == 0:
        n = n / 2
        i += 1
    else:
        n = 3 * n + 1
        i += 1
print(i)