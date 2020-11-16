all_dishess = set()
days_dishes = set()
all_dishes = int(input())
for i in range(all_dishes):
    all_dishess.add(input())
days = int(input())
for j in range(days):
    dishes_days = int(input())
    for n in range(dishes_days):
        days_dishes.add(input())
for i in (all_dishess - days_dishes):
    print(i)