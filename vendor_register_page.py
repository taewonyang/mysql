from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
import sqlite3

class Register_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('600x600')

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
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        list_table = cur.execute('''
        select name from sqlite_master where type='table' and name='vendor'
        ''').fetchall()
        print(list_table)
        if list_table == [] :
            print('테이블이 없습니다.')
        else :
            cur.execute('select * from vendor')
            rs = cur.fetchall()
            for i in tree.get_children():
                tree.delete(i)
            for contact in rs:
                tree.insert('', END, values=contact)

    def layout(self):
        global name_cmb, current_cmb, document_cmb
        # 검색 폼
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        list_table = cur.execute('''
                select name from sqlite_master where type='table' and name='vendor'
                ''').fetchall()
        name_opt = []
        current_opt = []
        document_opt = []
        if list_table == []:
            print('테이블이 없습니다.')
        else :
            cur.execute('select * from vendor')
            rs = cur.fetchall()
            for row in rs :
                if (row[0] in name_opt) == False :
                    name_opt.append(row[0])
                if (row[1] in current_opt) == False :
                    current_opt.append(row[1])
                if (row[2] in document_opt) == False :
                    document_opt.append(row[2])
        name_opt.sort()
        current_opt.sort()
        document_opt.sort()

        searchFrame = Frame(self.window)
        searchFrame.place(x=45, y=490)
        name_cmb = ttk.Combobox(searchFrame, height=5, width=26, values=name_opt)
        current_cmb = ttk.Combobox(searchFrame, height=5, width=4, values=current_opt)
        document_cmb = ttk.Combobox(searchFrame, height=5, width=11, values=document_opt)
        name_cmb.pack(side='left', padx=4)
        current_cmb.pack(side='left', padx=4)
        document_cmb.pack(side='left', padx=4)

        # 버튼
        btn_frame = Frame(self.window)
        btn_frame.place(x=485, y=60)
        modify_btn = Button(btn_frame, text='거래처\n 수정 ')
        modify_btn.pack(padx=5, pady=5)
        del_btn = Button(btn_frame, text='거래처\n 삭제 ', command=self.remove)
        del_btn.pack(padx=5, pady=5)

        search_btn = Button(self.window, text='조회')
        search_btn.place(x=425, y=485)
        new_btn = Button(self.window, text='거래처\n 등록 ', command=self.regist)
        new_btn.place(x=485, y=480)

    def regist(self):
        if name_cmb.get() == "":
            msgbox.showerror("입력오류!", "업체명을 입력해주세요")
        elif current_cmb.get() == "":
            msgbox.showerror("입력오류!", "통화를 입력해주세요")
        elif document_cmb.get() == "":
            msgbox.showerror("입력오류!", "구매입증서류를 입력해주세요")
        else:
            # create table
            conn = sqlite3.connect('./BOM.db')
            cur = conn.cursor()
            cur.execute(''' 
             CREATE TABLE IF NOT EXISTS vendor(vendor text, current text, document text)
             ''')
            # insert into table
            cur.execute('select * from vendor')
            rs = cur.fetchall()
            for row in rs :
                data = (name_cmb.get(), current_cmb.get().upper(), document_cmb.get())
                if row == tuple(data) :
                    msgbox.showerror('중복오류!', '이미 존재하는 데이터입니다.\n다시 입력해주세요.')
                else :
                    insert_sql = 'INSERT OR IGNORE INTO vendor values(?,?,?)'
                    cur.execute(insert_sql, (name_cmb.get(), current_cmb.get().upper(), document_cmb.get()))
                    msgbox.showinfo('등록완료!', '구매처 등록을 완료했습니다.')
                    conn.commit()
                    conn.close()

                    name_cmb.set('')
                    current_cmb.set('')
                    document_cmb.set('')

                    self.tree_data_view()

    def remove(self):
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        list_table = cur.execute('''
                select name from sqlite_master where type='table' and name='vendor'
                ''').fetchall()
        if list_table == []:
            print('테이블이 없습니다.')
        else:
            selectedItem = tree.focus()
            getValue = tree.item(selectedItem).get('values')
            if selectedItem == "" :
                msgbox.showerror('선택 오류', '삭제할 데이터를 선택해주세요.')
            else :
                response = msgbox.askyesno('예/아니오', '해당 데이터를 삭제합니까?')
                if response == 1 :
                    cur.execute('delete from vendor where vendor=:con1 and current=:con2 and document=:con3', {"con1":getValue[0], "con2":getValue[1], "con3":getValue[2]})
                    conn.commit()
                    conn.close()
                    msgbox.showinfo('삭제완료!', '삭제를 완료했습니다.')

                    self.tree_data_view()
                elif response == 0 :
                    return