for i in range(int(input())):
    a = input()
    if 'кот' in a:
        print(i + 1, a.find('кот') + 1)