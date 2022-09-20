from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3

class StockedList_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1100x600')
        self.layout()

    def layout(self):
        title = Label(self.window, text='원자재 입고리스트', font=("Georgia", 15))
        title.place(x=500, y=20)
        material_sn = Label(self.window, text='원자재 품번')
        material_sn.place(x=20, y=50)
        material_lb = Label(self.window)
        material_lb.place(x=100, y=50)
        no =1
        material_lb.configure(text=f'SJD-{no}')

        # 원자재 frame
        material_fr = LabelFrame(self.window, text='Material Info')
        material_fr.place(x=20, y=80)
        material_name = Label(material_fr, text='원자재 규격')
        material_name.grid(row=0, column=0, padx=5, pady=5)
        namecode_kor_lb = Label(material_fr, text='원자재 품명(국문)')
        namecode_kor_lb.grid(row=0, column=1, padx=5, pady=5)
        namecode_eng_lb = Label(material_fr, text='원자재 품명(영문)')
        namecode_eng_lb.grid(row=0, column=2, padx=5, pady=5)
        kind_lb = Label(material_fr, text='원자재 종류')
        kind_lb.grid(row=0, column=3, padx=5, pady=5)
        hscode_lb = Label(material_fr, text='세번(HS CODE)')
        hscode_lb.grid(row=0, column=4, padx=5, pady=5)
        requriedAmount_lb = Label(material_fr, text='소요량')
        requriedAmount_lb.grid(row=0, column=5, padx=5, pady=5)
        unit_lb = Label(material_fr, text='단위')
        unit_lb.grid(row=0, column=6, padx=5, pady=5)
        ekw_lb = Label(material_fr, text='구성비(EKW기준)')
        ekw_lb.grid(row=0, column=7, padx=5, pady=5)
        manufacturer_lb = Label(material_fr, text='제조사')
        manufacturer_lb.grid(row=0, column=8, padx=5, pady=5)

        name_opt=[]
        material_cmb = ttk.Combobox(material_fr, values=name_opt, height=5, width=15)
        material_cmb.grid(row=1, column=0, padx=5, pady=5)
        namecode_kor_txt = Label(material_fr)
        namecode_kor_txt.grid(row=1, column=1, padx=5, pady=5)
        namecode_eng_txt = Label(material_fr)
        namecode_eng_txt.grid(row=1, column=2, padx=5, pady=5)
        kind_txt = Label(material_fr)
        kind_txt.grid(row=1, column=3, padx=5, pady=5)
        hscode_txt = Label(material_fr)
        hscode_txt.grid(row=1, column=4, padx=5, pady=5)
        requriedAmount_e = Entry(material_fr)
        requriedAmount_e.grid(row=1, column=5, padx=5, pady=5)
        unit_txt = Label(material_fr, text='EA')
        unit_txt.grid(row=1, column=6, padx=5, pady=5)
        ekw_e = Entry(material_fr)
        ekw_e.grid(row=1, column=7, padx=5, pady=5)
        manufacturer_e = Entry(material_fr)
        manufacturer_e.grid(row=1, column=8, padx=5, pady=5)

        # 구매 frame
        Purchase_fr = LabelFrame(self.window, text='Purchase Info')
        Purchase_fr.place(x=20, y=180)
        # 1 row
        vendorname_lb = Label(Purchase_fr, text='구매처')
        vendorname_lb.grid(row=0, column=0, padx=5, pady=5)
        buydate_lb = Label(Purchase_fr, text='구매일자')
        buydate_lb.grid(row=0, column=1, padx=5, pady=5)
        origin_lb = Label(Purchase_fr, text='원산지')
        origin_lb.grid(row=0, column=2, padx=5, pady=5)
        document_lb = Label(Purchase_fr, text='구매입증서류 종류')
        document_lb.grid(row=0, column=3, padx=5, pady=5)
        price_lb = Label(Purchase_fr, text='단가')
        price_lb.grid(row=0, column=4, padx=5, pady=5)
        current_lb = Label(Purchase_fr, text='통화')
        current_lb.grid(row=0, column=5, padx=5, pady=5)
        exchangeRate_lb = Label(Purchase_fr, text='구매일자 환율')
        exchangeRate_lb.grid(row=0, column=6, padx=5, pady=5)
        totalPrice_lb = Label(Purchase_fr, text='가격')
        totalPrice_lb.grid(row=0, column=7, padx=5, pady=5)

        vendorname_opt=[]
        vendorname_cmb = ttk.Combobox(Purchase_fr, values=vendorname_opt, height=5, width=12)
        vendorname_cmb.grid(row=1, column=0, padx=5, pady=5)
        buydate_e = Entry(Purchase_fr)
        buydate_e.grid(row=1, column=1, padx=5, pady=5)
        origin_e = Entry(Purchase_fr)
        origin_e.grid(row=1, column=2, padx=5, pady=5)
        document_txt = Label(Purchase_fr)
        document_txt.grid(row=1, column=3, padx=5, pady=5)
        price_e = Entry(Purchase_fr)
        price_e.grid(row=1, column=4, padx=5, pady=5)
        current_txt = Label(Purchase_fr)
        current_txt.grid(row=1, column=5, padx=5, pady=5)
        exchangeRate_e = Entry(Purchase_fr)
        exchangeRate_e.grid(row=1, column=6, padx=5, pady=5)
        totalPrice_txt = Label(Purchase_fr)
        totalPrice_txt.grid(row=1, column=7, padx=5, pady=5)

        # vendornamee_ =  Entry(Purchase_fr)
        # name_lb.grid(row=0, column=0)
        # name_e.grid(row=0,column=1)


        # current_lb = Label(Purchase_fr, text='통화')
        # current_lb.grid(row=2, column=0)
        # current_txt = Label(Purchase_fr)
        # current_txt.grid(row=2, column=1)
        # document_lb = Label(Purchase_fr, text='구매입증서류 종류')
        # # current_lb = ttk.Combobox(Puchase_fr, height=5, width=20)









    #     lb2.grid(row=1, column=0)
    #     e1.grid(row=1, column=1)
    #
    #     lb3 = Label(self.window, text='통화')
    #     lb4 = Label(self.window)
    #     lb3.grid(row=2, column=0)
    #     lb4.grid(row=2, column=1)
    #
    #     lb5 = Label(self.window, text='구매입증서류')
    #     lb6 = Label(self.window)
    #     lb5.grid(row=3, column=0)
    #     lb6.grid(row=3, column=1)
    #
    #     conn = sqlite3.connect('BOM.db')
    #     cur = conn.cursor()
    #     searched_db = cur.execute('select * from vendor').fetchall()
    #     name_opt = []
    #     for row in searched_db :
    #         name_opt.append(row[1])
    #
    #     cmb1.configure(values = name_opt)
    #     def changeLabel(event) :
    #         sel_name = cmb1.get()
    #         cur.execute('select * from vendor where name=?', (sel_name,))
    #         rs = cur.fetchall()[0]
    #         # print(rs)
    #         lb4.configure(text=rs[2])
    #         lb6.configure(text=rs[3])
    #
    #     cmb1.bind("<<ComboboxSelected>>", changeLabel)
    #
    #     lb7 = Label(self.window, text='품명(영문)')
    #     cmb2 = ttk.Combobox(self.window, values=['SCD', 'PCD'], height=2, width=6)
    #     lb7.grid(row=4, column=0)
    #     cmb2.grid(row=4, column=1)
    #
    #     btn1 = Button(self.window, text='저장', command=self.save)
    #     btn1.grid(row=5,column=0, columnspan=2)
    #
    # def save(self):
    #     # create table
    #     conn = sqlite3.connect('./BOM.db')
    #     conn.execute('PRAGMA foreign_keys = ON')
    #     cur = conn.cursor()
    #     cur.execute('''
    #                  CREATE TABLE IF NOT EXISTS material(
    #                     material_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    #                     vendor_id       INTEGER NOT NULL,
    #                     supplier_name   TEXT    NOT NULL,
    #                     income_date     TEXT    NOT NULL,
    #                     current         TEXT    NOT NULL,
    #                     document        TEXT    NOT NULL,
    #                     item_name_eng   TEXT    NOT NULL,
    #                     FOREIGN KEY (vendor_id)
    #                     REFERENCES vendor (vendor_id)
    #                         ON UPDATE CASCADE
    #                         ON DELETE RESTRICT
    #                     )
    #                  ''')
    #     conn.commit()
    #     conn.close()
    #
    #     # insert data into table
    #     conn = sqlite3.connect('./BOM.db')
    #     cur = conn.cursor()
    #
    #     sel_name = cmb1.get()
    #     cur.execute('select * from vendor where name=?', (sel_name,))
    #     rs = cur.fetchall()[0]
    #
    #     insert_sql = 'INSERT OR IGNORE INTO material values(NULL,?,?,?,?,?,?)'
    #     cur.execute(insert_sql, (rs[0], rs[1], e1.get(), rs[2], rs[3], cmb2.get()))
    #     msgbox.showinfo('등록완료!', '구매처 등록을 완료했습니다.')
    #     conn.commit()
    #     conn.close()