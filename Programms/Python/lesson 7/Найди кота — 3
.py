y = 0
k = -1
a = input()
s = 1
while a != "СТОП":
    if k == -1 and ("Кот" in a or "кот" in a):
        k = s
    if "Кот" in a or "кот" in a:
        y += 1
    a = input()
    s += 1
print(y, k)