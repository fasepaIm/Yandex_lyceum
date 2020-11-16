monitor = -1
fact = 1
a = 1
while monitor == -1:
    number = int(input())
    znak = input()
    if znak == "x":
        print(number)
        break
    elif number < 0 and znak == "!":
        continue
    elif number >= 0 and znak == "!":
        for i in range(1, number + 1):
            a *= i
        print(a)
        a = 1
        continue
    number2 = int(input())
    if number2 == 0 and (znak == "/" or znak == "%"):
        continue    
    elif znak == "+":
        print(number + number2)
        continue
    elif znak == "-":
        print(number - number2)
        continue
    elif znak == "*":
        print(number * number2)
        continue
    elif znak == "/":
        print(number // number2)
        continue
    elif znak == "%":
        print(number % number2)
        continue