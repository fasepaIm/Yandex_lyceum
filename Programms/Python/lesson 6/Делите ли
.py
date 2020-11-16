n = int(input())
x = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        x += 1
if x == 2:
    print(end="\n" "ПРОСТОЕ")
else:
    print(end="\n" "НЕТ")