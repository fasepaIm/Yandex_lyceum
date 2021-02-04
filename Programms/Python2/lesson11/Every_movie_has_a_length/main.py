import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    query = """UPDATE films
        SET duration = '42'
        WHERE duration = ''"""
    connection.cursor().execute(query)
    connection.commit()
