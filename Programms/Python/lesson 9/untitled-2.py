a = int(input())
all_products = set()
resipes_products = set()
for i in range(a):
    product = input()
    all_products.add(product)
recipes = int(input())
for i in range(recipes):
    resipes0 = input()
    products_all = int(input())
    for i in range(products_all):
        name = input()
        resipes_products.add(name)
    if resipes_products <= all_products:
        print(resipes0)
    resipes_products.clear()