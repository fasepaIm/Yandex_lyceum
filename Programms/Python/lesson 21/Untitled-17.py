MorseCode = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}


def encode_to_morse(text):
    global MorseCode
    sortir_text = text.upper().split()
    over_text = []
    for i in sortir_text:
        if i.isalpha():
            word = []
            for j in i:
                word.append(MorseCode[j])
            over_text.append(' '.join(word))
        else:
            print('Извините, но в вашем тексте присутствуют запрещённые символы.' 
                  ' Наша программа не может их обработать. Пока.')
            return 0
    print('|'.join(over_text))


def decode_from_morse(code):
    global MorseCode
    all_text = []
    CodeMorse = {}
    for i in MorseCode:
        CodeMorse[MorseCode[i]] = i
    all_cod = code.split('|')
    for i in all_cod:
        cod = i.split()
        strk = ''
        for j in cod:
            if j in CodeMorse:
                strk += CodeMorse[j]
            else:
                print('В заданном коде есть невозможные символыю Программа останавливает работу.')
                return 0
        all_text.append(strk)
    print(' '.join(all_text))


a = input('Вас приветствует программа "МОРЗЯНКА". Вы хотите "кодировать" или "декодировать" текст: ')
if a == 'кодировать':
    encode_to_morse(input('Введите текст для кодировки: '))
else:
    decode_from_morse(input('Введите код для декодирования: '))