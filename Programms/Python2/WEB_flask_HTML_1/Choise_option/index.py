from flask import Flask

app = Flask(__name__)

planets = {'Меркурий':['Эта планета близка к Солнцу;', 'На ней нет жизни;',
                   'Вы вообще о чём?;', 'Она - планета;',
                   'Наконец, она просто красива! может быть'],

           'Венера':['Эта планета близка к Земле;', 'На ней много света;',
                   'На ней есть *****;', 'На ***;',
                   'Наконец, она просто красива!'],

           'Земля':['Это Земля;', 'На ней много необходимых ресурсов;',
                   'На ней есть вода и атмосфера;', 'На ней есть магнитное поле;',
                   'Наконец, она просто красива!'],

           'Марс':['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;',
                   'На ней есть вода и атмосфера;', 'На ней есть небольшое магнитное поле;',
                   'Наконец, она просто красива!'],

           'Юпитер':['Эта планета близка к Земле;', 'Ничего интересного не прочитаете',
                   'На ней что-то есть;', 'На ней есть что-то;',
                   'Она просто планета!'],

           'Сатурн':['Эта планета близка к Марсу;', 'На ней много Сатурна;',
                   'На ней есть вода и атмосфера;', 'На есть поле;',
                   'Наконец, она!'],

           'Уран':['Эта планета близка к Сатурну;', 'На ней ресурсов;',
                   'На ней есть вода и атмосфера;', 'На ней есть поле;',
                   'Наконец, она красива!'],

           'Нептун':['Эта планета близка к Урану;', 'Зачем пришёл?',
                   'На ней есть вода и атмосфера;', 'На ней есть небольшое;',
                   'Она просто!'],
}

@app.route('/')
@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <h1>Моё предложение: {planet_name}</h1>
                  </head>
                  <body>
                    <h4>{planets[planet_name][0]}</h4>
                    <div class="alert alert-success" role="alert">
                      <h4>{planets[planet_name][1]}</h4>
                    </div>
                    <div class="alert alert-dark" role="alert">
                      <h4>{planets[planet_name][2]}</h4>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h4>{planets[planet_name][3]}</h4>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h4>{planets[planet_name][4]}</h4>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

