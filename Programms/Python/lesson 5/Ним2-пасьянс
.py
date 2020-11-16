a = int(input())
b = int(input())
while a > 0 or b > 0:
    number = int(input())
    if a > 0:
        if number == 1:
            c = int(input())  
            a -= c
            print(a, b)
    if b > 0:
        if number == 2:
            d = int(input())
            b -= d
            print(a, b)