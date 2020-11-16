a = int(input())
b = a // 100
c = a % 10
d = a // 10
e = d % 10
if b < e:
    b, e = e, b
if e < c:
    e, c = c, e
if b < e:
    b, e = e, b
m = b / 2
n = c / 2
v = m + n
if v == e:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")