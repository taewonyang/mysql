from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3

class Register_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('800x600')

        self.layout()

    def layout(self):
        global vendor_name_txt, currency_cmb, document_cmb
        register_frame = LabelFrame(self.window, text='구매처 입력')
        register_frame.pack()

        vendor_name_lb = Label(register_frame, text='업체명')
        vendor_name_lb.grid(row=0, column=0)
        vendor_name_txt = Entry(register_frame, width=30)
        vendor_name_txt.grid(row=0, column=1)

        currency_lb = Label(register_frame, text='통화')
        currency_lb.grid(row=1, column=0)
        currency_opt = ['KRW', 'CNY', 'RMB', 'USD', 'EUR']
        currency_cmb = ttk.Combobox(register_frame, state='readonly', values = currency_opt ,height=5, width=5)
        currency_cmb.current(0)
        currency_cmb.grid(row=1, column=1)

        document_lb = Label(register_frame, text='구매입증서류')
        document_lb.grid(row=2, column=0)
        document_opt = ['거래명세표', '수입면장']
        document_cmb = ttk.Combobox(register_frame, state='readonly', values = document_opt, height=2, width=10)
        document_cmb.current(0)
        document_cmb.grid(row=2, column=1)

        register_btn = Button(register_frame, text='등록', command=self.register)
        register_btn.grid(row=3, column=0, columnspan=2)

    def register(self):
        if vendor_name_txt.get() == "" :
            msgbox.showerror("입력오류!", "업체명을 입력해주세요")
        else :
            # create table
            conn = sqlite3.connect('./BOM.db')
            cur = conn.cursor()
            cur.execute(''' 
            CREATE TABLE IF NOT EXISTS vendor(vendor text, current text, document text)
            ''')
            # insert into table
            insert_sql = 'insert into vendor values(?,?,?)'
            cur.execute(insert_sql, (vendor_name_txt.get(), currency_cmb.get(), document_cmb.get()))
            conn.commit()
            conn.close()

            msgbox.showinfo('등록완료!', '구매처 등록을 완료했습니다.')
