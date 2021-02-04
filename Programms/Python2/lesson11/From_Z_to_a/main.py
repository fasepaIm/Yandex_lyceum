import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    query = """DELETE FROM films 
                WHERE title LIKE 'Я%а'"""
    connection.cursor().execute(query).fetchall()
    connection.commit()
