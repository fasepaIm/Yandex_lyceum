a = int(input())
b = a // 100
c = a % 10
d = a // 10
e = d % 10
if b != c and c != e and b != e:
    print("ОК")
if b == c == e:
    print("В числе все цифры одинаковые")
elif b == c or b == e or e == c or c == b:
    print("В числе две одинаковые цифры")
