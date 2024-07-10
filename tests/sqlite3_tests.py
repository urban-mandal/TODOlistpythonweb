import sqlite3
con = sqlite3.connect("\\\\ad.sigov.si\\usr\\M-P\\MandalU10\\Documents\\data bases\\dataincriment.db")
#name, deadline,importance  - are columns
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
con.commit()
# name = ("Urban",)
# cur.execute("INSERT INTO person (name) VALUES (?)", name)
# con.commit()
res = cur.execute("SELECT * FROM person")
print(res.fetchall())