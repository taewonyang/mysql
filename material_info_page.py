from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3

class Material_Info :
    def __init__(self, window):
        self.window = window
        self.window.geometry('600x600')

        self.layout()
        self.create_tree_widget()
        self.tree_data_view()

        def changeText(event):
            if namecode_eng_cmb.get() == "SCD":
                namecode_kor_txt.configure(text='단결정 다이아몬드')
                kind_txt.configure(text='원석')
            elif namecode_eng_cmb.get() == "PCD":
                namecode_kor_txt.configure(text='다결정 다이아몬드')
                kind_txt.configure(text='원석')
            elif namecode_eng_cmb.get() == "SHANK":
                namecode_kor_txt.configure(text='샹크')
                kind_txt.configure(text='기타')

        def selectedText(event):
            selectedItem = tree.focus()
            getValue = tree.item(selectedItem).get('values')
            self.cancel()
            if selectedItem != "" :
                name_e.insert(0, getValue[0])
                namecode_eng_cmb.set(getValue[1])
                namecode_kor_txt.configure(text=getValue[2])
                kind_txt.configure(text=getValue[3])
                hscode_e.insert(0, getValue[4])

        tree.bind("<<TreeviewSelect>>", selectedText)
        namecode_eng_cmb.bind("<<ComboboxSelected>>", changeText)

    def layout(self):
        title = Label(self.window, text='Material Info', font=("Georgia",15))
        title.place(x=240, y=10)
        global name_e, namecode_eng_cmb, namecode_kor_txt, kind_txt, hscode_e

        name_lb = Label(self.window, text='원자재 규격')
        name_lb.place(x=10, y=60)
        name_e = Entry(self.window, width=20)
        name_e.place(x=120, y=60)
        namecode_eng_lb = Label(self.window, text='원자재 품명(영문)')
        namecode_eng_lb.place(x=10, y=90)
        namecode_eng_cmb = ttk.Combobox(self.window, height=3, width=8, values=['SCD','PCD','SHANK'], state='readonly')
        namecode_eng_cmb.place(x=120, y=90)
        namecode_kor_lb = Label(self.window, text='원자재 품명(국문)')
        namecode_kor_lb.place(x=10, y=120)
        namecode_kor_txt = Label(self.window, width=20, anchor='w')
        namecode_kor_txt.place(x=120, y=120)
        kind_lb = Label(self.window, text='원자재 종류')
        kind_lb.place(x=360, y=60)
        kind_txt = Label(self.window, width=9, anchor='w')
        kind_txt.place(x=460, y=60)
        hscode_lb = Label(self.window, text='세번(HS CODE)')
        hscode_lb.place(x=360, y= 90)
        hscode_e = Entry(self.window, width=12)
        hscode_e.place(x=460, y=90)

        save_btn = Button(self.window, text=' Save ', command=self.regist)
        save_btn.place(x=460, y=130)
        cancel_btn = Button(self.window, text='Cancel', command=self.cancel)
        cancel_btn.place(x=510, y=130)
        update_btn = Button(self.window, text=' 수정 ', command=self.edit)
        update_btn.place(x=520, y=200)
        delete_btn = Button(self.window, text=' 삭제 ', command=self.remove)
        delete_btn.place(x=520, y=250)

    def create_tree_widget(self):
        global tree
        tree_frame = Frame(self.window)
        tree_frame.place(x=10, y=200, width=500, height=360)

        columns = ('name_column', 'namecode_eng_column', 'namecode_kor_column', 'kind_column', 'hscode_column')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        tree.heading('name_column', text='규격', anchor=CENTER)
        tree.heading('namecode_eng_column', text='품명(영문)', anchor=CENTER)
        tree.heading('namecode_kor_column', text='품명(국문)', anchor=CENTER)
        tree.heading('kind_column', text='종류', anchor=CENTER)
        tree.heading('hscode_column', text='HS CODE', anchor=CENTER)
        tree.column('name_column', width=100)
        tree.column('namecode_eng_column', width=60)
        tree.column('namecode_kor_column', width=100)
        tree.column('kind_column', width=30, anchor=CENTER)
        tree.column('hscode_column', width=70, anchor=CENTER)
        tree.place(relheight=1, relwidth=1)

        scrollbar = Scrollbar(tree_frame, orient="vertical")
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

    def tree_data_view(self):
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        list_table = cur.execute('''
                select name from sqlite_master where type='table' and name='material_info'
                ''').fetchall()
        if list_table == []:
            print('테이블이 없습니다.')
        else:
            # 트리뷰 새로고침
            cur.execute('select * from material_info')
            rs = cur.fetchall()
            for i in tree.get_children():
                tree.delete(i)
            for row in rs:
                tree.insert('', END, values=row[1:])

    def regist(self):
        if name_e.get() == "":
            msgbox.showerror("입력오류!", "규격명을 입력해주세요")
        elif namecode_eng_cmb.get() == "":
            msgbox.showerror("입력오류!", "품명(영문)을 선택해주세요")
        elif hscode_e.get() == "":
            msgbox.showerror("입력오류!", "세번을 입력해주세요")
        else:
            # create table
            conn = sqlite3.connect('./BOM.db')
            conn.execute('PRAGMA foreign_keys = ON')
            cur = conn.cursor()
            cur.execute(''' 
             CREATE TABLE IF NOT EXISTS material_info(
                material_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                material_name       TEXT    NOT NULL,
                namecode_kor        TEXT    NOT NULL,
                namecode_eng        TEXT    NOT NULL,
                material_kind       TEXT    NOT NULL,
                hscode              TEXT    NOT NULL
                )
             ''')

            # insert data into table
            cur.execute('select * from material_info')
            rs = cur.fetchall()

            # 중복여부 체크
            data = (str(name_e.get()), str(namecode_eng_cmb.get()), str(namecode_kor_txt.cget('text')), str(kind_txt.cget('text')),str(hscode_e.get()))
            overlap_check = []
            if rs != []:  # DB에 데이터가 있다면
                for row in rs:
                    print(row)
                    if row[1:] == tuple(data):
                        overlap_check.append('ok')
                        break
            # (데이터O / 중복O)
            if overlap_check != []:
                msgbox.showerror('중복오류!', '이미 존재하는 데이터입니다.\n다시 입력해주세요.')
            # (데이터O / 중복X) or (데이터X)
            else:
                insert_sql = 'INSERT INTO material_info values(NULL,?,?,?,?,?)'
                cur.execute(insert_sql, data)
                msgbox.showinfo('등록완료!', '원자재 정보를 등록하였습니다.')
                conn.commit()
                conn.close()

                self.tree_data_view()
                self.cancel()

    def cancel(self):
        name_e.delete(0, END)
        namecode_eng_cmb.set("")
        namecode_kor_txt.configure(text='')
        kind_txt.configure(text='')
        hscode_e.delete(0, END)

    def remove(self):
        conn = sqlite3.connect('./BOM.db')
        cur = conn.cursor()
        list_table = cur.execute('''
                        select name from sqlite_master where type='table' and name='material_info'
                        ''').fetchall()
        if list_table == []:
            msgbox.showerror('선택 오류', '삭제할 데이터를 선택해주세요.')
        else:
            selectedItem = tree.focus()
            getValue = tree.item(selectedItem).get('values')
            if selectedItem == "":
                msgbox.showerror('선택 오류', '삭제할 데이터를 선택해주세요.')
            else:
                response = msgbox.askyesno('예/아니오', '해당 데이터를 삭제합니까?')
                if response == 1:
                    cur.execute('''delete from material_info 
                                where material_name=:con1 and namecode_kor=:con2 and namecode_eng=:con3
                                    and material_kind=:con4 and hscode=:con5''',
                                {"con1": getValue[0], "con2": getValue[1], "con3": getValue[2], "con4": getValue[3], "con5": getValue[4]})
                    conn.commit()
                    conn.close()
                    msgbox.showinfo('삭제완료!', '삭제를 완료했습니다.')

                    self.tree_data_view()
                    self.cancel()
                elif response == 0:
                    return
    def edit(self):
        selectedItem = tree.focus()
        getValue = tree.item(selectedItem).get('values')
        if selectedItem == "" :
            msgbox.showerror('선택 오류', '수정할 데이터를 선택해주세요.')
        else :
            if name_e.get() == "":
                msgbox.showerror("입력오류!", "변경할 규격명을 입력해주세요")
            elif namecode_eng_cmb.get() == "":
                msgbox.showerror("입력오류!", "변경할 품명(영문)를 선택해주세요")
            elif hscode_e.get== "" :
                msgbox.showerror("입력오류!", "변경할 세번(HS CODE)를 입력해주세요")
            else:
                response = msgbox.askyesno('예/아니오', '입력된 내용으로 수정하시겠습니까?')
                if response == 1:
                    conn = sqlite3.connect('./BOM.db')
                    cur = conn.cursor()
                    update_query = '''
                    update material_info set material_name=?, namecode_kor=?, namecode_eng=?, material_kind=?, hscode=?
                        where material_name=? and namecode_kor=? and namecode_eng=? and material_kind=? and hscode=?
                    '''
                    query_data = (name_e.get(), namecode_eng_cmb.get(), namecode_kor_txt.cget('text'), kind_txt.cget('text'), hscode_e.get(), getValue[0], getValue[1], getValue[2], getValue[3], getValue[4])
                    cur.execute(update_query, query_data)
                    msgbox.showinfo('수정완료!', '데이터가 수정되었습니다.')
                    conn.commit()
                    conn.close()

                    self.tree_data_view()
                else :
                    return