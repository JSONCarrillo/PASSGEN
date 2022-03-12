import sqlite3 as sq
from cryptography.fernet import Fernet

db = 'data.db'

def connect():
    connection = sq.connect(db)
    con = connection.cursor()
    con.execute(
        """
            CREATE TABLE IF NOT EXISTS data (
                site text,
                user text,
                password text primary key
            )
        """
    )

    connection.commit()
    connection.close()

def enter(user, site, passwd):
    connection = sq.connect(db)
    con = connection.cursor()
    con.execute("INSERT INTO data VALUES(?,?,?)", (site, user, passwd))
    connection.commit()
    connection.close()

def show():
    connection = sq.connect(db)
    con = connection.cursor()
    con.execute("SELECT * FROM data")
    fetch = con.fetchall()
    connection.commit()
    connection.close()
    return fetch

def Delete(password):
    connection = sq.connect(db)
    con = connection.cursor()
    con.execute("DELETE FROM data WHERE password=(?)", (password,))
    connection.commit()
    connection.close()

def edit(user, site, passwd):
    connection = sq.connect(db)
    con = connection.cursor()
    con.execute("UPDATE data SET site=(?), user=(?) WHERE password=(?)", (site, user, passwd))
    connection.commit()
    connection.close()

def checkIfEmpty():
    if len(show()) == 0:
        return True
    else:
        return False

connect()