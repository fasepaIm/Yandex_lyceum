import json


def get_data(response):
    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]

    corners = toponym["boundedBy"]["Envelope"]
    delta1 = str((float(corners["upperCorner"].split()[0]) - float(corners["lowerCorner"].split()[0])) / 2)
    delta2 = str((float(corners["upperCorner"].split()[1]) - float(corners["lowerCorner"].split()[1])) / 2)

    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    # delta = "0.005"

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": ",".join(toponym_coodrinates.split())
    }
    return map_params
