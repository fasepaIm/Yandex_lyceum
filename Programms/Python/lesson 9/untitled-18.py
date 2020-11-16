number = set()
number2 = set()
number3 = set()
a = input()
number.add(a)
while a != '':
    if a == "":
        break
    number.add(a)
    a = input()
b = input()
number2.add(b)
while b != '':
    if b == "":
        break    
    number2.add(b)
    b = input()

number3 = number & number2
if len(number3) > 0:
    for i in number3:
        print(i)
else:
    print('EMPTY')