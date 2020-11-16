a = int(input())
k = 0
while a != 1:
    if a % 2 == 1:
        a -= 1
        k += 1
    else:
        a /= 2
        k += 1
print(k) 