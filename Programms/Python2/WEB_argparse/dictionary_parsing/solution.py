import argparse


def print_dictonary(args):
    for i in args.items:
        elem = i.split()
        print(f'Key: {elem[0]}\tValue: {elem[-1]}')


parser = argparse.ArgumentParser()
parser.add_argument("--sort", action='store_true')
parser.add_argument("items", nargs='*')

args = parser.parse_args()
print_dictonary(args)
