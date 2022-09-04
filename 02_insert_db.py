import sqlite3
from libs.db.dba import getConn
def insert_b() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    cur.execute('''
    insert into test values('홍길동',80,90,100)
    ''')
    conn.commit()
    conn.close()
def insert_c() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    ins_sql = 'insert into test values(?,?,?,?)'
    cur.execute(ins_sql, ('김철수',77,88,99)) #튜플형식으로 들어가야한다 반드시!!!!
    conn.commit()
    conn.close()
def insert_d() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    ins_sql = 'insert into test values(?,?,?,?)'
    li = [('김철수2',72,82,92), ('김철수3',73,83,93), ('김철수4',74,84,94)]
    cur.executemany(ins_sql, li)
    conn.commit()
    conn.close()

if __name__ == '__main__' :
    # insert_b()
    # insert_c()
    insert_d()
