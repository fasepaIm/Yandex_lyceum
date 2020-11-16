total = 0
a = float(input())
while a > 0:
    if a > 1000:
        a = a - a * 0.05
    total = total + a
    a = float(input())
print(total)