import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = """SELECT title FROM Films
                   WHERE title like '%?'"""
    res = connection.cursor().execute(query).fetchall()
    for i in res:
        print(i[0])


films(input())
