for i in range(int(input()[1:])):
    a = input()
    if '#' in a:
        a = (a[:a.find('#')])
    print(a.rstrip())