from databasefolder import get_database_loc
import sqlite3 as sq
import json


db_path = get_database_loc()
def tasks_db_initiate():
    global db_path
    con = sq.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks(id, taskDict)")
    cur.close()
    con.close()


def load_tasks(id):
    global db_path
    con = sq.connect(db_path)
    cur = con.cursor()
    res = cur.execute(f"SELECT taskDict FROM tasks WHERE id={id}")
    tasks = json.loads(res.fetchall()[0][0])['tasks']
    print(tasks)
    return tasks

def add_a_task(id, task):
    pass