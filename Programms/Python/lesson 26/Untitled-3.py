import sys

cnt = sys.stdin.readlines()
print((sum(map(lambda x: int(x), cnt))) / len(cnt) if cnt != [] else -1)