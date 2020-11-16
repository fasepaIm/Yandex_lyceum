import random
import os

with open('lines.txt', encoding='utf-8') as opened_file:
    if os.path.getsize('lines.txt') > 0:
        print(random.choice(opened_file.readlines()))
