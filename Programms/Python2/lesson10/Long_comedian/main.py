import sqlite3


def films(name):
    connection = sqlite3.connect(name)
    query = """SELECT title FROM Films 
                WHERE genre IN(
                SELECT id FROM genres
                WHERE title == 'комедия') and duration >= 60"""
    result = connection.cursor().execute(query).fetchall()
    for i in result:
        print(i[0])


films(input())
