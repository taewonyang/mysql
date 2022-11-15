from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3
from tkcalendar import Calendar
from datetime import datetime

class Bom_register():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1500x750')
        self.window.resizable(False, False)
        self.layout()
        self.initialDB()

        datetime.today().strftime('%Y-%m-%d')

        def calView(self) : #캘린더 view
            global cal1, DateSel_btn, calForget_btn
            cal1 = Calendar(innerRight_frame, selectmode='day')
            cal1.grid(row=0, column=0, padx=3, pady=5)

            DateSelBtn_lbframe = Label(innerRight_frame)
            DateSelBtn_lbframe.grid(row=0, column=1, padx=3)
            DateSel_btn = Button(DateSelBtn_lbframe, text=' 날짜 \n 입력 ', command=input_seldate)
            DateSel_btn.grid(row=0, column=0, padx=3, pady=10)
            calForget_btn = Button(DateSelBtn_lbframe, text=' 달력 \n 닫기 ', command=forget_cal)
            calForget_btn.grid(row=1,column=0, padx=3, pady=10)

        def input_seldate(): # 선택 날짜 입력
            sel_date = datetime.strptime(cal1.get_date(), '%m/%d/%y').date()
            bomDate_e.delete(0, END)
            bomDate_e.insert(0, sel_date)
            cal1.grid_forget()
            DateSel_btn.grid_forget()
            calForget_btn.grid_forget()

        def forget_cal() : #달력 숨기기
            cal1.grid_forget()
            DateSel_btn.grid_forget()
            calForget_btn.grid_forget()

        bomDate_e.bind("<Button-1>", calView)

    def layout(self):
        global bomDate_e, innerRight_frame, bomCurrent_cmb

        topFrame = Frame(self.window, width=1500, height=70, bg='#FDFFFF', bd=0.5)
        topFrame.place(x=0, y=0)
        leftFrame = Frame(self.window, width=605, height=680, relief='solid', bd=0.5)
        leftFrame.place(x=5, y=70)
        rightFrame = Frame(self.window, width=885, height=675, relief='solid', bd=0.5)
        rightFrame.place(x=610, y=70)

        # topFrame내용
        title1_lb = Label(topFrame, text='BOM 등록', font=("Georgia", 15), bg='#FDFFFF')
        title1_lb.place(x=30, y=20)
        title2_lb = Label(topFrame, text='BOM 조회', font=("Georgia", 15), bg='#FDFFFF')
        title2_lb.place(x=620, y=20)

        # leftFrame내용
        # -기본 정보(공통)-
        bomInfo_frame = LabelFrame(leftFrame, text='기본 정보(공통)', labelanchor=N)
        bomInfo_frame.pack(fill='both', expand=True, padx=10, pady=10)
        innerLeft_frame = Frame(bomInfo_frame)
        innerLeft_frame.grid(row=0, column=0, padx=10)
        innerRight_frame = Frame(bomInfo_frame, height=176)
        innerRight_frame.grid(row=0, column=1, padx=10)

        bomDate_lb = Label(innerLeft_frame, text='날짜               \n(ex:2022-11-10)')
        bomDate_lb.grid(row=0, column=0, padx=5, pady=3, sticky=W)
        bomDate_lbframe = Label(innerLeft_frame)
        bomDate_lbframe.grid(row=0, column=1, padx=5, pady=3, sticky=W)
        bomDate_e = Entry(bomDate_lbframe, width=10)
        bomDate_e.grid(row=0, column=0,padx=1)
        bomToday_btn = Button(bomDate_lbframe, text=' T ')
        bomToday_btn.grid(row=0, column=1, padx=1)
        bomCurrent_lb = Label(innerLeft_frame, text='통화')
        bomCurrent_lb.grid(row=1, column=0, padx=5, pady=3, sticky=W)
        bomCurrent_cmb = ttk.Combobox(innerLeft_frame, height=5, width=8, state='readonly')
        bomCurrent_cmb.grid(row=1, column=1, padx=5, pady=3, sticky=W)
        bomExRate_lb = Label(innerLeft_frame, text='환율')
        bomExRate_lb.grid(row=2, column=0, padx=5, pady=3, sticky=W)
        bomExRate_e = Entry(innerLeft_frame, width=10)
        bomExRate_e.grid(row=2, column=1, padx=5, pady=3, sticky=W)
        CheckVar1 = IntVar()
        keep_chkbtn = Checkbutton(innerLeft_frame, text="기본 정보(공통)\n입력내용 유지", variable=CheckVar1)
        keep_chkbtn.grid(row=3, column=0, padx=7, pady=7)
        clear_btn = Button(innerLeft_frame, text=' 기본 정보 \nClear')
        clear_btn.grid(row=3, column=1, padx=7, pady=7)


        # -세부정보-
        detailInfo_frame = LabelFrame(leftFrame, text='세부 내용', labelanchor=N)
        detailInfo_frame.pack(fill='both', expand=True, padx=10, pady=15)
        #제품정보
        producInfo_frame = LabelFrame(detailInfo_frame, text='제품 정보')
        producInfo_frame.grid(row=0, column=0, padx=5, pady=10)
        productSerial_lb = Label(producInfo_frame, text='완제품 품번')
        productSerial_lb.grid(row=0, column=0, padx=5, pady=3)
        productSerial_txt = Label(producInfo_frame, width=8)
        productSerial_txt.grid(row=0, column=1, padx=5, pady=3, sticky=W)
        productSpec_lb = Label(producInfo_frame, text='완제품 규격')
        productSpec_lb.grid(row=1, column=0, padx=5, pady=3)
        productSpec_e = Entry(producInfo_frame, width=32)
        productSpec_e.grid(row=1, column=1, padx=5, pady=3)

        specialtxt_lbframe = LabelFrame(producInfo_frame,text='')
        specialtxt_lbframe.grid(row=1, column=2, padx=8)
        angle_btn = Button(specialtxt_lbframe, text='  ˚  ')
        angle_btn.grid(row=0, column=0, padx=0.5)
        micron_btn = Button(specialtxt_lbframe, text=' ㎛ ')
        micron_btn.grid(row=0, column=1, padx=0.5)
        x_btn = Button(specialtxt_lbframe, text=' × ')
        x_btn.grid(row=0, column=2, padx=0.5)
        pie_btn = Button(specialtxt_lbframe, text=' Ø ')
        pie_btn.grid(row=0, column=3, padx=0.5)
        xcon_btn = Button(specialtxt_lbframe, text='×CON')
        xcon_btn.grid(row=0, column=4, padx=0.5)
        xcyl_btn = Button(specialtxt_lbframe, text='×CYL')
        xcyl_btn.grid(row=0, column=5, padx=0.5)

        productType_lb = Label(producInfo_frame, text='완제품 품명')
        productType_lb.grid(row=2, column=0, padx=5, pady=3)
        productType_cmb = ttk.Combobox(producInfo_frame, height=3, width=10, state='readonly')
        productType_cmb.grid(row=2, column=1, padx=5, pady=3, sticky=W)
        productPrice_lb = Label(producInfo_frame, text='완제품 가격')
        productPrice_lb.grid(row=3,column=0, padx=5, pady=3)
        productPrice_e = Entry(producInfo_frame, width =15)
        productPrice_e.grid(row=3, column=1, padx=5, pady=3, sticky=W)
        productPic_lb = Label(producInfo_frame, text='완제품 사진')
        productPic_lb.grid(row=4, column=0, padx=1, pady=5)
        productPic_txt = Label(producInfo_frame, text='없음')
        productPic_txt.grid(row=4, column=1, padx=1, pady=5, sticky=W)
        addPic_btn = Button(producInfo_frame, text='사진 첨부')
        addPic_btn.grid(row=4, column=1, padx=2, pady=5)

        #소재정보
        materialInfo_frame = LabelFrame(detailInfo_frame, text='소재 정보')
        materialInfo_frame.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        material_lb = Label(materialInfo_frame, text='원석')
        material_lb.grid(row=0, column=0, padx=5, pady=3)
        material_cmb = ttk.Combobox(materialInfo_frame, height=5, width=15, state='readonly')
        material_cmb.grid(row=0, column=1, padx=5, pady=3)
        materialBuyDate_lb = Label(materialInfo_frame, text='원석 구매일자')
        materialBuyDate_lb.grid(row=0, column=2, padx=5, pady=3)
        materialBuyDate_cmb = ttk.Combobox(materialInfo_frame, height=5, width=12, state='readonly')
        materialBuyDate_cmb.grid(row=0, column=3, padx=5, pady=3)
        shank_lb = Label(materialInfo_frame, text='샹크')
        shank_lb.grid(row=1, column=0, padx=5, pady=3)
        shank_cmb = ttk.Combobox(materialInfo_frame, height=5, width=15, state='readonly')
        shank_cmb.grid(row=1, column=1, padx=5, pady=3)
        shankBuyDate_lb = Label(materialInfo_frame, text='샹크 구매일자')
        shankBuyDate_lb.grid(row=1, column=2, padx=5, pady=3)
        shankBuyDate_cmb = ttk.Combobox(materialInfo_frame, height=5, width=12, state='readonly')
        shankBuyDate_cmb.grid(row=1, column=3, padx=5, pady=3)

        etc_lb = Label(materialInfo_frame, text='etc')
        etc_lb.grid(row=2, column=0, padx=5, pady=3)
        etc_cmb = ttk.Combobox(materialInfo_frame, height=5, width=15, state='readonly')
        etc_cmb.grid(row=2, column=1, padx=5, pady=3)
        etcBuyDate_lb = Label(materialInfo_frame, text='etc 구매일자')
        etcBuyDate_lb.grid(row=2, column=2, padx=5, pady=3)
        etcBuyDate_cmb = ttk.Combobox(materialInfo_frame, height=5, width=12, state='readonly')
        etcBuyDate_cmb.grid(row=2, column=3, padx=5, pady=3)

        # 버튼frmae
        dataBtn_frame = Frame(leftFrame)
        dataBtn_frame.pack( fill='both', expand=True, padx=10, pady=10)

        empty_lb1 = Label(dataBtn_frame, text='     ')
        empty_lb1.grid(row=0,column=0, padx=10, pady=3)
        empty_lb2 = Label(dataBtn_frame, text='     ')
        empty_lb2.grid(row=0, column=1, padx=10, pady=3)
        empty_lb3 = Label(dataBtn_frame, text='     ')
        empty_lb3.grid(row=0, column=2, padx=10, pady=3)
        new_frame = LabelFrame(dataBtn_frame, text='신규등록')
        new_frame.grid(row=0, column=3, padx=10, pady=3)
        db_insert_btn = Button(new_frame, text='  Save  ')
        db_insert_btn.grid(row=0, column=0, padx=1, pady=3)

        existing_Frame = LabelFrame(dataBtn_frame, text='기존데이터')
        existing_Frame.grid(row=0, column=4, padx=10, pady=3)
        btn_dataload_btn = Button(existing_Frame, text=' Load ')
        btn_dataload_btn.grid(row=0, column=0, padx=1, pady=3)
        cancel_btn = Button(existing_Frame, text='Cancel')
        cancel_btn.grid(row=0, column=1, padx=1, pady=3)
        db_delete_btn = Button(existing_Frame, text='  Del  ', fg='#FF0000')
        db_delete_btn.grid(row=0, column=2, padx=9, pady=3)
        db_edit_btn = Button(existing_Frame, text=' Update ')
        db_edit_btn.grid(row=0, column=3, padx=1, pady=3)

        # rightFrame 내용
        global tree_frame

        bomDate_lb2 = Label(rightFrame, text='날짜 선택')
        bomDate_lb2.place(x=10, y=20)
        bomDate_cmb = ttk.Combobox(rightFrame, height=7, width=13, state='readonly')
        bomDate_cmb.place(x=80, y=20)
        bomDateView_btn = Button(rightFrame, text='조회')
        bomDateView_btn.place(x=210, y=15)
        tree_frame = Frame(rightFrame, bg='blue')
        tree_frame.place(x=10, y=70, width=870, height=530)

    def initialDB(self):
        conn = sqlite3.connect('BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()

        # <기본정보-통화 데이터 뿌려주기>
        list_table = cur.execute('''
                       select name from sqlite_master where type='table' and name='vendor'
                       ''').fetchall()
        if list_table == []:
            print('material_info 테이블이 없습니다.')
        else:
            current_db = cur.execute('select * from vendor').fetchall()
            current_opt = []
            for row in current_db :
                if row in current_opt :
                current_opt.append(row[2])
            bomCurrent_cmb.configure(values=current_opt)


    def create_tree_widget(self):
        columns = ('sn_col', 'name_col', 'namecode_eng_col', 'namecode_kor_col', 'material_kind_col', 'hscode_col',
                   'amount_col', 'ekw_col', 'manufacturer_col', 'country_origin_col', 'vendor_name_col', 'buydate_col',
                   'exchange_col', 'price_col', 'current_col', 'total_price_col', 'document_col',
                   'purchase_doc_valid_col',
                   'origin_doc_valid_col', 'btn_col')