n = int(input())
a = "НЕТ"
for i in range(n):
    b = input()
    if "Кот" in b or "кот" in b:
        a = "МЯУ"
print(a)