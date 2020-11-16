a = int(input())
b = 0
while a % 2 == 0:
    a //= 2
    b += 1
if a == 1:
    print(b)
else:
    print("НЕТ")