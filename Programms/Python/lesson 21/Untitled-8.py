all_name = ''
all_vacation_dates = ''


def setup_profile(name, vacation_dates):
    global all_name, all_vacation_dates
    all_name = name
    all_vacation_dates = vacation_dates


def print_application_for_leave():
    print(f'Заявление на отпуск в период {all_vacation_dates}. {all_name}')


def print_holiday_money_claim(amount):
    print(f'Прошу выплатить {amount} отпускных денег. {all_name}')


def print_attorney_letter(to_whom):
    print(f'На время отпуска в период {all_vacation_dates} моим заместителем назначается {to_whom}. {all_name}')