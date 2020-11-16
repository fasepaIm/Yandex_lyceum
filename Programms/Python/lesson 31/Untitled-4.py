import sys
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word = morph.parse(input())[0]
if 'NOUN' in word.tag:
    print('Единственное число:')
    n = word.inflect({'nomn', 'sing'}).word
    print(f'Именительный падеж: {n}')
    n = word.inflect({'gent', 'sing'}).word
    print(f'Родительный падеж: {n}')
    n = word.inflect({'datv', 'sing'}).word
    print(f'Дательный падеж: {n}')
    n = word.inflect({'accs', 'sing'}).word
    print(f'Винительный падеж: {n}')
    n = word.inflect({'ablt', 'sing'}).word
    print(f'Творительный падеж: {n}')
    n = word.inflect({'loct', 'sing'}).word
    print(f'Предложный падеж: {n}')
    print('Множественное число:')
    n = word.inflect({'nomn', 'plur'}).word
    print(f'Именительный падеж: {n}')
    n = word.inflect({'gent', 'plur'}).word
    print(f'Родительный падеж: {n}')
    n = word.inflect({'datv', 'plur'}).word
    print(f'Дательный падеж: {n}')
    n = word.inflect({'accs', 'plur'}).word
    print(f'Винительный падеж: {n}')
    n = word.inflect({'ablt', 'plur'}).word
    print(f'Творительный падеж: {n}')
    n = word.inflect({'loct', 'plur'}).word
    print(f'Предложный падеж: {n}')
else:
    print('Не существительное')