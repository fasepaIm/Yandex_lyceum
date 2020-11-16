class ErrorFormat(Exception):
    pass


class WrongNumberOfNumbers(Exception):
    pass


class UnknowMobileOperator(Exception):
    pass


class UnknowCountryCode(Exception):
    pass


def true_number(number):
    try:
        other_country = False
        true_symbols = ['+', '-', '(', ')']
        codes = [i for i in range(910, 940)] + [i for i in range(980, 990)] +\
            [i for i in range(902, 907)] + [i for i in range(960, 970)]

        number = ''.join([str(i) for i in list(number) if i.isdigit() or i in true_symbols])

        if not all(number.split('-')):
            raise ErrorFormat('неверный формат')
        else:
            number = number.replace('-', '')

        open_bt = number.find('(')
        end_bt = number.find(')')

        if open_bt > -1:
            if end_bt < open_bt or not number[open_bt + 1:end_bt].isdigit()\
                    or not number.count('(') == 1 or not number.count(')') == 1:
                raise ErrorFormat('неверный формат')
        else:
            if end_bt > -1:
                raise ErrorFormat('неверный формат')
        number = ''.join(number[i] for i in range(len(number))
                         if number[i].isdigit() or number[i] == '+' and i == 0)

        if number[0] == '8':
            number = '+7' + number[1:]

        if number.find('+7') != 0 and number.find('+1') != 0 and number.find('+55') != 0 and\
                number.find('+359') != 0:
            if number[0] == '+':
                raise UnknowCountryCode('не определяется код страны')
            else:
                raise ErrorFormat('неверный формат')

        if number[:2] != '+7':
            other_country = True

        if len(number) == 12:
            code = int(number[2:5])
            if not other_country:
                if code in codes:
                    return number
                else:
                    raise UnknowMobileOperator('не определяется оператор мобильной связи')
            else:
                return number
        else:
            raise WrongNumberOfNumbers('неверное колчиство цифр')

    except ErrorFormat:
        return 'неверный формат'

    except WrongNumberOfNumbers:
        return 'неверное количество цифр'

    except UnknowMobileOperator:
        return 'не определяется оператор сотовой связи'

    except UnknowCountryCode:
        return 'не определяется код страны'


print(true_number(input()))

