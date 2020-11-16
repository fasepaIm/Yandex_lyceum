a = []
b = [0, 0, 0, 0]
for i in range(int(input())):
    a.append((input().split()))
for i in a:
    if int(i[0]) == 0 or int(i[1]) == 0:
        print(f'({i[0]}, {i[1]})')
    if int(i[0]) > 0 and int(i[1]) > 0:
        b[0] += 1
    elif int(i[0]) < 0 and int(i[1]) > 0:
        b[1] += 1
    elif int(i[0]) < 0 and int(i[1]) < 0:
        b[2] += 1
    elif int(i[0]) > 0 and int(i[1]) < 0:
        b[3] += 1
print(f'I: {b[0]}, II: {b[1]}, III: {b[2]}, IV: {b[3]}.')