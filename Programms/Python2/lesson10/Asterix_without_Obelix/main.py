import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = """SELECT title FROM Films 
                WHERE title like '%Астерикс%' AND title NOT LIKE '%Обеликс%'"""
    result = connection.cursor().execute(query).fetchall()
    for i in result:
        print(i[0])


films(input())
