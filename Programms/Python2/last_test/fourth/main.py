import sqlite3

filename, habitat = input(), input()
con = sqlite3.connect(filename)
cur = con.cursor()
color_ids = cur.execute(f"""select color_id from ages 
                            where habitat == '{habitat}' order by age""").fetchall()
colors = []
for id in color_ids:
    colors.append(cur.execute(f"""select name from colors where id == '{id[0]}'""").fetchall()[0][0])
for i in colors:
    print(i)
