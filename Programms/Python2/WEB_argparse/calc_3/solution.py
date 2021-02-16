import argparse


def check_num(args):
    if len(args) == 0:
        return 'NO PARAMS'
    elif len(args) == 1:
        return 'TOO FEW PARAMS'
    elif len(args) > 2:
        return 'TOO MANY PARAMS'
    else:
        return sum(args)


parser = argparse.ArgumentParser()
parser.add_argument('numbers', nargs='*')

try:
    args = parser.parse_args()
    numbers = list(map(int, args.numbers))
    print(check_num(numbers))
except Exception as error:
    print(error.__class__.__name__)
