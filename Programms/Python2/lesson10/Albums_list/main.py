import sqlite3


def check(genre):
    con = sqlite3.connect("music_db.sqlite")
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM Album
                WHERE AlbumId IN (SELECT AlbumId FROM Track
                WHERE GenreID IN (SELECT GenreID FROM Genre
                WHERE Name = '{genre}'))""").fetchall()
    result = sorted(result, key=lambda x: (int(x[-1]), x[1]))
    for i in result:
        print(i[1])

        
check(input())
