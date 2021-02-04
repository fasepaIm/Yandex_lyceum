import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    query = """DELETE FROM films 
                WHERE genre IN(
                SELECT id FROM genres
                WHERE title == 'комедия')"""
    connection.cursor().execute(query).fetchall()
    connection.commit()
