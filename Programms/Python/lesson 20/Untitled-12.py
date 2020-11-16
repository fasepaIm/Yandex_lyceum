def prime(number):
    d = 0
    for i in range(1, number + 1):
        if number % i == 0:
            d += 1
        if d > 2:
            return 'Составное число'
            break
    if d == 2:
        return 'Простое число'