import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests


def info_about_drugstore(json_response):
    # Получаем первые 10 найденных организаций.
    organizations = json_response["features"][:10]
    list_with_information = []
    for i in range(len(organizations)):
        # Название организации.
        org_name = organizations[i]["properties"]["CompanyMetaData"]["name"]
        # Адрес организации.
        org_address = organizations[i]["properties"]["CompanyMetaData"]["address"]
        # Другая информация про организацию.
        #organization = json_response["features"][1]
        # Часы работы организации.
        #org_hours = [organizations[i]"properties"]["CompanyMetaData"]["Hours"]["text"]

        # Получаем координаты ответа.
        point = organizations[i]["geometry"]["coordinates"]
        org_point = "{0},{1}".format(point[0], point[1])
        list_with_information.append("{0},pm2rdl".format(org_point))
    return list_with_information
