from libs.db.dba import getConn
import sqlite3
def select_a() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    cur.execute('select * from test')
    print('전체데이터 출력하기')
    rs = cur.fetchall()
    for i in rs :
        print(i)
    conn.close()
def select_b(num, name) :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    cur.execute('select * from test where name=?', (name,))  #튜플의 형태여함!!!(name,)
    print('데이터 가져오기')
    rs = cur.fetchmany(num)
    for i in rs :
        print(i)

if __name__ == '__main__' :
    select_a()
    select_b(1, '홍길동')