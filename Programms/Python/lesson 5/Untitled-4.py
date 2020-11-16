print("Введите кол-во камней в кучке:")
kamni = int(input())
while kamni > 0:
    if kamni % 4 == 2:
        a = 1
        kamni -= 1
        print("ИИ взял", a, "камней.")
        print("Осталось", kamni, "камней.")
    elif kamni % 4 == 3:
        a = 2
        kamni -= 2
        print("ИИ взял", a, "камней.")
        print("Осталось", kamni, "камней.")        
    elif kamni % 4 == 0:
        a = 3
        kamni -= 3
        print("ИИ взял", a, "камней.")
        print("Осталось", kamni, "камней.")        
    else:
        kamni -= 1
        print("ИИ взял 1 камень.")
        print("Осталось", kamni, "камней.")
    if kamni == 0:
        print("ИИ проиграл.")
    if kamni > 0:
        print("Ваш ход.(Имейте ввиду, что нельзя брать больше 3 камушков.)")
        v = int(input())
    if kamni >= 0:
        while v > kamni or 3 < v or v == 0:
            if v > kamni or 3 < v or v == 0:
                print("Осталось", kamni, "камней.")
                v = int(input("Ваш ход.(Имейте ввиду, что нельзя брать больше 3 камушков или 0.) "))
        print("Вы взяли", v, "камней.")
        kamni -= v
        print("Осталось", kamni, "камней.")
        if kamni == 0:
            print("Пользователь проиграл.")