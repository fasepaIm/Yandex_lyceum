import sys
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word = morph.parse(input())[0]
if 'INFN' in word.tag or 'VERB' in word.tag:
    print('Прошедшее время:')
    print(word.inflect({'masc', 'past'}).word)
    print(word.inflect({'femn', 'past'}).word)
    print(word.inflect({'neut', 'past'}).word)
    print(word.inflect({'plur', 'past'}).word)

    print('Настоящее время:')
    print(word.inflect({'pres', 'sing', '1per'}).word)
    print(word.inflect({'pres', 'plur', '1per'}).word)
    print(word.inflect({'pres', 'sing', '2per'}).word)
    print(word.inflect({'pres', 'plur', '2per'}).word)
    print(word.inflect({'pres', 'sing', '3per'}).word)
    print(word.inflect({'pres', 'plur', '3per'}).word)
else:
    print('Не глагол')