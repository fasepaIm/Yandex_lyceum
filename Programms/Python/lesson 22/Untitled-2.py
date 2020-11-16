def count_food(days):
    global daily_food
    if len(days) > 1:
        xxx = 0
        a = days[0]
        b = days[-1]
        for i in range(a - 1, b):
            xxx += int(daily_food[i])

        return xxx
    else:
        return daily_food[int(days[0]) - 1]