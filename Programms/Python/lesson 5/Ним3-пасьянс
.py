a = int(input())
b = int(input())
c = int(input()) 
while a > 0 or b > 0 or c > 0:
    number = int(input())
    if a > 0:
        if number == 1:
            k = int(input())  
            a -= k 
            print(a, b, c)
    if b > 0:
        if number == 2:
            d = int(input())
            b -= d
            print(a, b, c)
    if c > 0:
        if number == 3:
            t = int(input())
            c -= t
            print(a, b, c)