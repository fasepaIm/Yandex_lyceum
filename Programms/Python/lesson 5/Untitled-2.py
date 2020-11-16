first_heap = int(input("Введите кол-во камней в первой куче: "))
second_heap = int(input("Введите кол-во камней во второй куче: "))
a = 0
b = 1
if first_heap == second_heap:
    a = 1
    b = 0
    first_heap -= a
    print("ИИ взял", a, "камней. Осталось", first_heap,
          "камней в первой куче и", second_heap, "во второй куче.")
if first_heap == 0 and second_heap == 0:
    print("ИИ выиграл.")
while first_heap > 0 or second_heap > 0:
    if b == 1:
        if first_heap > second_heap:
            a = first_heap - second_heap
            first_heap -= a
            print("ИИ взял", a, "камней. Осталось", first_heap,
                  "камней в первой куче и", second_heap, "во второй куче.")
            a = 0
        if first_heap < second_heap:
            a = second_heap - first_heap
            second_heap -= a
            print("ИИ взял", a, "камней. Осталось", first_heap,
                  "камней в первой куче и", second_heap, "во второй куче.")
            a = 0
    if first_heap == 0 and second_heap == 0:
        print("ИИ выиграл.")
    if first_heap > 0 or second_heap > 0:
        print("Ваш ход.(Имейте ввиду, что можно брать любое кол-во камней.)")
        heap = int(input("Введите номер кучи из которой собираетесь брать камни: "))
        if heap == 1:
            a = int(input("Введите кол-во камней которое собираетесь брать: "))
            if a >= 0:
                while a > first_heap or a == 0:
                    print("Осталось", first_heap,
                          "камней в первой куче и", second_heap, "во второй куче.")
                    a = int(input("Введите кол-во камней которое собираетесь брать: "))
            print("Вы взяли", a, "камней.")
            first_heap -= a
            print("Осталось", first_heap, "камней в первой куче и", second_heap, "во второй куче.")
            a = 0
            b = 1
        if heap == 2:
            a = int(input("Введите кол-во камней которое собираетесь брать: "))
            if a >= 0:
                while a > second_heap or a == 0:
                    print("Осталось", first_heap,
                          "камней в первой куче и", second_heap, "во второй куче.")
                    a = int(input("Введите кол-во камней которое собираетесь брать: "))
            print("Вы взяли", a, "камней.")
            second_heap -= a
            print("Осталось", first_heap, "камней в первой куче и", second_heap, "во второй куче.")
            a = 0
            b = 1
        if first_heap == 0 and second_heap == 0:
            print("Пользователь выиграл.")