import sys
import pymorphy2

words = {}
word = []
morph = pymorphy2.MorphAnalyzer()
str_data = sys.stdin.read().lower()
str_data = ''.join([i if i.isalpha() else ' ' for i in str_data])
for i in str_data.split():
    parse_my = morph.parse(i)[0]
    if parse_my.score > 0.5 and 'NOUN' in parse_my.tag:
        a = morph.parse(i)[0].normal_form
        if a in words:
            words[a] += 1
        else:
            words[a] = 1
for i in words:
    word.append([i, words[i]])
word = sorted(word, key=lambda x: (x[1], x[0]))
word.reverse()
word = word[:10]
word = [i[0] for i in word]
print(' '.join(word))