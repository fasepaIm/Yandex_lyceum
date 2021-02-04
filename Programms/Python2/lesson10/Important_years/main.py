import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = query = """SELECT year FROM Films
                   WHERE title like 'Х%'"""
    res = connection.cursor().execute(query).fetchall()
    result = []
    for i in res:
        if i[0] not in result:
            result.append(i[0])
    for i in result:
        print(i)


films(input())
