import re
import os
from functools import reduce

total = 0
price = open('prices.txt')
products = price.readlines()
if os.path.getsize('prices.txt') > 0:
    for i in range(len(products)):
        products[i] = re.sub(r'\s+', ' ', products[i])
    for i in products:
        total += reduce(lambda x, y: x * y, [float(j) for j in i.split() if not j.isalpha()])
price.close()
kop = [i for i in str(round(total, 2)).split('.')][-1].ljust(2, '0')
print(f'{str(int(total))}.{kop}')
