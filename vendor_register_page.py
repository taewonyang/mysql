from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
import sqlite3

class Register_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('580x600')

        self.create_tree_widget()
        self.tree_data_view()
        self.layout()

    def create_tree_widget(self):
        global tree
        tree_frame = Frame(self.window)
        tree_frame.place(x=50, y=60, width=390, height=400)

        columns = ('name_column', 'current_column', 'document_column')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        tree.heading('name_column', text='업체명', anchor=CENTER)
        tree.heading('current_column', text='통화', anchor=CENTER)
        tree.heading('document_column', text='구매입증서류', anchor=CENTER)
        tree.column('name_column', width=200)
        tree.column('current_column', width=60)
        tree.column('document_column', width=100)
        tree.place(relheight=1, relwidth=1)

        scrollbar = Scrollbar(tree_frame, orient="vertical")
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

    def tree_data_view(self):
        db_filename = 'BOM.db'
        cur_dir = os.getcwd()
        file_path = cur_dir+'\\'+db_filename
        if os.path.isfile(file_path) == True :
            conn = sqlite3.connect('./BOM.db')
            cur = conn.cursor()
            cur.execute('select * from vendor')
            rs = cur.fetchall()

            for i in tree.get_children():
                tree.delete(i)
            for contact in rs:
                tree.insert('', END, values=contact)
        else:
            print('파일이 없습니다.')

    def layout(self):
        # 검색 폼
        searchFrame = Frame(self.window)
        searchFrame.place(x=10 ,y=490)
        search_lb = Label(searchFrame, text='검색')
        search_lb.pack(side='left', padx=3)

        name_opt = []
        current_opt = []
        document_opt=[]
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        cur.execute('select * from vendor')
        rs = cur.fetchall()
        for row in rs :
            if (row[0] in name_opt) == False :
                name_opt.append(row[0])
            if (row[1] in current_opt) == False :
                current_opt.append(row[1])
            if (row[2] in document_opt) == False :
                document_opt.append(row[2])

        nameSearch_cmb = ttk.Combobox(searchFrame, height=5, width=26, values=name_opt)
        currentSearch_cmb = ttk.Combobox(searchFrame, height=5, width=4, values=current_opt)
        documentSearch_cmb = ttk.Combobox(searchFrame, height=5, width=11, values=document_opt)
        nameSearch_cmb.pack(side='left', padx=4)
        currentSearch_cmb.pack(side='left', padx=4)
        documentSearch_cmb.pack(side='left', padx=4)

        # 등록btn
        btn_frmae = Frame(self.window)
        btn_frmae.place(x=460, y=60)
        new_btn = Button(btn_frmae, text='업체 등록', command=self.create_register_widget())
        new_btn.pack(padx=5, pady=5)
        modify_btn = Button(btn_frmae, text='업체 수정')
        modify_btn.pack(padx=5, pady=5)
        del_btn = Button(btn_frmae, text='업체 삭제')
        del_btn.pack(padx=5, pady=5)


    def create_register_widget(self):
        global vendor_name_txt, currency_cmb, document_cmb, new_win
        new_win = Toplevel()
        new_win.geometry('400x300')
        new_win.resizable(False, False)

        register_frame = LabelFrame(new_win, text='구매처 입력')
        register_frame.place(x=30, y=70)

        vendor_name_lb = Label(register_frame, text='업체명')
        vendor_name_lb.grid(row=0, column=0, sticky='w')
        vendor_name_txt = Entry(register_frame, width=30)
        vendor_name_txt.grid(row=0, column=1, sticky='w')
        currency_lb = Label(register_frame, text='통화')
        currency_lb.grid(row=1, column=0,sticky='w')
        currency_opt = ['KRW', 'CNY', 'RMB', 'USD', 'EUR']
        currency_cmb = ttk.Combobox(register_frame, state='readonly', values=currency_opt, height=5, width=5)
        currency_cmb.current(0)
        currency_cmb.grid(row=1, column=1,sticky='w')

        document_lb = Label(register_frame, text='구매입증서류')
        document_lb.grid(row=2, column=0,sticky='w')
        document_opt = ['거래명세표', '수입면장']
        document_cmb = ttk.Combobox(register_frame, state='readonly', values=document_opt, height=2, width=10)
        document_cmb.current(0)
        document_cmb.grid(row=2, column=1,sticky='w')

        register_btn = Button(new_win, text='등록하기', command=self.register)
        register_btn.place(x=200, y= 250)

    def register(self):
        if vendor_name_txt.get() == "":
            msgbox.showerror("입력오류!", "업체명을 입력해주세요")
        else:
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
            self.tree_data_view()

