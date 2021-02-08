import sys
import argparse


def count_lines(path):
    try:
        with open(path, 'r', encoding='utf8') as file:
            lines = file.readlines()
    except Exception:
        lines = []
    return len(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default='')
    args = parser.parse_args()

    print(count_lines(args.file))
