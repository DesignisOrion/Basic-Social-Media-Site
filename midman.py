import sqlite3 as sql
from os import path

ROOT = path.dirname(path.realpath(__file__))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'Social.db'))
    cur = con.cursor()
    cur.execute("insert into posts (name, content) VALUES (?, ?)", (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'Social.db'))
    cur = con.cursor()
    cur.execute("select name, content from posts")
    posts = cur.fetchall()
    return posts