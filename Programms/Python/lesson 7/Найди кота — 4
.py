zveri = "НЕТ"
n = int(input())
for i in range(n):
    a = input()
    if "Кот" in a or "кот" in a:
        zveri = "МЯУ"
    elif "Пёс" in a or "пёс" in a:
        zveri = "НЕТ"
print(zveri)