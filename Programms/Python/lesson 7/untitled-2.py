blocks = int(input())
a = 0
h1 = 0
for i in range(blocks):
    block = int(input())
    h = block % 256
    r = block // 256 % 256
    m = block // 256 // 256 % 256
    test = 37 * (m + r + h1) % 256
    if (test != h or h > 100) and a == 0:
        print(i)
        a = 1
    h1 = h
if a == 0:
    print('-1')