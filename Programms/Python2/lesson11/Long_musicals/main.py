import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    data = {}
    query = """UPDATE films
                SET duration = 100
                WHERE genre IN(
                SELECT id FROM genres
                WHERE title == 'мюзикл') and duration > 100"""
    connection.cursor().execute(query)
    connection.commit()
