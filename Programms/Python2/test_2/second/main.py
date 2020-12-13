import sqlite3


con = sqlite3.connect(input())
zap1 = input()
zap2 = input()
cur = con.cursor()
result = cur.execute(f"""SELECT name FROM bays_of_island
            WHERE {zap1} and not {zap2} order by depth desc""").fetchall()
#result = sorted(result, reverse=True)
for i in result:
    print(i[0])
