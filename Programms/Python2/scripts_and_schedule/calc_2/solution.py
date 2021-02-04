import sys


class NoParams(Exception):
    pass


try:
    a = [i for i in sys.argv[1:]]
    if len(a) == 0:
        raise NoParams('NO PARAMS')
    a = list(map(int, a))

    coeff = 1
    args_sum = 0
    for i in a:
        args_sum += i * coeff
        coeff *= -1
    print(args_sum)
    
except NoParams as ex:
    print(ex)

except Exception as ex:
    print(ex.__class__.__name__)
