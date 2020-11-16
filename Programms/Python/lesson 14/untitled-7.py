c = []
b = int(input())
for i in range(b):
    a = input()
    if 'лук' not in a:
        c.append(a)
print(', '.join(c))