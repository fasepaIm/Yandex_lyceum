import sys
import pymorphy2

bottle = 99
morph = pymorphy2.MorphAnalyzer()
kvass = morph.parse('бутылка')[0]
words = kvass.make_agree_with_number(bottle).word
worl = morph.parse('осталось')[0]
while bottle > 0:
    print(f'В холодильнике {bottle} {words} кваса.')
    print('Возьмём одну и выпьем.')
    bottle -= 1
    words = kvass.make_agree_with_number(bottle).word
    if words[-1] == 'и' or words[-1] == 'к':
        worm = 'Осталось'
    else:
        worm = 'Осталась'
    print(f'{worm} {bottle} {words} кваса.')