stop = -1
a = input()
i = 0
while a != "СТОП":
    i += 1
    if ("Кот" in a or "кот" in a) and stop == -1:
        stop = i
    a = input()
print(stop)