import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("arg", nargs='*', default=['no args'])

args = parser.parse_args()
print('\n'.join(args.arg))
