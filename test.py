import sqlite3 as sl
import sys

slConnection = sl.connect('first-sqlite.db')
slConnection.execute("PRAGMA foreign_keys = 1")

slCursor = slConnection.cursor()

createParentTabelQuery = '''CREATE TABLE IF NOT EXISTS stock (
                    stockid     INTEGER PRIMARY KEY,
                    stockname   TEXT NOT NULL,
                    stocksymbol TEXT); '''
createChildTableQuery = '''CREATE TABLE IF NOT EXISTS stockprice (
                    id          INTEGER PRIMARY KEY,
                    quantity    INT NOT NULL,
                    price   REAL,
                    stockid INT,
                    FOREIGN KEY (stockid) REFERENCES stock (stockid) );'''

insertParentTableQuery = '''INSERT INTO stock (stockname, stocksymbol) VALUES ('firststock', 'FRS');'''
insertChildTableQuery = '''INSERT INTO stockprice (quantity, price, stockid) VALUES (10, 15.0, 4);'''
deleteParentTableQuery = '''DELETE FROM stock;'''
selectParentTableQuery = '''SELECT * FROM stock;'''
selectChildTableQuery = '''SELECT * FROM stockprice;'''

slCursor.execute(createParentTabelQuery)
slCursor.execute(createChildTableQuery)
# slCursor.execute(insertParentTableQuery)
# slCursor.execute(insertChildTableQuery)
slCursor.execute(deleteParentTableQuery)
print(slCursor.execute(selectParentTableQuery).fetchall())
print(slCursor.execute(selectChildTableQuery).fetchall())

slConnection.commit()

slCursor.close()
slConnection.close()
sys.exit