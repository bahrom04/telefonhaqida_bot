import sqlite3

def sql_start():
    global conn,cur
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    if conn:
        print('Data Base connected')
    cur.execute('CREATE TABLE IF NOT EXISTS user_number(name TEXT, id TEXT PRIMARY KEY)')
    conn.commit()

def user_number():
    fetch = cur.execute('SELECT id FROM user_number').fetchall()
    print(fetch)
    return fetch

def add(a):
    cur.execute('INSERT INTO user_number VALUES (?,?)', a)
    conn.commit()

