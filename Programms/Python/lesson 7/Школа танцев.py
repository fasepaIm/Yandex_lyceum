a = "раз"
b = "два"
c = "три"
d = "четыре"
n = int(input())
p = 0
while n > 0:
    a1 = input()
    if a1 == "раз":
        p += 1
    elif a1 != "раз":
        p = str(p)
        print("Правильных отсчётов было " + p + ", но теперь вы ошиблись.")
        p = 0
        n -= 1
        if n == 0:
            print("На сегодня хватит.")
            break
        continue
    b1 = input()
    if b1 == "два":
        p += 1
    elif b1 != "два":
        p = str(p)
        print("Правильных отсчётов было " + p + ", но теперь вы ошиблись.")
        p = 0
        n -= 1
        if n == 0:
            print("На сегодня хватит.")
            break
        continue
    c1 = input()
    if c1 == "три":
        p += 1
    elif c1 != "три":
        p = str(p)
        print("Правильных отсчётов было " + p + ", но теперь вы ошиблись.")
        p = 0
        n -= 1
        if n == 0:
            print("На сегодня хватит.")
            break
        continue
    d1 = input()
    if d1 == "четыре":
        p += 1
    elif d1 != "четыре":
        p = str(p)
        print("Правильных отсчётов было " + p + ", но теперь вы ошиблись.")
        p = 0
        n -= 1
        if n == 0:
            print("На сегодня хватит.")
            break
        continue