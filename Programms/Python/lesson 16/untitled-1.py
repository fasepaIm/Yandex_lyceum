a = [int(i) for i in input().split()]
b = [i.lower() for i in input().split()]
c = ''
for i in a:
    c += b[i - 1]
    c += ' '
print(c.capitalize())