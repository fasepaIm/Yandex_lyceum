a = input().split(', ')
b = input().split(', ')
z = 0
for i in a:
    c = []
    c.append(', '.join(j for j in b if len(set(i) & set(j)) == 0))
    if len(c) > 0:
        print(str(c)[2:-2])
        z = 1
    else:
        print('Нет')