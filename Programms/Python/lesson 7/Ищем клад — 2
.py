x = int(input())
y = int(input())
x1 = 0
y1 = 0
storona = input()
koordinat = int(input())
h = 1
h1 = 0
while storona != "стоп":
    if storona == "север":
        y1 += koordinat
    elif storona == "юг":
        y1 -= koordinat
    elif storona == "запад":
        x1 -= koordinat
    elif storona == "восток":
        x1 += koordinat
    if x1 == x and y1 == y and h1 == 0:
        h1 = h
    storona = input()
    if storona == "стоп":
        break
    koordinat = int(input())
    h += 1
print(h1)