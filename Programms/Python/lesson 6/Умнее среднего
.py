n = int(input())
d = int(input())
x = 1
if n == 1:
    print("0")
if n > 1:
    for i in range(n - 1):
        if x == 1:
            print("0")
        m = int(input())
        c = d / x
        if m > c:
            print(">")
        elif m == c:
            print("0")
        elif m < c:
            print("<")
        x += 1
        d += m