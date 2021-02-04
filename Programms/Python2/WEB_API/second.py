import requests

geocoder_request_1 = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode="
geocoder_request_2 = "&format=json"
cities = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']

for city in cities:
    # Выполняем запрос.
    response = requests.get(f'{geocoder_request_1}{city}{geocoder_request_2}')
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Название округа
        toponym_name = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
        print(f'{city}: {toponym_name}')
    else:
        print("Ошибка выполнения запроса:")
        print(f'{geocoder_request_1}{city}{geocoder_request_2}')
        print("Http статус:", response.status_code, "(", response.reason, ")")
