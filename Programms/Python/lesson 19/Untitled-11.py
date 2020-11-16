def bracket_check(test_string):
    bracket = [i for i in list(test_string) if i == '(' or i == ')']
    if len(bracket) % 2 != 0:
        print('NO')
        return None
    elif len(bracket) == 0:
        print('YES')
        return None
    else:
        while len(bracket) != 0:
            f = 1
            if bracket[0] != '(':
                print('NO')
                return None
            else:
                for i in range(len(bracket)):
                    if bracket[i] == ')':
                        f = 0
                        del bracket[0]
                        del bracket[i - 1]
                        break
            if f != 0:
                print('NO')
                return None
    print('YES')