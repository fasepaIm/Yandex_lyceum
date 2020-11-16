a = len(input())
b = a * 40
if b < 100:
    print(b, "коп.")
elif b > 100:
    print(b // 100, "р.", b % 100, "коп.")