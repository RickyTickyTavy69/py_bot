import sqlite3


def create_db():
    cur, conn = connect_db()
    db_execute('CREATE TABLE IF NOT EXISTS users'
                '(id int auto_increment primary key, name varchar(50), pass varchar(255))', cur, conn)

    close_connection(cur, conn)


def connect_db():
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    return cur, conn


def close_connection(cur, conn):
    cur.close()
    conn.close()


def db_execute(query, cur, conn):
    cur.execute(query)
    conn.commit()
