n = int(input())
b = "НЕТ"
for i in range(n):
    a = input()
    if "Кот" in a or "кот" in a:
        b = "МЯУ"
        break
print(b)