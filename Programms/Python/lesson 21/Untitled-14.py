def roman():
    global one, two, three
    three = one + two
    all_num = [one, two, three]
    numbers = {
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX',
        '10': 'X',
        '20': 'XX',
        '30': 'XXX',
        '40': 'XL',
        '50': 'L',
        '60': 'LX',
        '70': 'LXX',
        '80': 'LXXX',
        '90': 'XC',
        '100': 'C',
        '200': 'CC',
        '300': 'CCC',
        '400': 'CD',
        '500': 'D',
        '600': 'DC',
        '700': 'DCC',
        '800': 'DCCC',
        '900': 'CM',
        '1000': 'M',
        '2000': 'MM',
        '3000': 'MMM'
    }
    for i in range(len(all_num)):
        if len(str(all_num[i])) == 1:
            all_num[i] = numbers[str(all_num[i])]
        elif len(str(all_num[i])) == 2:
            if str(all_num[i])[-1] == '0':
                all_num[i] = numbers[str(all_num[i])]
            else:
                all_num[i] = numbers[str(all_num[i])[0] + '0'] + numbers[str(all_num[i])[-1]]
        elif len(str(all_num[i])) == 3:
            if str(all_num[i])[-1] == '0' and str(all_num[i])[-2] == '0':
                all_num[i] = numbers[str(all_num[i])]
            elif str(all_num[i])[-1] == '0' and str(all_num[i])[-2] != '0':
                all_num[i] = numbers[str(all_num[i])[0] + '00'] + numbers[str(all_num[i])[-2] + '0']
            elif str(all_num[i])[-1] != '0' and str(all_num[i])[-2] == '0':
                all_num[i] = numbers[str(all_num[i])[0] + '00'] + numbers[str(all_num[i])[-1]]
            else:
                all_num[i] = (numbers[str(all_num[i])[0] + '00'] + numbers[str(all_num[i])[-2] + '0']
                              + numbers[str(all_num[i])[-1]])
        elif len(str(all_num[i])) == 4:
            if str(all_num[i])[-1] == '0' and str(all_num[i])[-2] == '0' and str(all_num[i])[-3] == '0':
                all_num[i] = numbers[str(all_num[i])]
            elif str(all_num[i])[-1] == '0' and str(all_num[i])[-2] == '0' and str(all_num[i])[-3] != '0':
                all_num[i] = numbers[str(all_num[i])[0] + '000'] + numbers[str(all_num[i])[1] + '00']
            elif str(all_num[i])[-1] == '0' and str(all_num[i])[-2] != '0' and str(all_num[i])[-3] != '0':
                all_num[i] = (numbers[str(all_num[i])[0] + '000'] + numbers[str(all_num[i])[1] + '00']
                              + numbers[str(all_num[i])[2] + '0'])
            elif str(all_num[i])[-1] != '0' and str(all_num[i])[-2] != '0' and str(all_num[i])[-3] != '0':
                all_num[i] = (numbers[str(all_num[i])[0] + '000'] + numbers[str(all_num[i])[1] + '00']
                              + numbers[str(all_num[i])[2] + '0'] + numbers[str(all_num[i])[3]])
            elif str(all_num[i])[-1] == '0' and str(all_num[i])[-2] == '0' and str(all_num[i])[-3] != '0':
                all_num[i] = numbers[str(all_num[i])[0] + '000'] + numbers[str(all_num[i])[-1]]
            elif str(all_num[i])[-1] != '0' and str(all_num[i])[-2] != '0' and str(all_num[i])[-3] == '0':
                all_num[i] = (numbers[str(all_num[i])[0] + '000'] + numbers[str(all_num[i])[2] + '0']
                              + numbers[str(all_num[i])[3]])
            elif str(all_num[i])[-1] == '0' and str(all_num[i])[-2] != '0' and str(all_num[i])[-3] == '0':
                all_num[i] = numbers[str(all_num[i])[0] + '000'] + numbers[str(all_num[i])[-2] + '0']
            elif str(all_num[i])[-1] != '0' and str(all_num[i])[-2] == '0' and str(all_num[i])[-3] != '0':
                all_num[i] = (numbers[str(all_num[i])[0] + '000']
                              + numbers[str(all_num[i])[-3] + '00'] + numbers[str(all_num[i])[-1]])
    print(f'{all_num[0]} + {all_num[1]} = {all_num[2]}')