start = int(input())
s = 0
a = s
for i in range(1, start + 1):
    while a > 0:
        print("Осталось секунд:", a)
        if a != 0:
            a -= 1
    if a == 0:
        print("Осталось секунд:", a)
    print("Пуск", i)
    s += 1
    a = s