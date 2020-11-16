name = ''
jump = 0


def polite_input(question):
    global name, jump
    jump += 1
    if jump == 1:
        print('Как вас зовут?')
        name = input()   
    return input(f'{name}, {question} \n')