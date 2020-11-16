def number_in_english(number):
    cnt = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety',
        '100': 'one hundred',
        '200': 'two hundred',
        '300': 'three hundred',
        '400': 'four hundred',
        '500': 'five hundred',
        '600': 'six hundred',
        '700': 'seven hundred',
        '800': 'eight hundred',
        '900': 'nine hundred'
    }
    if len(str(number)) == 1:
        return cnt[str(number)]
    elif len(str(number)) == 2 and str(number)[0] == '1':
        return cnt[str(number)]
    elif len(str(number)) == 2 and str(number)[-1] == '0':
        return cnt[str(number)]
    elif len(str(number)) == 2 and str(number)[-1] != '0':
        a = cnt[str(number)[0] + '0'] + ' '
        b = cnt[str(number)[-1]]
        return a + b
    elif len(str(number)) == 3:
        if str(number)[-1] == '0' and str(number)[-2] == '0':
            return cnt[str(number)]
        elif str(number)[1] == '0' and str(number)[-1] != '0':
            a = cnt[str(number)[0] + '00'] + ' ' + 'and' + ' '
            b = cnt[str(number)[2:]]
            return a + b
        elif str(number)[1] == '1':
            a = cnt[str(number)[0] + '00'] + ' ' + 'and' + ' '
            b = cnt[str(number)[1:]]
            return a + b
        elif str(number)[1] != '0' and str(number)[-1] == '0':
            a = cnt[str(number)[0] + '00'] + ' ' + 'and' + ' '
            b = cnt[str(number)[1:]]
            return a + b
        else:
            a = cnt[str(number)[0] + '00'] + ' ' + 'and' + ' '
            b = cnt[str(number)[1] + '0'] + ' '
            c = cnt[str(number)[-1]]
            return a + b + c