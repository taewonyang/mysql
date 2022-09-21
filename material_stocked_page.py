from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3

class StockedList_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1000x800')
        self.layout()
        self.dbLoad()

    def layout(self):
        global material_cmb, namecode_kor_txt, namecode_eng_txt, kind_txt, hscode_txt
        global vendorName_cmb, document_txt, current_txt, buydate_e, exchangeRate_e, price_e, totalPrice_txt, manufacturer_e, unit_e, origin_e
        title = Label(self.window, text='원자재 입고리스트', font=("Georgia", 15))
        title.place(x=430, y=20)
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
        material_name.grid(row=0, column=0, padx=5, pady=3)
        namecode_kor_lb = Label(material_fr, text='원자재 품명(국문)')
        namecode_kor_lb.grid(row=0, column=1, padx=5, pady=3)
        namecode_eng_lb = Label(material_fr, text='원자재 품명(영문)')
        namecode_eng_lb.grid(row=0, column=2, padx=5, pady=3)
        kind_lb = Label(material_fr, text='원자재 종류')
        kind_lb.grid(row=0, column=3, padx=5, pady=3)
        hscode_lb = Label(material_fr, text='세번(HS CODE)')
        hscode_lb.grid(row=0, column=4, padx=5, pady=3)
        requriedAmount_lb = Label(material_fr, text='소요량')
        requriedAmount_lb.grid(row=0, column=5, padx=5, pady=3)
        unit_lb = Label(material_fr, text='단위')
        unit_lb.grid(row=0, column=6, padx=5, pady=3)
        ekw_lb = Label(material_fr, text='구성비(EKW기준)')
        ekw_lb.grid(row=0, column=7, padx=5, pady=3)
        manufacturer_lb = Label(material_fr, text='제조사')
        manufacturer_lb.grid(row=0, column=8, padx=5, pady=3)
        origin_lb = Label(material_fr, text='원산지')
        origin_lb.grid(row=0, column=9, padx=5, pady=3)

        material_cmb = ttk.Combobox(material_fr, height=5, width=15)
        material_cmb.grid(row=1, column=0, padx=5, pady=3)
        namecode_kor_txt = Label(material_fr, width=15)
        namecode_kor_txt.grid(row=1, column=1, padx=5, pady=3)
        namecode_eng_txt = Label(material_fr, width=10)
        namecode_eng_txt.grid(row=1, column=2, padx=5, pady=3)
        kind_txt = Label(material_fr, width=7)
        kind_txt.grid(row=1, column=3, padx=5, pady=3)
        hscode_txt = Label(material_fr, width=12)
        hscode_txt.grid(row=1, column=4, padx=5, pady=3)
        requriedAmount_e = Entry(material_fr, width=7)
        requriedAmount_e.grid(row=1, column=5, padx=5, pady=3)
        unit_e = Entry(material_fr, width=5, justify='center')
        unit_e.grid(row=1, column=6, padx=5, pady=3)
        ekw_e = Entry(material_fr, width=13)
        ekw_e.grid(row=1, column=7, padx=5, pady=3)
        manufacturer_e = Entry(material_fr, width=7, justify='center')
        manufacturer_e.grid(row=1, column=8, padx=5, pady=3)
        origin_e = Entry(material_fr, width=7, justify='center')
        origin_e.grid(row=1, column=9, padx=5, pady=3)


        # 구매 frame
        Purchase_fr = LabelFrame(self.window, text='Purchase Info')
        Purchase_fr.place(x=20, y=160)

        vendorname_lb = Label(Purchase_fr, text='구매처')
        vendorname_lb.grid(row=0, column=0, padx=5, pady=3)
        buydate_lb = Label(Purchase_fr, text='구매일자')
        buydate_lb.grid(row=0, column=1, padx=5, pady=3)
        exchangeRate_lb = Label(Purchase_fr, text='(구매일) 환율')
        exchangeRate_lb.grid(row=0, column=2, padx=5, pady=3)
        price_lb = Label(Purchase_fr, text='단가')
        price_lb.grid(row=0, column=3, padx=5, pady=3)
        current_lb = Label(Purchase_fr, text='통화')
        current_lb.grid(row=0, column=4, padx=5, pady=3)
        totalPrice_lb = Label(Purchase_fr, text='가격')
        totalPrice_lb.grid(row=0, column=5, padx=5, pady=3)
        document_lb = Label(Purchase_fr, text='구매입증서류 종류')
        document_lb.grid(row=0, column=6, padx=5, pady=3)

        vendorName_cmb = ttk.Combobox(Purchase_fr, height=5, width=15)
        vendorName_cmb.grid(row=1, column=0, padx=5, pady=3)
        buydate_e = Entry(Purchase_fr, width=10)
        buydate_e.grid(row=1, column=1, padx=5, pady=3)
        exchangeRate_e = Entry(Purchase_fr, width=10)
        exchangeRate_e.grid(row=1, column=2, padx=5, pady=3)
        price_e = Entry(Purchase_fr, width=10)
        price_e.grid(row=1, column=3, padx=5, pady=3)
        current_txt = Label(Purchase_fr, width=8)
        current_txt.grid(row=1, column=4, padx=5, pady=3)
        totalPrice_txt = Label(Purchase_fr, width=15)
        totalPrice_txt.grid(row=1, column=5, padx=5, pady=3)
        document_txt = Label(Purchase_fr)
        document_txt.grid(row=1, column=6, padx=5, pady=3)


    def dbLoad(self):
        conn = sqlite3.connect('BOM.db')
        cur = conn.cursor()
        # 원자재
        material_db = cur.execute('select * from material_info').fetchall()
        materialName_opt =[]
        for row in material_db :
            materialName_opt.append(row[1])
        material_cmb.configure(values = materialName_opt)

        def changeLabel_material(event):
            sel_name = material_cmb.get()
            cur.execute('select * from material_info where material_name=?', (sel_name,))
            rs = cur.fetchall()[0]
            namecode_kor_txt.configure(text=rs[2])
            namecode_eng_txt.configure(text=rs[3])
            kind_txt.configure(text=rs[4])
            hscode_txt.configure(text=rs[5])

        material_cmb.bind("<<ComboboxSelected>>", changeLabel_material)


        # 구매정보
        vendor_db = cur.execute('select * from vendor').fetchall()
        name_opt = []
        for row in vendor_db :
            name_opt.append(row[1])
        vendorName_cmb.configure(values = name_opt)

        def changeLabel_purchase(event):
            sel_name = vendorName_cmb.get()
            cur.execute('select * from vendor where name=?', (sel_name,))
            rs = cur.fetchall()[0]
            document_txt.configure(text=rs[3])
            current_txt.configure(text=rs[2])

        def toatl_cal(event) :
            try :
                if exchangeRate_e.get() !="" and price_e.get() !="" :
                    total_p = float(exchangeRate_e.get()) * float(price_e.get())
                    totalPrice_txt.configure(text=total_p)
                else :
                    totalPrice_txt.configure(text="")
            except :
                print('예외처리')

        vendorName_cmb.bind("<<ComboboxSelected>>", changeLabel_purchase)
        price_e.bind("<KeyRelease>", toatl_cal)
        exchangeRate_e.bind("<KeyRelease>", toatl_cal)

        # 기본설정
        manufacturer_e.insert(0,"미상")
        unit_e.insert(0,"EA")
        origin_e.insert(0,"미상")


        # buydate_e, exchangeRate_e, price_e, totalPrice_txt
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