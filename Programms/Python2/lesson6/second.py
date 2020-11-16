class ErrorFormat(Exception):
    pass


def true_number(number):
    try:
        error_message = 'error'
        true_symbols = ['+', '-', '(', ')']

        number = ''.join([str(i) for i in list(number) if i.isdigit() or i in true_symbols])

        if number.find('+7') != 0 and number.find('8') != 0:
            raise ErrorFormat('error')

        if not all(number.split('-')):
            raise ErrorFormat('error')
        else:
            number = number.replace('-', '')

        open_bt = number.find('(')
        end_bt = number.find(')')

        if open_bt > -1:
            if end_bt < open_bt or not number[open_bt + 1:end_bt].isdigit()\
                    or not number.count('(') == 1 or not number.count(')') == 1:
                raise ErrorFormat('error')
        else:
            if end_bt > -1:
                raise ErrorFormat('error')
        number = ''.join(str(i) for i in list(number) if i.isdigit())
        if number[0] == '8':
            number = '+7' + number[1:]
        else:
            number = '+' + number
        if len(number) == 12:
            return number
        else:
            raise ErrorFormat('error')

    except ErrorFormat:
        return error_message


print(true_number(input()))
