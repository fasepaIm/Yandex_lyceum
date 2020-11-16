price1 = 0
price2 = 0
price3 = 0
total = 0
total_head = 0
m = -1
b = int(input())
c = int(input())
for n in range(1, c + 1):
    price1 = n * 20
    if price1 <= b:
        for j in range(c, m, -1):
            price2 = j * 10
            if price2 <= b:
                for i in range(c, m, -1):
                    price3 = i * 5
                    total = price1 + price2 + price3
                    total_head = i + j + n
                    if total == b and total_head == c:
                        print(n, j, i)
                    price3 = 0
                    total = 0
                    total_head = 0                        