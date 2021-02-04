import sqlite3


def check(artist_name):
    con = sqlite3.connect("music_db.sqlite")
    cur = con.cursor()
    result = sorted(list(set([i[0] for i in cur.execute(f"""SELECT Name FROM Track
                WHERE AlbumId IN (SELECT AlbumId FROM Album
                WHERE ArtistID IN (SELECT ArtistID FROM Artist
                WHERE Name = '{artist_name}'))""").fetchall()])))
    for i in result:
        print(i)

check(input())
