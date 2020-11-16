m = set()
n = set()
a = set()
m1 = int(input())
n1 = int(input())
for i in range(m1):
    name1 = input()
    m.add(name1)
for j in range(n1):
    name2 = input()
    n.add(name2)
a = n ^ m
if len(a) > 0:
    print(len(a))
else:
    print('NO')