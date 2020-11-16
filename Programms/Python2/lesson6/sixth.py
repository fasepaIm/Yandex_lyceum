class ErrorFormat(Exception):
    pass


class WrongNumberOfNumbers(Exception):
    pass


class UnknowMobileOperator(Exception):
    pass


def true_number(number):
    try:
        true_symbols = ['+', '-', '(', ')']
        codes = [i for i in range(910, 940)] + [i for i in range(980, 990)] +\
            [i for i in range(902, 907)] + [i for i in range(960, 970)]

        number = ''.join([str(i) for i in list(number) if i.isdigit() or i in true_symbols])

        if number.find('+7') != 0 and number.find('8') != 0:
            raise ErrorFormat('неверный формат')

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
        number = ''.join(str(i) for i in list(number) if i.isdigit())
        if number[0] == '8':
            number = '+7' + number[1:]
        else:
            number = '+' + number
        if len(number) == 12:
            code = int(number[2:5])
            if code in codes:
                return number
            else:
                raise UnknowMobileOperator('не опеределяется оператор мобильной связи')
        else:
            raise WrongNumberOfNumbers('неверное колчиство цифр')

    except ErrorFormat:
        return 'неверный формат'

    except WrongNumberOfNumbers:
        return 'неверное количество цифр'

    except UnknowMobileOperator:
        return 'не определяется оператор сотовой связи'


print(true_number(input()))