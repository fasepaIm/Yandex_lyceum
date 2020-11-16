print("Введите кол-во камней в кучке:")
kamni = int(input())
while kamni > 0:
    if kamni % 4 == 0:
        kamni -= 1
        print("ИИ взял 1 камень.")
        print("Осталось", kamni, "камней.")
    else:
        a = kamni % 4
        kamni -= kamni % 4
        print("ИИ взял", a, "камней.")
        print("Осталось", kamni, "камней.")
    if kamni == 0:
        print("ИИ выиграл.")
    if kamni > 0:
        print("Ваш ход.(Имейте ввиду, что нельзя брать больше 3 камушков.)")
        v = int(input())
    if kamni > 0:
        while v > kamni or 3 < v:
            if v > kamni or 3 < v:
                print("Осталось", kamni, "камней.")
                v = int(input())
        print("Вы взяли", v, "камней.")
        kamni -= v
        print("Осталось", kamni, "камней.")
        if kamni == 0:
            print("Пользователь выиграл.")