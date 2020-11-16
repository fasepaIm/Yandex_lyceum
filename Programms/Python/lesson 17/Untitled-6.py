b = []
count = []
f = int(input())
for i in range(f):
    a = input().split()
    b.append(a)
for i in range(f):
    z = 1
    for j in range(i + 1, f):
        if len(b[i][0]) == len(b[j][0]) and len(b[i][-1]) == len(b[j][-1]) and \
                b[i][0][0:-1] == b[j][0][0:-1] and b[i][-1][0:-1] == b[j][-1][0:-1]:
            z += 1
        count.append(z)
        count.sort(reverse=True)
print(count[0])