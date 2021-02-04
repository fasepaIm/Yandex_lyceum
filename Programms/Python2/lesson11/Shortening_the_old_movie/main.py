import sqlite3


def get_result(name):
    connection = sqlite3.connect(name)
    data = {}
    query = """UPDATE films
                SET duration = duration / 3
                WHERE year = 1973"""
    connection.cursor().execute(query)
    connection.commit()
