import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    data = {}
    query = """UPDATE films
                SET duration = duration * 2
                WHERE genre IN(
                SELECT id FROM genres
                WHERE title == 'фантастика')"""
    connection.cursor().execute(query)
    connection.commit()
get_result('films_db.sqlite')
