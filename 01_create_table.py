from libs.db.dba import getConn

def create_table() :
    conn = getConn('d:/Users/LG/Desktop/py/project/3_Company/3_BOM/MYSQL_know/abc.db')
    cur = conn.cursor()
    cur.execute('''
    create table test(name text,
    kor int,
    eng int,
    mat int)
    ''')
    conn.commit()
    conn.close()
if __name__ == '__main__' :
    create_table()