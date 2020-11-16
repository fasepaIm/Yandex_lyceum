a = input()
m = 0
while m == 0:
    b = input()
    if a[-1] != b[0]:
        print(b)
        m = 1
    a = b