book = {}
for i in range(int(input())):
    b = [j for j in input().split(' ', 1)]
    book[b[0]] = b[-1]
for i in range(int(input())):
    print(book.get(input(), 'Нет в словаре'))