import requests

geocoder_request = """https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%BA%D0%B0,%2038&format=json"""

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Почтовый индекс топонима:
    toponym_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    # Адрес:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_address,"\nИндекс:", toponym_code)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
