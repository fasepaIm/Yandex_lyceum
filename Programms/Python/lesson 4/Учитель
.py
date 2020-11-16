money = int(input())
while money >= 8:
    a = money % 8
    b = money // 8
    c = b * 7
    money = money - a - c
print(money)