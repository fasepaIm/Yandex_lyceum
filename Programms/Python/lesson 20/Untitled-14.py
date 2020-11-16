def make_shades(alley, k):
    for i in range(len(alley)):
        if str(alley[i]).isdigit() and alley[i] != 0:
            a = alley[i]
            alley[i] = True
            if k > 0:
                for j in range(i, (i + (k * a + 1))):
                    if j <= len(alley) - 1 and alley[j] == 0:
                        alley[j] = True
            if k < 0:
                z = k * -1
                b = i - (z * a + 1) + 1
                for j in range(b, i):
                    if j > -1:
                        alley[j] = True
    for i in range(len(alley)):
        if alley[i] == 0:
            alley[i] = False
    return alley


def calculate_sunny_length(shades):
    f = 0
    for i in shades:
        if i is False:
            f += 1
    return f


def main():
    damage_trees = 0
    k = int(input())
    trees = [int(i) for i in input().split()]
    for i in range(len(trees)):
        if k > 0:
            if str(trees[i]).isdigit() and trees[i] != 96969696 and trees[i] != 0:
                a = trees[i]
                for j in range(i, (i + (k * a + 1))):
                    if j <= len(trees) - 1 and trees[j] == 0:
                        trees[j] = 96969696
        if k < 0:
            a = trees[i]
            z = k * -1
            b = i - (z * a + 1) + 1
            for j in range(b, i):
                if j > -1:
                    trees[j] = 96969696  
    for i in range(len(trees)):
        if trees[i] == 0:
            damage_trees += 1
    if damage_trees >= 10:
        print('Обгорел')
    else:
        print('Тени достаточно')