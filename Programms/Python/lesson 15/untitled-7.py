a = input()
c = []
b = [str(i) for i in input().split()]
for i in b:
    if a in i or a.upper() in i:
        print(i)