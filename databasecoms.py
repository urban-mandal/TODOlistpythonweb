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












# tasks_db_initiate()
# con = sq.connect(folder_path)
# cur = con.cursor()
# tasks_data = {
#     "tasks": ["callnyx yess sir"]
# }
# data_json = json.dumps(tasks_data)
# id_data = {
#     "id_user": 3,
#     "tasks": data_json 
# }

# cur.execute("INSERT INTO tasks (id, taskDict) VALUES (:id_user , :tasks)", id_data)
# con.commit()
# con = sq.connect(folder_path)
# cur = con.cursor()
# res = cur.execute("SELECT taskDict FROM tasks WHERE id=3")
# # print(res.fetchall(), len(res.fetchall()))
# for i in res.fetchall():
#     de_task_json = json.loads(i[0])
#     print(de_task_json['tasks'])




