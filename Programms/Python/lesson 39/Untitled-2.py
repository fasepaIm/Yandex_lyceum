class Profile():
    def __init__(self, name):
        self.name = name

    def info(self):
        return ''

    def describe(self):
        print('{}\n{}'.format(self.name, self.info))


class Vacancy(Profile):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'


class Resume(Profile):
    def __init__(self, name, time):
        super().__init__(name)        
        self.time = time

    def info(self):
        return f'Стаж работы: {self.time}'