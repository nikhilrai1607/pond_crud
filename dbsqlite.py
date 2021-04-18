import sqlite3
import os

DATABASE = '/database.db'

cur_dir = os.path.abspath('.')

db = cur_dir+DATABASE

conn = sqlite3.connect(db)

"""
Schema:
id: int
file_name: string
media_type: string
created_at: time
updated_at: time

"""

conn.execute('CREATE TABLE IF NOT EXISTS item (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,file_name TEXT NOT NULL,media_type TEXT NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,updated_at timestamp  NOT NULL  DEFAULT current_timestamp)')
conn.execute('''CREATE TRIGGER IF NOT EXISTS updated_on_tt
             AFTER UPDATE ON item
             BEGIN
                 UPDATE item set updated_at=current_timestamp where id=new.id;
             END
             ;
             ''')
conn.close()

def get_row(id):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    res = cur.execute('select * from item where id=?',(id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def cursor():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return conn,cur
