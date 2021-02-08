import argparse


def copy_file(args):
    with open(args.files_name[0], "r", encoding="utf8") as reading_file:
        lines = reading_file.readlines()
        need_lines = lines[0:args.lines[0]]

    if args.upper:
        need_lines = list(map(lambda string: string.upper(), need_lines))
    
    with open(args.files_name[1], "w", encoding="utf8") as writing_file:
        for string in need_lines:
            writing_file.write(string)


parser = argparse.ArgumentParser()
parser.add_argument("--upper", action="store_true")
parser.add_argument("--lines", type=int, nargs=1, default=[-1])
parser.add_argument("files_name", type=str, nargs=2)

args = parser.parse_args()
copy_file(args)
