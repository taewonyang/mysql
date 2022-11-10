from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3

class Bom_register():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1500x700')
        self.window.resizable(False, False)
        self.layout()

    def layout(self):
        topFrame = Frame(self.window, width=1500, height=70, bg='#FDFFFF')
        topFrame.place(x=0, y=0)
        leftFrame = Frame(self.window, width=600, height=630, relief='solid', bd=0.5)
        leftFrame.place(x=0, y=70)
        rightFrame = Frame(self.window, width=900, height=630)
        rightFrame.place(x=600, y=70)

        # topFrame내용
        title = Label(topFrame, text='BOM 등록', font=("Georgia", 15), bg='#FDFFFF')
        title.place(x=30, y=20)

        # leftFrame내용
        bomInfo_frame = LabelFrame(leftFrame, text='기본 정보')
        bomInfo_frame.place(x=20, y=20)
        bomDate_lb = Label(bomInfo_frame, text='입력 날짜          \n(ex:2022-11-10)')
        bomDate_lb.grid(row=0, column=0, padx=5, pady=3, sticky=W)
        bomDate_lbframe = Label(bomInfo_frame)
        bomDate_lbframe.grid(row=0, column=1, padx=5, pady=3, sticky=W)
        bomDate_e = Entry(bomDate_lbframe, width=10)
        bomDate_e.grid(row=0, column=0,padx=1)
        bomToday_btn = Button(bomDate_lbframe, text=' T ')
        bomToday_btn.grid(row=0, column=1, padx=1)
        bomCurrent_lb = Label(bomInfo_frame, text='통화')
        bomCurrent_lb.grid(row=1, column=0, padx=5, pady=3, sticky=W)
        bomCurrent_cmb = ttk.Combobox(bomInfo_frame, height=5, width=8, state='readonly')
        bomCurrent_cmb.grid(row=1, column=1, padx=5, pady=3, sticky=W)
        bomExRate_lb = Label(bomInfo_frame, text='환율')
        bomExRate_lb.grid(row=1, column=2, padx=5, pady=3, sticky=W)
        bomExRate_e = Entry(bomInfo_frame, width=10)
        bomExRate_e.grid(row=1, column=3, padx=5, pady=3, sticky=W)

        #제품정보
        producInfo_frame = LabelFrame(leftFrame, text='제품 정보')
        producInfo_frame.place(x=20, y=130)
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

        #소재정보
        materialInfo_frame = LabelFrame(leftFrame, text='소재 정보')
        materialInfo_frame.place(x=20, y=280)
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
        dataBtn_frame = LabelFrame(leftFrame, text='BOM 데이터')
        dataBtn_frame.place(x=20, y=450)
