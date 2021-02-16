import argparse


def file_reader(args):
    with open(args.file_name, 'r', encoding='utf8') as file:
        lines = [i.split('\n')[0] for i in file.readlines()]
        start_of_line = ''
        if args.sort:
            lines.sort()
        for i in range(len(lines)):
            if args.num:
                start_of_line = f'{i} '
            print(f'{start_of_line}{lines[i]}')
        if args.count:
            print(f'rows count: {len(lines)}')


parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str)
parser.add_argument("--count", action='store_true')
parser.add_argument("--sort", action='store_true')
parser.add_argument("--num", action='store_true')

args = parser.parse_args()

try:
    file_reader(args)
except Exception:
    print('ERROR')
