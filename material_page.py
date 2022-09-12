from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3
PRAGMA foreign_keys = ON

class Material_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('600x600')
        self.layout()

    def layout(self):
        global cmb1, e1, lb4, lb6, cmb2
        lb1 = Label(self.window, text='구매처')
        cmb1 = ttk.Combobox(self.window, height=5, width=20)
        lb1.grid(row=0, column=0)
        cmb1.grid(row=0, column=1)

        lb2 = Label(self.window, text='구매일자')
        e1 = Entry(self.window)
        lb2.grid(row=1, column=0)
        e1.grid(row=1, column=1)

        lb3 = Label(self.window, text='통화')
        lb4 = Label(self.window)
        lb3.grid(row=2, column=0)
        lb4.grid(row=2, column=1)

        lb5 = Label(self.window, text='구매입증서류')
        lb6 = Label(self.window)
        lb5.grid(row=3, column=0)
        lb6.grid(row=3, column=1)

        conn = sqlite3.connect('BOM.db')
        cur = conn.cursor()
        searched_db = cur.execute('select * from vendor').fetchall()
        name_opt = []
        for row in searched_db :
            name_opt.append(row[1])

        cmb1.configure(values = name_opt)
        def changeLabel(event) :
            sel_name = cmb1.get()
            cur.execute('select * from vendor where name=?', (sel_name,))
            rs = cur.fetchall()[0]
            # print(rs)
            lb4.configure(text=rs[2])
            lb6.configure(text=rs[3])

        cmb1.bind("<<ComboboxSelected>>", changeLabel)

        lb7 = Label(self.window, text='품명(영문)')
        cmb2 = ttk.Combobox(self.window, values=['SCD', 'PCD'], height=2, width=6)
        lb7.grid(row=4, column=0)
        cmb2.grid(row=4, column=1)

        btn1 = Button(self.window, text='저장', command=self.save)
        btn1.grid(row=5,column=0, columnspan=2)

    def save(self):
        # create table
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        cur.execute(''' 
                     CREATE TABLE IF NOT EXISTS material(
                        material_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                        vendor_id       INTEGER NOT NULL,
                        supplier_name   TEXT    NOT NULL,
                        income_date     TEXT    NOT NULL,
                        current         TEXT    NOT NULL,
                        document        TEXT    NOT NULL,
                        item_name_eng   TEXT    NOT NULL,
                        FOREIGN KEY (vendor_id)
                            REFERENCES vendor (vendor_id)
                        )
                     ''')
        conn.commit()
        conn.close()

        # insert data into table
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()

        sel_name = cmb1.get()
        cur.execute('select * from vendor where name=?', (sel_name,))
        rs = cur.fetchall()[0]
        print(rs)

        insert_sql = 'INSERT OR IGNORE INTO material values(NULL,?,?,?,?,?,?)'
        cur.execute(insert_sql, (rs[0], rs[1], e1.get(), rs[2], rs[3], cmb2.get()))
        msgbox.showinfo('등록완료!', '구매처 등록을 완료했습니다.')
        conn.commit()
        conn.close()


