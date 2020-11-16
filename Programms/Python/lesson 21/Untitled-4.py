shop = []
summ = 0
alll = 0
check = 0


def add_item(itemName, itemCost):
    global shop, summ, alll
    buy = itemName + ' - ' + str(itemCost)
    shop.append(buy)
    summ += itemCost
    alll += 1


def print_receipt():
    global shop, summ, alll, check
    if alll != 0:
        check += 1
        print(f'Чек {check}. Всего предметов: {alll}')
        for i in shop:
            print(i)
        print(f'Итого: {summ}')
        print('-----')
        shop = []
        summ = 0
        alll = 0