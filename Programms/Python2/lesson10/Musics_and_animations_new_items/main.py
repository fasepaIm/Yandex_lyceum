import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = """SELECT title FROM Films 
                WHERE genre IN(
                SELECT id FROM genres 
                WHERE title IN ('музыка', 'анимация')) and year >= 1997"""
    res = connection.cursor().execute(query).fetchall()
    for i in res:
        print(i[0])


films(input())
