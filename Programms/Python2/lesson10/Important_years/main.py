import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = """SELECT year FROM Films
                   WHERE title like 'Х%'"""
    res = set(connection.cursor().execute(query).fetchall())
    for i in res:
        print(i[0])


films(input())
