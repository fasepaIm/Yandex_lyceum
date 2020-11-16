import sys
import pymorphy2


morph = pymorphy2.MorphAnalyzer()
data = list(map(str.strip, sys.stdin))
n = morph.parse('живой')[0]
for i in data:
    word = morph.parse(i)[0]
    if 'NOUN' in word.tag:
        if 'anim' in word.tag:
            it = n.inflect({word.tag.gender, word.tag.number}).word
            print(it.capitalize())
        else:
            it = n.inflect({word.tag.gender, word.tag.number}).word
            print(f'Не {it}')
    else:
        print('Не существительное')