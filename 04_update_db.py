import sqlite3
from libs.db.dba import getConn
def update_a() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    up_sql = 'update test set name=? where name=?'
    cur.execute(up_sql, ('홍일정', '홍길동'))
    conn.commit()
    conn.close()

if __name__ == '__main__' :
    update_a()