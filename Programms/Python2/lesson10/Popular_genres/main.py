import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = """SELECT title FROM genres
                 WHERE id IN(
                 SELECT genre FROM Films
                 WHERE year IN (2010, 2011))"""
    result = connection.cursor().execute(query).fetchall()
    data = []
    for i in result:
        if i[0] not in data:
            print(i[0])
            data.append(i[0])


films(input())
