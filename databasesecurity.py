from databasefolder import get_database_loc
import sqlite3 as sq
from argon2 import PasswordHasher
# btw once you fetch from res you cant fetch again be carefull man like for a fact!!!!!!!!
ph = PasswordHasher()

db_path = get_database_loc()

def db_users_initiate():
    global db_path
    con = sq.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS loginInfo (id INTEGER PRIMARY KEY, username, password)")
    con.commit()
    cur.close()
    con.close()

def user_login(user_username, password):
    con = sq.connect(db_path)
    cur = con.cursor()
    res = cur.execute(f"SELECT password FROM loginInfo WHERE username= ? ", (user_username,))
    if res.fetchall():
        res = cur.execute(f"SELECT password FROM loginInfo WHERE username= ? ", (user_username,))
        hashed_password = res.fetchall()[0][0]
        if verify_password(hashed_password, password) == True:
            cur.close()
            con.close()
            return "logged in"
        else:     
            cur.close()
            con.close()
            return "password not correct"
    cur.close()
    con.close()
    return "username not right"

def add_user(username, password):
    con = sq.connect(db_path)
    cur = con.cursor()
    hashed_password = hash_password(password)
    cur.execute("INSERT INTO loginInfo (username, password) VALUES (?, ?) ", (username, hashed_password))
    con.commit()
    res = cur.execute("SELECT * FROM loginInfo")
    print(res.fetchall())
    cur.close()
    con.close()
 
def hash_password(password):
    global ph
    hashed_password = ph.hash(password)
    return hashed_password

def verify_password(hashed_password, password):
    global ph
    try:
        ph.verify(hashed_password, password)
        ph.check_needs_rehash(hashed_password)
        return True
    except:
        return False

