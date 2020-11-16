lev = 0
pr = 1000
number = (pr - lev) // 2
print(number)
a = input()
while a != '=':
    if a == '<':
        lev = number
        number = lev + ((pr - lev) // 2)
        print(number)
    elif a == '>':
        pr = number
        number = pr - ((pr - lev) // 2)
        print(number)
    a = input()
    if a == '=':
        print("Число угадано.")