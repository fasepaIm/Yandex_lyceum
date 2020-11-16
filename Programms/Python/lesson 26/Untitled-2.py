children = [[input().split()[-1] == '5' for i in range(int(input()))] for j in range(int(input()))]
tr = [any(map(lambda i: int(i) == 5, i)) for i in children]
if all(tr):
    print('ДА')
else:
    print('НЕТ')