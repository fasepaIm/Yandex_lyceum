import sqlite3


def check(genre):
    con = sqlite3.connect("music_db.sqlite")
    cur = con.cursor()
    result = sorted(cur.execute(f"""SELECT Name FROM Artist
                WHERE ArtistId IN (SELECT ArtistId FROM Album
                WHERE AlbumId IN (SELECT AlbumId FROM Track
                WHERE GenreID IN (SELECT GenreID FROM Genre
                WHERE Name = '{genre}')))""").fetchall())
    for i in result:
        print(i[0])

        
check(input())
