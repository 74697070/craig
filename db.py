import sqlite3

conn = sqlite3.connect('listings.db')
c = conn.cursor()

def init():
    c.execute('''create table if not exists Results 
            (repost_of text, date text, url text, price text, name text, id text)''')

def insert_row(*args):
    c.execute('insert into Results values (?,?,?,?,?,?)', args)

def fetch_query(id):
    c.execute('select * from Results where id = ?', (id,))
    return c.fetchone()

init()
