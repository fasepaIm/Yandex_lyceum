def month_name(num, lang):
    months = {
        '1': ['январь', 'january'],
        '2': ['февраль', 'february'],
        '3': ['март', 'march'],
        '4': ['апрель', 'april'],
        '5': ['май', 'may'],
        '6': ['июнь', 'june'],
        '7': ['июль', 'july'],
        '8': ['август', 'august'],
        '9': ['сентябрь', 'september'],
        '10': ['октябрь', 'october'],
        '11': ['ноябрь', 'november'],
        '12': ['декабрь', 'december']
    }
    if lang == 'en':
        return months[str(num)][1]
    if lang == 'ru':
        return months[str(num)][0]