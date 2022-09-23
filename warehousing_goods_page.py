from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog
import os
import shutil
import sqlite3

class Warehousing_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1000x900')
        self.window.resizable(False, False)
        self.layout()
        self.initialDB()

        global folderName, destination
        folderName = []
        destination = []

    def layout(self):
        global material_cmb, namecode_kor_txt, namecode_eng_txt, kind_txt, hscode_txt, material_txt
        global vendorName_cmb, document_txt, current_txt, buydate_e, exchangeRate_e, price_e, totalPrice_txt, manufacturer_e, unit_e, origin_e, docMaterial_txt, docOrigin_txt
        title = Label(self.window, text='원자재 입고리스트', font=("Georgia", 15))
        title.place(x=430, y=20)
        material_sn = Label(self.window, text='원자재 품번')
        material_sn.place(x=20, y=50)
        material_txt = Label(self.window)
        material_txt.place(x=100, y=50)
        no =1
        material_txt.configure(text=f'SJD-{no}')

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
        namecode_eng_txt = Label(material_fr, width=17)
        namecode_eng_txt.grid(row=1, column=2, padx=5, pady=3)
        kind_txt = Label(material_fr, width=7)
        kind_txt.grid(row=1, column=3, padx=5, pady=3)
        hscode_txt = Label(material_fr, width=12)
        hscode_txt.grid(row=1, column=4, padx=5, pady=3)
        requriedAmount_e = Entry(material_fr, width=7)
        requriedAmount_e.grid(row=1, column=5, padx=5, pady=3)
        unit_e = Entry(material_fr, width=5, justify='center')
        unit_e.grid(row=1, column=6, padx=5, pady=3)
        pack_lb = Label(material_fr)
        pack_lb.grid(row=1, column=7, padx=5, pady=3)
        ekw_e = Entry(pack_lb, width=9)
        ekw_e.grid(row=0, column=0, padx=5, pady=3)
        perText_lb = Label(pack_lb, text='%')
        perText_lb.grid(row=0, column=1)
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
        docMaterial_lb = Label(Purchase_fr, text='구매입증서류')
        docMaterial_lb.grid(row=0, column=7, padx=5, pady=3)
        docOrigin_lb = Label(Purchase_fr, text='원산지증빙서류')
        docOrigin_lb.grid(row=0, column=8, padx=5, pady=3)

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
        pack1_lb = Label(Purchase_fr)
        pack1_lb.grid(row=1, column=7, padx=5, pady=3)
        docMaterial_txt = Label(pack1_lb)
        docMaterial_txt.grid(row=0, column=0, padx=1, pady=3)
        addfile_btn1 = Button(pack1_lb, text='파일첨부', command=self.open_attachWin_purchase)
        addfile_btn1.grid(row=0, column=1, padx=1, pady=3)
        pack2_lb = Label(Purchase_fr)
        pack2_lb.grid(row=1, column=8, padx=5, pady=3)
        docOrigin_txt = Label(pack2_lb)
        docOrigin_txt.grid(row=0, column=0, padx=1, pady=3)
        addfile_btn2 = Button(pack2_lb, text='파일첨부', command=self.open_attachWin_origin)
        addfile_btn2.grid(row=0, column=1, padx=1, pady=3)

        # 버튼
        db_insert_btn = Button(self.window, text='save')
        db_insert_btn.place(x=830, y=260)

    def initialDB(self):
        # 기본설정
        manufacturer_e.insert(0, "미상")
        unit_e.insert(0, "EA")
        origin_e.insert(0, "미상")

        global purchase_dir, origin_dir, current_dir, sn
        sn = material_txt.cget('text')
        current_dir = os.getcwd()
        purchase_dir = current_dir + f'\\document\\purchase\\{sn}'
        origin_dir = current_dir + f'\\document\\origin\\{sn}'

        # 자동계산입력 (단가 / 가격 )
        def toatl_cal(event):
            try:
                if exchangeRate_e.get() != "" and price_e.get() != "":
                    total_p = float(exchangeRate_e.get()) * float(price_e.get())
                    totalPrice_txt.configure(text=total_p)
                else:
                    totalPrice_txt.configure(text="")
            except:
                print('예외처리')

        price_e.bind("<KeyRelease>", toatl_cal)
        exchangeRate_e.bind("<KeyRelease>", toatl_cal)


        # 콤보박스 리스트 뿌려주기
        conn = sqlite3.connect('BOM.db')
        cur = conn.cursor()

        # 1)원자재
        list_table = cur.execute('''
               select name from sqlite_master where type='table' and name='material_info'
               ''').fetchall()
        if list_table == []:
            print('material_info 테이블이 없습니다.')
        else :
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

        # 2)구매정보
        list_table = cur.execute('''
                       select name from sqlite_master where type='table' and name='vendor'
                       ''').fetchall()
        if list_table == []:
            print('vendor 테이블이 없습니다.')
        else :
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

            vendorName_cmb.bind("<<ComboboxSelected>>", changeLabel_purchase)

        self.check_certificate()


    def check_certificate(self): # 입증서류 유무 체크
        if os.path.exists(purchase_dir+'\\') == True :
            docMaterial_txt.configure(text='있음', background='#6B66FF', fg='#FFFFFF')
        else :
            docMaterial_txt.configure(text='없음', background='#000000', fg='#FFFFFF')

        if os.path.exists(origin_dir) == True :
            docOrigin_txt.configure(text='있음', background='#6B66FF', fg='#FFFFFF')
        else :
            docOrigin_txt.configure(text='없음', background='#000000', fg='#FFFFFF')

    def regist(self):
        # create table
        conn = sqlite3.connect('./BOM.db')
        conn.execute('PRAGMA foreign_keys = ON')
        cur = conn.cursor()
        cur.execute(''' 
                     CREATE TABLE IF NOT EXISTS warehoused_list (
                        warehoused_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                        material_sn         TEXT    NOT NULL,
                        material_name       TEXT    NOT NULL,
                        namecode_kor        TEXT    NOT NULL,
                        namecode_eng        TEXT    NOT NULL,
                        material_kind       TEXT    NOT NULL,
                        hscode              TEXT    NOT NULL,
                        requried_amount     INT     NOT NULL,
                        unit                TEXT    NOT NULL,
                        ekw                 INT     NOT NULL,
                        manufacturer        TEXT    NOT NULL,
                        country_origin      TEXT    NOT NULL,
                        vendor_name         TEXT    NOT NULL,
                        buydate             TEXT    NOT NULL,
                        exchange_rate       FLOAT   NOT NULL,
                        price               INT     NOT NULL,
                        current             TEXT    NOT NULL,
                        total_price         FLOAT   NOT NULL,
                        document            TEXT    NOT NULL,
                        purchase_doc_valid  TEXT    NOT NULL,
                        origin_doc_valid    TEXT    NOT NULL,
                        vendor_id           INTEGER NOT NULL,
                        material_id         INTEGER NOT NULL
                        )
                     ''')



    #################### 파일첨부 화면 ##########################
    # 파일첨부 윈도우 오픈(구매증명서)
    def open_attachWin_purchase(self):
        self.open_attachWin()
        saveFile_win.title('구매입증서류 파일첨부')
        save_btn.configure(command=self.attach_purchaseFile)

    # 파일첨부 윈도우 오픈(원산지증명서)
    def open_attachWin_origin(self):
        self.open_attachWin()
        saveFile_win.title('원산지증빙서류 파일첨부')
        save_btn.configure(command=self.attach_originFile)

    def open_attachWin(self):
        global path_e, save_btn, saveFile_win, cancel_btn
        # Layout
        saveFile_win = Toplevel()
        saveFile_win.resizable(False, False)
        row1 = Label(saveFile_win, pady=7)
        row1.pack()
        Label(row1, text='File Name', font=("Georgia", 11)).pack(side='left', padx=3, pady=5)
        path_e = Entry(row1, width=40)
        path_e.pack(side='left', padx=3, pady=5, ipady=2)
        Button(row1, text='파일선택', font=("Georgia", 11), command=self.open_file).pack(side='left', padx=3, pady=5)
        row2 = Label(saveFile_win, pady=7)
        row2.pack()
        save_btn = Button(row2, text='파일 저장', font=("Georgia", 11))
        save_btn.pack(side='left', padx=5, pady=5)
        cancel_btn = Button(row2, text='취소', font=("Georgia", 11), command=self.cancel_attache_win)
        cancel_btn.pack(side='left', padx=5, pady=5)

    # 파일 불러오기
    def open_file(self):
        global file, filename
        file = filedialog.askopenfilename(title='파일을 선택하세요',
                                          filetypes=(("JPG 파일", "*.jpg"), ("PDF 파일", "*.pdf"),
                                                     ("All files", "*.*")))
        filename = file.split('/')[-1]
        if filename == "":
            return
        else:
            path_e.delete(0, END)
            path_e.insert(0, filename)

    # 파일첨부 버튼 실행(구매증명서)
    def attach_purchaseFile(self):
        folderName.clear()
        destination.clear()
        folderName.append('purchase')
        destination.append(purchase_dir + '\\' + filename)
        self.save_file()

    # 파일첨부 버튼 실행(원산지증명서)
    def attach_originFile(self):
        folderName.clear()
        destination.clear()
        folderName.append('origin')
        destination.append(origin_dir + '\\' + filename)
        self.save_file()

    def save_file(self):
        if os.path.exists(destination[0]) == True:
            response = msgbox.askyesno('예/아니오', '해당파일이 존재합니다.\n덮어쓰기를 실행할까요?')
            if response == 1:
                shutil.copyfile(file, destination[0])
                msgbox.showinfo('파일저장 완료!', '기존파일을 덮어쓰기하였습니다.')
                saveFile_win.destroy()
            else:
                print('덮어쓰기x, 복사x')
                pass
        elif os.path.exists(current_dir + f'\\document\\{folderName[0]}\\{sn}') == True :
            shutil.copyfile(file, destination[0])
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        elif os.path.exists(current_dir + f'\\document\\{folderName[0]}') == True :
            os.mkdir(current_dir + f'\\document\\{folderName[0]}\\{sn}')
            shutil.copyfile(file, destination[0])
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        elif os.path.exists(current_dir + '\\document') == True :
            os.mkdir(current_dir + f'\\document\\{folderName[0]}')
            os.mkdir(current_dir + f'\\document\\{folderName[0]}\\{sn}')
            shutil.copyfile(file, destination[0])
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        else :
            os.mkdir(current_dir + '\\document')
            os.mkdir(current_dir + f'\\document\\{folderName[0]}')
            os.mkdir(current_dir + f'\\document\\{folderName[0]}\\{sn}')
            shutil.copyfile(file, destination[0])
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()

        self.check_certificate()

    def cancel_attache_win(self):
        saveFile_win.destroy()