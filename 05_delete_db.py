import sqlite3
from libs.db.dba import getConn
def delete_a() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    cur.execute('delete from test where eng<=?', (85,))
    conn.commit()
    conn.close()

if __name__ == '__main__' :
    delete_a()