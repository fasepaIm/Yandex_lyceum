def true_number(number):
    error_message = 'error'
    true_symbols = ['+', '-', '(', ')']

    number = ''.join([str(i) for i in list(number) if i.isdigit() or i in true_symbols])

    if number.find('+7') != 0 and number.find('8') != 0:
        return error_message

    if not all(number.split('-')):
        return error_message
    else:
        number = number.replace('-', '')

    open_bt = number.find('(')
    end_bt = number.find(')')

    if open_bt > -1:
        if end_bt < open_bt or not number[open_bt + 1:end_bt].isdigit()\
                or not number.count('(') == 1 or not number.count(')') == 1:
            return error_message
    else:
        if end_bt > -1:
            return error_message
    number = ''.join(str(i) for i in list(number) if i.isdigit())
    if number[0] == '8':
        number = '+7' + number[1:]
    else:
        number = '+' + number
    if len(number) == 12:
        return number
    else:
        return error_message


print(true_number(input()))
