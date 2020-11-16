a = []
for i in range(int(input())):
    a.append(int(input()))
left, right = int(input()), int(input())
for i in a:
    if i >= left and i <= right:
        print(i)