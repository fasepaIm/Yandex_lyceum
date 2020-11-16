listki = int(input())
children = set()
children2 = set()
children3 = set()
for i in range(listki):
    stroki = int(input())
    for j in range(stroki):
        last_name = input()
        if i == 0:
            children.add(last_name)
        elif i > 0:
            children2.add(last_name)
    if i > 0:
        children3 = children & children2
        children = children3
        children2.clear()
for i in children3:
    print(i)