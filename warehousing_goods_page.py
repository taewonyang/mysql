from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog
from datetime import datetime
import os
import shutil
import sqlite3

class Warehousing_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1500x820')
        self.window.resizable(False, False)
        self.layout()
        self.create_tree_widget()
        self.initialDB()
        self.tree_data_view()

        global folderName, destination
        folderName = []
        destination = []

        # 증빙서류 폴더 열기
        def docMaterial_open_folder(self):
            if docMaterial_txt.cget('text') =='없음' :
                msgbox.showinfo('No file', '첨부된 구매입증서류 파일이 없습니다.')
            else:
                msgbox.showinfo('첨부파일 열기', '구매입증서류 폴더를 오픈하였습니다. 첨부파일을 확인하세요.')
                serial = sn_txt.cget('text')
                purchase_dir_path = current_dir + f'\\document\\purchase\\{serial}'
                path = os.path.realpath(purchase_dir_path)
                os.startfile(path)

        def docOrigin_open_folder(self):
            if docOrigin_txt.cget('text') =='없음' :
                msgbox.showinfo('No file', '첨부된 원산지증빙서류 파일이 없습니다.')
            else:
                msgbox.showinfo('첨부파일 열기', '원산지증빙서류 폴더를 오픈하였습니다. 첨부파일을 확인하세요.')
                serial = sn_txt.cget('text')
                origin_dir_path = current_dir + f'\\document\\origin\\{serial}'
                path = os.path.realpath(origin_dir_path)
                os.startfile(path)

        docMaterial_txt.bind("<Double-Button-1>", docMaterial_open_folder)
        docOrigin_txt.bind("<Double-Button-1>", docOrigin_open_folder)

    def resultData_export(self):
        global resultData
        resultData = []
        resultData.clear()

        conn = sqlite3.connect('./BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()
        list_table = cur.execute('''
                    select name from sqlite_master where type='table' and name='warehoused_list'
                    ''').fetchall()
        if list_table == []:
            print('warehoused_list 테이블이 없습니다.')
        else:
            cur.execute('select * from warehoused_list')
            rs = cur.fetchall()


    def layout(self):
        global sn_txt
        global material_cmb, namecode_kor_txt, namecode_eng_txt, kind_txt, hscode_txt, requriedAmount_e, unit_e, ekw_e, manufacturer_e, origin_e
        global vendorName_cmb, document_txt, current_txt, buydate_e, exchangeRate_e, price_e, current_txt, totalPrice_txt, docMaterial_txt, docOrigin_txt

        title = Label(self.window, text='원자재 입고리스트', font=("Georgia", 15))
        title.place(x=600, y=20)
        warehoused_sn_lb = Label(self.window, text='원자재 입고 품번:')
        warehoused_sn_lb.place(x=20, y=50)
        sn_txt = Label(self.window) #원자재 입고 품번
        sn_txt.place(x=120, y=50)

        # 원자재 frame
        material_fr = LabelFrame(self.window, text='Material Info')
        material_fr.place(x=20, y=80)
        material_name_lb = Label(material_fr, text='원자재 규격')
        material_name_lb.grid(row=0, column=0, padx=5, pady=3)
        namecode_eng_lb = Label(material_fr, text='원자재 품명(영문)')
        namecode_eng_lb.grid(row=0, column=1, padx=5, pady=3)
        namecode_kor_lb = Label(material_fr, text='원자재 품명(국문)')
        namecode_kor_lb.grid(row=0, column=2, padx=5, pady=3)
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

        material_cmb = ttk.Combobox(material_fr, height=5, width=15, state='readonly')
        material_cmb.grid(row=1, column=0, padx=5, pady=3)
        namecode_eng_txt = Label(material_fr, width=17)
        namecode_eng_txt.grid(row=1, column=1, padx=5, pady=3)
        namecode_kor_txt = Label(material_fr, width=15)
        namecode_kor_txt.grid(row=1, column=2, padx=5, pady=3)
        kind_txt = Label(material_fr, width=7)
        kind_txt.grid(row=1, column=3, padx=5, pady=3)
        hscode_txt = Label(material_fr, width=12)
        hscode_txt.grid(row=1, column=4, padx=5, pady=3)
        requriedAmount_e = Entry(material_fr, width=7, justify='center')
        requriedAmount_e.grid(row=1, column=5, padx=5, pady=3)
        unit_e = Entry(material_fr, width=5, justify='center')
        unit_e.grid(row=1, column=6, padx=5, pady=3)
        pack_lb = Label(material_fr)
        pack_lb.grid(row=1, column=7, padx=5, pady=3)
        ekw_e = Entry(pack_lb, width=9, justify='center')
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
        buydate_lb = Label(Purchase_fr, text='구매일자\n(ex) 2022-10-28)')
        buydate_lb.grid(row=0, column=1, padx=5, pady=3)
        exchangeRate_lb = Label(Purchase_fr, text='(구매일) 환율')
        exchangeRate_lb.grid(row=0, column=2, padx=5, pady=3)
        price_lb = Label(Purchase_fr, text='단가')
        price_lb.grid(row=0, column=3, padx=5, pady=3)
        current_lb = Label(Purchase_fr, text='통화')
        current_lb.grid(row=0, column=4, padx=5, pady=3)
        totalPrice_lb = Label(Purchase_fr, text='가격(KRW기준)')
        totalPrice_lb.grid(row=0, column=5, padx=5, pady=3)
        document_lb = Label(Purchase_fr, text='구매입증서류 종류')
        document_lb.grid(row=0, column=6, padx=5, pady=3)
        docMaterial_lb = Label(Purchase_fr, text='구매입증서류')
        docMaterial_lb.grid(row=0, column=7, padx=5, pady=3)
        docOrigin_lb = Label(Purchase_fr, text='원산지증빙서류')
        docOrigin_lb.grid(row=0, column=8, padx=5, pady=3)

        vendorName_cmb = ttk.Combobox(Purchase_fr, height=5, width=15, state='readonly')
        vendorName_cmb.grid(row=1, column=0, padx=5, pady=3)
        buydate_e = Entry(Purchase_fr, width=10)
        buydate_e.grid(row=1, column=1, padx=5, pady=3)
        exchangeRate_e = Entry(Purchase_fr, width=10, justify='center')
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
        btn_Frame = LabelFrame(self.window, text=' 입고내역 데이터 ')
        btn_Frame.place(x=1120, y=185)

        new_frame = LabelFrame(btn_Frame, text='신규등록')
        new_frame.grid(row=0, column=0, padx=10, pady=3)
        db_insert_btn = Button(new_frame, text='  Save  ', command=self.regist)
        db_insert_btn.grid(row=0, column=0, padx=1, pady=3)

        existing_Frame = LabelFrame(btn_Frame, text='기존데이터')
        existing_Frame.grid(row=0, column=1, padx=10, pady=3)
        btn_dataload_btn = Button(existing_Frame, text=' Load ', command=self.dataload)
        btn_dataload_btn.grid(row=0, column=0, padx=1, pady=3)
        cancel_btn = Button(existing_Frame, text='Cancel', command=self.cancel)
        cancel_btn.grid(row=0, column=1, padx=1, pady=3)
        db_delete_btn = Button(existing_Frame, text='  Del  ', fg='#FF0000', command=self.remove)
        db_delete_btn.grid(row=0, column=2, padx=9, pady=3)
        db_edit_btn = Button(existing_Frame, text=' Update ', command=self.edit)
        db_edit_btn.grid(row=0, column=3, padx=1, pady=3)

        # 조회cmb
        global search_cmb1, search_cmb2, search_cmb3, search_cmb4, search_cmb5, search_cmb6, search_cmb11, search_cmb12, search_cmb17, search_cmb18, search_cmb19

        searchFrame = Frame(self.window, width=1480)
        searchFrame.place(x=10, y=725)
        search_cmb1 = ttk.Combobox(searchFrame, height=5 ,width=5)
        search_cmb1.grid(row=0,column=1)
        search_cmb2 = ttk.Combobox(searchFrame, height=5, width=10)
        search_cmb2.grid(row=0, column=2)
        search_cmb3 = ttk.Combobox(searchFrame, height=5, width=7)
        search_cmb3.grid(row=0, column=3)
        search_cmb4 = ttk.Combobox(searchFrame, height=5, width=14)
        search_cmb4.grid(row=0, column=4)
        search_cmb5 = ttk.Combobox(searchFrame, height=5, width=7)
        search_cmb5.grid(row=0, column=5)
        search_cmb6 = ttk.Combobox(searchFrame, height=5, width=8)
        search_cmb6.grid(row=0, column=6)
        Label(searchFrame, text='       ', fg='#FFFFFF', width=29).grid(row=0, column=7)
        search_cmb11 = ttk.Combobox(searchFrame, height=5, width=13)
        search_cmb11.grid(row=0, column=10)
        search_cmb12 = ttk.Combobox(searchFrame, height=5, width=9)
        search_cmb12.grid(row=0, column=11)
        Label(searchFrame, text='       ', fg='#FFFFFF', width=32).grid(row=0, column=12)
        search_cmb17 = ttk.Combobox(searchFrame, height=5, width=11)
        search_cmb17.grid(row=0, column=13)
        search_cmb18 = ttk.Combobox(searchFrame, height=5, width=12)
        search_cmb18.grid(row=0, column=14)
        search_cmb19 = ttk.Combobox(searchFrame, height=5, width=12)
        search_cmb19.grid(row=0, column=15)

        searchBtn_frame = Frame(self.window)
        searchBtn_frame.place(x=1340, y=760)
        search_btn = Button(searchBtn_frame, text=' Search ', padx=5, pady=5, command=self.search)
        search_btn.grid(row=0, column=0)
        default_btn = Button(searchBtn_frame, text=' Default ', padx=5, pady=5, command=self.default)
        default_btn.grid(row=0, column=11)

    def initialDB(self):
        material_cmb.set('')
        namecode_eng_txt.configure(text='')
        namecode_kor_txt.configure(text='')
        kind_txt.configure(text='')
        hscode_txt.configure(text='')
        requriedAmount_e.delete(0,END)
        ekw_e.delete(0,END)
        vendorName_cmb.set('')
        buydate_e.delete(0,END)
        exchangeRate_e.delete(0,END)
        price_e.delete(0,END)
        current_txt.configure(text='')
        totalPrice_txt.configure(text='')
        document_txt.configure(text='')
        manufacturer_e.delete(0,END)
        unit_e.delete(0,END)
        origin_e.delete(0,END)

        # 기본설정
        manufacturer_e.insert(0, "미상")
        unit_e.insert(0, "EA")
        origin_e.insert(0, "미상")

        # 원자재품번(sn) 설정
        conn = sqlite3.connect('./BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()
        list_table = cur.execute('''
                        select name from sqlite_master where type='table' and name='warehoused_list'
                        ''').fetchall()
        if list_table == []:
            print('warehoused_list 테이블이 없습니다.')
            sn_txt.configure(text=f'SJD-1')
        else :
            cur.execute('select * from warehoused_list')
            rs = cur.fetchall()
            if rs == [] :
                sn_txt.configure(text=f'SJD-1')
            else :
                no = int(rs[-1][0]) + 1
                sn_txt.configure(text=f'SJD-{no}')

        global purchase_dir, origin_dir, current_dir, sn
        sn = sn_txt.cget('text')
        current_dir = os.getcwd()
        purchase_dir = current_dir + f'\\document\\purchase\\{sn}'
        origin_dir = current_dir + f'\\document\\origin\\{sn}'

        # 자동계산입력 (단가 / 가격 )
        def toatl_cal(event):
            try:
                if exchangeRate_e.get() != "" and price_e.get() != "":
                    total_p = round(float(exchangeRate_e.get()),2) * round(float(price_e.get()),2)
                    totalPrice_txt.configure(text=round(total_p,2))
                else:
                    totalPrice_txt.configure(text="")
            except:
                print('예외처리')

        price_e.bind("<KeyRelease>", toatl_cal)
        exchangeRate_e.bind("<KeyRelease>", toatl_cal)


        # 콤보박스 리스트 뿌려주기
        conn = sqlite3.connect('BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
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
                namecode_eng_txt.configure(text=rs[2])
                namecode_kor_txt.configure(text=rs[3])
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
                cur.execute('select * from vendor where vendor_name=?', (sel_name,))
                rs = cur.fetchall()[0]
                document_txt.configure(text=rs[3])
                current_txt.configure(text=rs[2])

            vendorName_cmb.bind("<<ComboboxSelected>>", changeLabel_purchase)

        self.check_certificate()

    def create_tree_widget(self):
        global tree
        tree_frame = Frame(self.window)
        tree_frame.place(x=10, y=280, width=1465, height=430)

        columns = ('sn_col','name_col', 'namecode_eng_col', 'namecode_kor_col', 'material_kind_col','hscode_col',
        'amount_col', 'ekw_col', 'manufacturer_col', 'country_origin_col', 'vendor_name_col', 'buydate_col',
        'exchange_col', 'price_col', 'current_col', 'total_price_col', 'document_col', 'purchase_doc_valid_col',
        'origin_doc_valid_col', 'btn_col')

        tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        tree.heading('sn_col', text='품번', anchor=CENTER)
        tree.heading('name_col', text='규격', anchor=CENTER)
        tree.heading('namecode_eng_col', text='품명(영문)', anchor=CENTER)
        tree.heading('namecode_kor_col', text='품명(국문)', anchor=CENTER)
        tree.heading('material_kind_col', text='원자재 종류', anchor=CENTER)
        tree.heading('hscode_col', text='세번', anchor=CENTER)
        tree.heading('amount_col', text='소요량', anchor=CENTER)
        tree.heading('ekw_col', text='구성비', anchor=CENTER)
        tree.heading('manufacturer_col', text='제조사', anchor=CENTER)
        tree.heading('country_origin_col', text='원산지', anchor=CENTER)
        tree.heading('vendor_name_col', text='구매처', anchor=CENTER)
        tree.heading('buydate_col', text='구매일자', anchor=CENTER)
        tree.heading('exchange_col', text='환율', anchor=CENTER)
        tree.heading('price_col', text='단가', anchor=CENTER)
        tree.heading('current_col', text='통화', anchor=CENTER)
        tree.heading('total_price_col', text='가격(KRW기준)', anchor=CENTER)
        tree.heading('document_col', text='구매입증서 종류', anchor=CENTER)
        tree.heading('purchase_doc_valid_col', text='구매입증서류 유무', anchor=CENTER)
        tree.heading('origin_doc_valid_col', text='원산지증빙서류 유무', anchor=CENTER)
        tree.heading('btn_col', text='    ', anchor=CENTER)

        tree.column('sn_col', width=60, anchor=CENTER)
        tree.column('name_col', width=90, anchor=CENTER)
        tree.column('namecode_eng_col', width=70, anchor=CENTER)
        tree.column('namecode_kor_col', width=115)
        tree.column('material_kind_col', width=80, anchor=CENTER)
        tree.column('hscode_col', width=70, anchor=CENTER)
        tree.column('amount_col', width=50, anchor=CENTER)
        tree.column('ekw_col', width=50, anchor=CENTER)
        tree.column('manufacturer_col', width=50, anchor=CENTER)
        tree.column('country_origin_col', width=50, anchor=CENTER)
        tree.column('vendor_name_col', width=120)
        tree.column('buydate_col', width=80, anchor=CENTER)
        tree.column('exchange_col', width=45, anchor=CENTER)
        tree.column('price_col', width=60, anchor=CENTER)
        tree.column('current_col', width=40, anchor=CENTER)
        tree.column('total_price_col', width=90, anchor=CENTER)
        tree.column('document_col', width=100, anchor=CENTER)
        tree.column('purchase_doc_valid_col', width=110, anchor=CENTER)
        tree.column('origin_doc_valid_col', width=120, anchor=CENTER)
        tree.column('btn_col', width=50, anchor=CENTER)

        tree.place(relheight=1, relwidth=1)
        scrollbar = Scrollbar(tree_frame, orient="vertical")
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

    def tree_data_view(self):
        conn = sqlite3.connect('./BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()
        list_table = cur.execute('''
                select name from sqlite_master where type='table' and name='warehoused_list'
                ''').fetchall()
        if list_table == []:
            print('warehoused_list 테이블이 없습니다.')
        else:
            global treeview_data
            treeview_data = []

            # 트리뷰 새로고침
            cur.execute('select * from warehoused_list')
            rs = cur.fetchall()
            for i in tree.get_children():
                tree.delete(i)
            for one in rs:
                one = list(one)
                del one[3] # 단위 EA 제거
                # vendor 테이블의 데이터 추출
                cur.execute('select * from vendor where vendor_id=?', (one[12],))
                searched_rs = cur.fetchall()
                # print(searched_rs)
                searched_vendor_name = searched_rs[0][1]
                searched_current = searched_rs[0][2]
                searched_document = searched_rs[0][3]

                # material 테이블의 데이터 추출
                cur.execute('select * from material_info where material_id=?', (one[13],))
                searched_rs = cur.fetchall()
                searched_material_name = searched_rs[0][1]
                searched_namecode_eng = searched_rs[0][2]
                searched_namecode_kor = searched_rs[0][3]
                searched_material_kind = searched_rs[0][4]
                searched_hscode = searched_rs[0][5]

                one.insert(2, searched_material_name)
                one.insert(3, searched_namecode_eng)
                one.insert(4, searched_namecode_kor)
                one.insert(5, searched_material_kind)
                one.insert(6, searched_hscode)
                one.insert(11, searched_vendor_name)
                one.insert(15, searched_current)
                one.insert(17, searched_document)
                del one[20:22]
                treeview_data.append(one)

            searchCmb1_opt = []
            searchCmb2_opt = []
            searchCmb3_opt = []
            searchCmb4_opt = []
            searchCmb5_opt = []
            searchCmb6_opt = []
            searchCmb11_opt = []
            searchCmb12_opt = []
            searchCmb17_opt = []
            searchCmb18_opt = []
            searchCmb19_opt = []

            for row in treeview_data:
                # treeview 새로고침
                tree.insert('', END, values=row[1:])

                # 검색cmb 새로고침
                if (row[1] in searchCmb1_opt) == False :
                    searchCmb1_opt.append(row[1])
                if (row[2] in searchCmb2_opt) == False :
                    searchCmb2_opt.append(row[2])
                if (row[3] in searchCmb3_opt) == False:
                    searchCmb3_opt.append(row[3])
                if (row[4] in searchCmb4_opt) == False:
                    searchCmb4_opt.append(row[4])
                if (row[5] in searchCmb5_opt) == False:
                    searchCmb5_opt.append(row[5])
                if (row[6] in searchCmb6_opt) == False:
                    searchCmb6_opt.append(row[6])
                if (row[11] in searchCmb11_opt) == False:
                    searchCmb11_opt.append(row[11])
                if (row[12] in searchCmb12_opt) == False:
                    searchCmb12_opt.append(row[12])
                if (row[17] in searchCmb17_opt) == False :
                    searchCmb17_opt.append(row[17])
                if (row[18] in searchCmb18_opt) == False :
                    searchCmb18_opt.append(row[18])
                if (row[19] in searchCmb19_opt) == False :
                    searchCmb19_opt.append(row[19])

                searchCmb1_opt.sort()
                searchCmb2_opt.sort()
                searchCmb3_opt.sort()
                searchCmb4_opt.sort()
                searchCmb5_opt.sort()
                searchCmb6_opt.sort()
                searchCmb11_opt.sort()
                searchCmb12_opt.sort()
                searchCmb17_opt.sort()
                searchCmb18_opt.sort()
                searchCmb19_opt.sort()
                search_cmb1.configure(values=searchCmb1_opt)
                search_cmb2.configure(values=searchCmb2_opt)
                search_cmb3.configure(values=searchCmb3_opt)
                search_cmb4.configure(values=searchCmb4_opt)
                search_cmb5.configure(values=searchCmb5_opt)
                search_cmb6.configure(values=searchCmb6_opt)
                search_cmb11.configure(values=searchCmb11_opt)
                search_cmb12.configure(values=searchCmb12_opt)
                search_cmb17.configure(values=searchCmb17_opt)
                search_cmb18.configure(values=searchCmb18_opt)
                search_cmb19.configure(values=searchCmb19_opt)

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
        if material_cmb.get() == "":
            msgbox.showerror("입력오류!", "원자재 규격을 입력해주세요")
        elif requriedAmount_e.get() == "" :
            msgbox.showerror("입력오류!", "소요량을 입력해주세요")
        elif unit_e.get() == "":
            msgbox.showerror("입력오류!", "단위를 입력해주세요")
        elif ekw_e.get() == "":
            msgbox.showerror("입력오류!", "구성비를 입력해주세요")
        elif manufacturer_e.get() == "":
            msgbox.showerror("입력오류!", "제조사를 입력해주세요")
        elif origin_e.get() == "":
            msgbox.showerror("입력오류!", "원산지를 입력해주세요")
        elif vendorName_cmb.get() == "":
            msgbox.showerror("입력오류!", "구매처를 선택해주세요")
        elif buydate_e.get() == "":
            msgbox.showerror("입력오류!", "구매날짜를 입력해주세요")
        elif exchangeRate_e.get() == "":
            msgbox.showerror("입력오류!", "환율을 입력해주세요")
        elif price_e.get() == "":
            msgbox.showerror("입력오류!", "단가를 입력해주세요")
        else:
            # create table
            conn = sqlite3.connect('./BOM.db')
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            cur.execute(''' 
                         CREATE TABLE IF NOT EXISTS warehoused_list (
                            warehoused_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                            warehoused_sn       TEXT    NOT NULL,
                            requried_amount     FLOAT   NOT NULL,
                            unit                TEXT    NOT NULL,
                            ekw                 FLOAT   NOT NULL,
                            manufacturer        TEXT    NOT NULL,
                            country_origin      TEXT    NOT NULL,
                            buydate             TEXT    NOT NULL,
                            exchange_rate       FLOAT   NOT NULL,
                            price               FLOAT   NOT NULL,
                            total_price         FLOAT   NOT NULL,
                            purchase_doc_valid  TEXT    NOT NULL,
                            origin_doc_valid    TEXT    NOT NULL,
                            vendor_id           INT     NOT NULL,
                            material_id         INT     NOT NULL,
                            FOREIGN KEY (vendor_id) REFERENCES vendor (vendor_id) ON UPDATE CASCADE,
                            FOREIGN KEY (material_id) REFERENCES material_info (material_id) ON UPDATE CASCADE
                            )
                         ''')

            conn.commit()
            conn.close()


            ### insert data into table ###
            conn = sqlite3.connect('./BOM.db')
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            # vendor_id 추출
            cur.execute('select vendor_id from vendor where vendor_name=:con1 and current=:con2 and document=:con3'
                        , {"con1":str(vendorName_cmb.get()), "con2":str(current_txt.cget('text')), "con3":str(document_txt.cget('text'))})
            searched_rs = cur.fetchall()
            searched_vendor_id = (searched_rs[0][0])
            # material_id 추출
            cur.execute('select material_id from material_info where material_name=:con1 and namecode_eng=:con2 and namecode_kor=:con3 and material_kind=:con4 and hscode=:con5'
                        ,{"con1":str(material_cmb.get()), "con2":str(namecode_eng_txt.cget('text')), "con3":str(namecode_kor_txt.cget('text')), "con4":str(kind_txt.cget('text')), "con5":str(hscode_txt.cget('text'))} )
            searched_rs = cur.fetchall()
            searched_material_id = (searched_rs[0][0])

            # 중복여부 체크
            cur.execute('select * from warehoused_list')
            rs = cur.fetchall()
            data = (round(float(requriedAmount_e.get()),1), str(unit_e.get()), round(float(ekw_e.get()),1), str(manufacturer_e.get()), str(origin_e.get()),
            datetime.strptime(buydate_e.get(), '%Y-%m-%d').date(), round(float(exchangeRate_e.get()),2), round(float(price_e.get()),2), round(float(totalPrice_txt.cget('text')),2)
            )
            overlap_check = []
            if rs != []:  # DB에 데이터가 있다면
                for row in rs:
                    print('row')
                    print(row)
                    if row[2:11] == tuple(data):
                        overlap_check.append('ok')
                        break
            # (데이터O / 중복O)
            if overlap_check != []:
                msgbox.showerror('중복오류!', '이미 존재하는 데이터입니다.\n다시 입력해주세요.')
            # (데이터O / 중복X) or (데이터X)
            else:
                data = list(data)
                data.insert(0, sn)
                for i in [docMaterial_txt.cget('text'), docOrigin_txt.cget('text'), int(searched_vendor_id), int(searched_material_id)] :
                    data.append(i)
                data = tuple(data)
                insert_sql = 'INSERT INTO warehoused_list values(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                cur.execute(insert_sql, data)
                msgbox.showinfo('등록완료!', '원자재 정보를 등록하였습니다.')
                conn.commit()
                conn.close()

                self.tree_data_view()
                self.initialDB()

    def cancel(self):
        self.initialDB()

    def remove(self):
        conn = sqlite3.connect('./BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()
        list_table = cur.execute('''
                        select name from sqlite_master where type='table' and name='warehoused_list'
                        ''').fetchall()
        if list_table == []:
            msgbox.showerror('선택 오류', '삭제할 데이터를 표에서 선택해주세요.')
        else:
            selectedItem = tree.focus()
            getValue = tree.item(selectedItem).get('values')
            if selectedItem == "":
                msgbox.showerror('선택 오류', '삭제할 데이터를 표에서 선택해주세요.')
            else:
                response = msgbox.askyesno('예/아니오', '해당 데이터를 삭제합니까?')
                if response == 1:
                    print()
                    cur.execute('delete from warehoused_list where warehoused_sn = ?', (getValue[0],))
                    conn.commit()
                    conn.close()
                    msgbox.showinfo('삭제완료!', '삭제를 완료했습니다.')

                    self.tree_data_view()
                    self.cancel()
                elif response == 0:
                    return

    def dataload(self):
        selectedItem = tree.focus()
        getValue = tree.item(selectedItem).get('values')
        if selectedItem == "":
            msgbox.showerror('선택 오류', '불러올 데이터를 표에서 선택해주세요.')
        else:
            print(getValue)
            self.cancel()
            sn_txt.configure(text=getValue[0])
            material_cmb.set(getValue[1])
            namecode_eng_txt.configure(text=getValue[2])
            namecode_kor_txt.configure(text=getValue[3])
            kind_txt.configure(text=getValue[4])
            hscode_txt.configure(text=getValue[5])
            requriedAmount_e.insert(0, getValue[6])
            ekw_e.insert(0, getValue[7])
            manufacturer_e.delete(0, END)
            manufacturer_e.insert(0, getValue[8])
            origin_e.delete(0, END)
            origin_e.insert(0, getValue[9])

            vendorName_cmb.set(getValue[10])
            buydate_e.insert(0, getValue[11])
            exchangeRate_e.insert(0, getValue[12])
            price_e.insert(0, getValue[13])
            current_txt.configure(text=getValue[14])
            totalPrice_txt.configure(text=getValue[15])
            document_txt.configure(text=getValue[16])
            if getValue[17] == '있음':
                docMaterial_txt.configure(text='있음', background='#6B66FF', fg='#FFFFFF')
            else:
                docMaterial_txt.configure(text='없음', background='#000000', fg='#FFFFFF')
            if getValue[18] == '있음':
                docOrigin_txt.configure(text='있음', background='#6B66FF', fg='#FFFFFF')
            else:
                docOrigin_txt.configure(text='없음', background='#000000', fg='#FFFFFF')

    def edit(self):
        selectedItem = tree.focus()
        getValue = tree.item(selectedItem).get('values')
        if selectedItem == "" :
            msgbox.showerror('선택 오류', '수정할 데이터를 표에서 선택해주세요.')
        else :
            if material_cmb.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 원자재 규격을 입력해주세요")
            elif requriedAmount_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 소요량을 입력해주세요")
            elif unit_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 단위를 입력해주세요")
            elif ekw_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 구성비를 입력해주세요")
            elif manufacturer_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 제조사를 입력해주세요")
            elif origin_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 원산지를 입력해주세요")
            elif vendorName_cmb.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 구매처를 선택해주세요")
            elif buydate_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 구매날짜를 입력해주세요")
            elif exchangeRate_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 환율을 입력해주세요")
            elif price_e.get() == "":
                msgbox.showerror("입력오류!", "수정되는 내용의 단가를 입력해주세요")
            else:
                response = msgbox.askyesno('예/아니오', '입력된 내용으로 수정하시겠습니까?')
                if response == 1:
                    conn = sqlite3.connect('./BOM.db')
                    conn.execute("PRAGMA foreign_keys = 1")
                    cur = conn.cursor()
                    # vendor_id 추출
                    cur.execute(
                        'select vendor_id from vendor where vendor_name=:con1 and current=:con2 and document=:con3'
                        , {"con1": str(getValue[10]), "con2": str(getValue[14]), "con3": str(getValue[16])})
                    searched_rs = cur.fetchall()
                    searched_vendor_id = (searched_rs[0][0])
                    # material_id 추출
                    cur.execute(
                        'select material_id from material_info where material_name=:con1 and namecode_kor=:con2 and namecode_eng=:con3 and material_kind=:con4 and hscode=:con5'
                        , {"con1": str(getValue[1]), "con2": str(getValue[3]), "con3": str(getValue[2]), "con4": str(getValue[4]),
                           "con5": str(getValue[5])})
                    searched_rs = cur.fetchall()
                    searched_material_id = (searched_rs[0][0])

                    update_query = '''
                    update warehoused_list set requried_amount=?, unit=?, ekw=?, manufacturer=?, country_origin=?, buydate=?, exchange_rate=?,
                                            price=?, total_price=?, purchase_doc_valid=?, origin_doc_valid=?, vendor_id=?, material_id=?
                                where warehoused_sn = ?
                    '''
                    query_data = (
                    round(float(requriedAmount_e.get()),1), str(unit_e.get()), round(float(ekw_e.get()),1), str(manufacturer_e.get()), str(origin_e.get()),
                    datetime.strptime(buydate_e.get(), '%Y-%m-%d').date(), round(float(exchangeRate_e.get()),2), round(float(price_e.get()),2), round(float(totalPrice_txt.cget('text')),2)
                    )
                    query_data = list(query_data)
                    for i in [docMaterial_txt.cget('text'), docOrigin_txt.cget('text'), int(searched_vendor_id),
                              int(searched_material_id), getValue[0]]:
                        query_data.append(i)
                    query_data = tuple(query_data)
                    print(query_data)
                    cur.execute(update_query, query_data)
                    msgbox.showinfo('수정완료!', '데이터가 수정되었습니다.')
                    conn.commit()
                    conn.close()

                    self.tree_data_view()
                else :
                    return

    def search(self):
        for i in tree.get_children():
            tree.delete(i)

        conn = sqlite3.connect('./BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()
        check_list = [search_cmb1.get(), search_cmb2.get(), search_cmb3.get(), search_cmb4.get(), search_cmb5.get(), search_cmb6.get(), search_cmb11.get(), search_cmb12.get(), search_cmb17.get(), search_cmb18.get(), search_cmb19.get()]
        searchInfo = []  # (검색순번, 입력값)
        for i in enumerate(check_list):
            if i[1] != "":
                searchInfo.append(i)
        # print('검색하려는값 (검색순번,입력값)')
        # print(searchInfo)

        if len(searchInfo) == 0 :
            self.tree_data_view()
            # print('검색요청값 없음')
        else :
            cur.execute('''SELECT warehoused_list.warehoused_sn, material_info.material_name, material_info.namecode_eng, material_info.namecode_kor,
                                material_info.material_kind, material_info.hscode, vendor.vendor_name, warehoused_list.buydate, vendor.document,
                                warehoused_list.purchase_doc_valid, warehoused_list.origin_doc_valid     
                            FROM warehoused_list 
                            JOIN material_info ON warehoused_list.material_id = material_info.material_id
                            JOIN vendor ON warehoused_list.vendor_id = vendor.vendor_id ''')

            searched_data = []

            # 트리뷰 view
            for check_row in cur.fetchall() :
                # print('===========')
                # print(check_row)
                result = []
                for i in searchInfo :
                    if check_row[i[0]] == i[1] :
                        result.append('일치')
                    else :
                        result.append('불일치')
                # print('result')
                # print(result)
                if list(set(result))[0] == '일치' and len(set(result)) == 1 :
                    # 트리뷰에 데이터 view
                    # print(check_row[0])
                    cur.execute('select * from warehoused_list where warehoused_sn = ?', (check_row[0],))
                    rs = cur.fetchall()


                    for one in rs:
                        one = list(one)
                        del one[3]  # 단위 EA 제거
                        # vendor 테이블의 데이터 추출
                        cur.execute('select * from vendor where vendor_id=?', (one[12],))
                        searched_rs = cur.fetchall()
                        # print(searched_rs)
                        searched_vendor_name = searched_rs[0][1]
                        searched_current = searched_rs[0][2]
                        searched_document = searched_rs[0][3]

                        # material 테이블의 데이터 추출
                        cur.execute('select * from material_info where material_id=?', (one[13],))
                        searched_rs = cur.fetchall()
                        searched_material_name = searched_rs[0][1]
                        searched_namecode_eng = searched_rs[0][2]
                        searched_namecode_kor = searched_rs[0][3]
                        searched_material_kind = searched_rs[0][4]
                        searched_hscode = searched_rs[0][5]

                        one.insert(2, searched_material_name)
                        one.insert(3, searched_namecode_eng)
                        one.insert(4, searched_namecode_kor)
                        one.insert(5, searched_material_kind)
                        one.insert(6, searched_hscode)
                        one.insert(11, searched_vendor_name)
                        one.insert(15, searched_current)
                        one.insert(17, searched_document)
                        del one[20:22]
                        searched_data.append(one)

            for row in searched_data:
                # treeview 새로고침
                tree.insert('', END, values=row[1:])

    def default(self):
        search_cmb1.set("")
        search_cmb2.set("")
        search_cmb3.set("")
        search_cmb4.set("")
        search_cmb5.set("")
        search_cmb6.set("")
        search_cmb11.set("")
        search_cmb12.set("")
        search_cmb17.set("")
        search_cmb18.set("")
        search_cmb19.set("")

        self.tree_data_view()

    ################################ 파일첨부 화면 ######################################
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