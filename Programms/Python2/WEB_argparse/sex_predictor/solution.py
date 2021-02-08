import argparse
import sys


movies = {
    'melodrama': 0,
    'football': 100,
    'other': 50
}


parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--movie", choices=["melodrama", "football", "other"], default="other")

args = parser.parse_args()

if args.barbie < 0 or args.barbie > 100:
    args.barbie = 50
if args.cars < 0 or args.cars > 100:
    args.cars = 50

boy = int((100 - args.barbie + args.cars + movies[args.movie]) / 3)
girl = 100 - boy

print(f'boy: {boy}')
print(f'girl: {girl}')
