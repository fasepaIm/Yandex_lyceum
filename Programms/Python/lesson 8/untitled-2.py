subsidy_amount = int(input())
all_animals = int(input())
while subsidy_amount > 0:
    for i in range(1, all_animals):
        subsidy_amount -= 20
        all_animals -= 1
        if subsidy_amount == 0:
            print(i, j, l)
        for j in range(1, all_animals):
            subsidy_amount -= 10
            all_animals -= 1
            if subsidy_amount == 0:
                print(i, j, l)            
            for l in range(1, all_animals):
                if all_animals > 0:
                    subsidy_amount -= 5
                    all_animals -= 1
                    if subsidy_amount == 0:
                        print(i, j, l)                