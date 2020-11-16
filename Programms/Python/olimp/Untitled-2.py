c = ''
d = ''
count = int(input())
number = input().split()
for i in number:
    b = 0
    a = list(input())
    for j in a:
        if a.count(j) == int(i) and j != c:
            if b == 0:
                c = j
                b += 1
            else:
                b = 2
                break
    if b == 1:
        d += c
    else:
        d = 'NO'
        break
print(d)