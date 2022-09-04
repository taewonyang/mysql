import sqlite3

def getConn(dbpath) :
    conn = sqlite3.connect(dbpath)
    return conn
