from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <div align="center">
                              <h1>Анкета претендента</h1>
                              <h5>на участие в миссии</h5>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                       <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
