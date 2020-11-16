n = int(input())
if n < 0:
    print("Пуск")
else:
    for i in range(n, -1, -1):
        print("Осталось секунд:", i)
        if i == 0:
            print("Пуск")