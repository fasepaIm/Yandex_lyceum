import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    data = {}
    query = """DELETE from films
                WHERE genre IN(
                SELECT id FROM genres
                WHERE title == 'фантастика') and year < 2000 and duration > 90"""
    connection.cursor().execute(query)
    connection.commit()
