import sys
import pymorphy2

words = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
morph = pymorphy2.MorphAnalyzer()
ok = 0
str_data = sys.stdin.read().lower()
str_data = ''.join([i if i.isalpha() else ' ' for i in str_data])
str_data = str_data.split()
for i in str_data:
    if morph.parse(i)[0].normal_form in words:
        ok += 1
print(ok)