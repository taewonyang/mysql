from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog
import sqlite3
from tkcalendar import Calendar
from datetime import datetime
import os
import shutil

class Bom_register():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1500x750')
        self.window.resizable(False, False)
        self.layout()
        self.initialDB()

        # <달력 보기>
        datetime.today().strftime('%Y-%m-%d')
        def calView(self) : #캘린더 view
            global cal1, DateSel_btn, calForget_btn
            innerRight_frame.grid(row=0, column=1, padx=10)
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
            innerRight_frame.grid_forget()

        def forget_cal() : #달력 숨기기
            cal1.grid_forget()
            DateSel_btn.grid_forget()
            calForget_btn.grid_forget()
            innerRight_frame.grid_forget()

        bomDate_e.bind("<Button-1>", calView)


        # <완제품사진 첨부폴더 열기>
        def picture_open_folder(self):
            if productPic_txt.cget('text') == '없음':
                msgbox.showinfo('No file', '첨부된 완제품의 사진 파일이 없습니다.')
            else:
                msgbox.showinfo('첨부파일 열기', '완제품 사진 폴더를 오픈하였습니다. 첨부파일을 확인하세요.')
                # serial = productPic_txt.cget('text')
                # picture_dir = current_dir + f'\\document\\product_picture\\{product_sn}'
                path = os.path.realpath(picture_dir)
                os.startfile(path)

        productPic_txt.bind("<Double-Button-1>", picture_open_folder)


    def layout(self):
        global innerRight_frame, productSerial_txt, productPic_txt, addPic_btn
        global bomDate_e, bomCurrent_cmb, bomExRate_e, productSpec_e, productType_cmb, productPrice_e, material_cmb, materialBuyDate_cmb, shank_cmb, shankBuyDate_cmb, etc_cmb, etcBuyDate_cmb
        topFrame = Frame(self.window, width=1500, height=70, bg='#FDFFFF', bd=0.5)
        topFrame.place(x=0, y=0)
        leftFrame = Frame(self.window, width=605, height=680, relief='solid', bd=0.5)
        leftFrame.place(x=5, y=70)
        rightFrame = Frame(self.window, width=885, height=660, relief='solid', bd=0.5)
        rightFrame.place(x=610, y=70)

        # topFrame내용
        title1_lb = Label(topFrame, text='BOM 등록', font=("Georgia", 15), bg='#FDFFFF')
        title1_lb.place(x=30, y=20)
        title2_lb = Label(topFrame, text='BOM 조회', font=("Georgia", 15), bg='#FDFFFF')
        title2_lb.place(x=620, y=20)

        # leftFrame내용
        # -기본 정보(공통)-
        bomInfo_frame = LabelFrame(leftFrame, text='기본 정보(공통)', labelanchor=N)
        bomInfo_frame.grid(row=0,column=0)
        # bomInfo_frame.pack(fill='both', expand=True, padx=10, pady=10)
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
        bomToday_btn = Button(bomDate_lbframe, text=' T ', command=self.input_today)
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
        basicInfoClear_btn = Button(innerLeft_frame, text=' 기본 정보 \nClear', command=self.basicInfoClear)
        basicInfoClear_btn.grid(row=3, column=1, padx=7, pady=7)

        # -세부정보-
        detailInfo_frame = LabelFrame(leftFrame, text='세부 내용', labelanchor=N)
        # detailInfo_frame.pack(fill='both', expand=True, padx=10, pady=15)
        detailInfo_frame.grid(row=1, column=0)
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
        angle_btn = Button(specialtxt_lbframe, text='  ˚  ', command=self.input_angleTxt)
        angle_btn.grid(row=0, column=0, padx=0.5)
        micron_btn = Button(specialtxt_lbframe, text=' ㎛ ', command=self.input_micronTxt)
        micron_btn.grid(row=0, column=1, padx=0.5)
        x_btn = Button(specialtxt_lbframe, text=' × ', command=self.input_xTxt)
        x_btn.grid(row=0, column=2, padx=0.5)
        pie_btn = Button(specialtxt_lbframe, text=' Ø ', command=self.input_pieTxt)
        pie_btn.grid(row=0, column=3, padx=0.5)
        xcon_btn = Button(specialtxt_lbframe, text='×CON', command=self.input_xCONTxt)
        xcon_btn.grid(row=0, column=4, padx=0.5)
        xcyl_btn = Button(specialtxt_lbframe, text='×CYL', command=self.input_xCYLTxt)
        xcyl_btn.grid(row=0, column=5, padx=0.5)

        productType_lb = Label(producInfo_frame, text='완제품 품명')
        productType_lb.grid(row=2, column=0, padx=5, pady=3)
        productType_cmb = ttk.Combobox(producInfo_frame, height=3, width=10, values= ['SCD TOOL', 'PCD TOOL'], state='readonly')
        productType_cmb.grid(row=2, column=1, padx=5, pady=3, sticky=W)
        productPrice_lb = Label(producInfo_frame, text='완제품 가격')
        productPrice_lb.grid(row=3,column=0, padx=5, pady=3)
        productPrice_e = Entry(producInfo_frame, width =15)
        productPrice_e.grid(row=3, column=1, padx=5, pady=3, sticky=W)
        productPic_lb = Label(producInfo_frame, text='완제품 사진')
        productPic_lb.grid(row=4, column=0, padx=1, pady=5)
        productPic_txt = Label(producInfo_frame)
        productPic_txt.grid(row=4, column=1, padx=1, pady=5, sticky=W)
        addPic_btn = Button(producInfo_frame, text='사진 첨부', command=self.open_attachWin)
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

        empty_lb4 = Label(materialInfo_frame, text='     ')
        empty_lb4.grid(row=1, column=4)
        componenteInfoClear_btn = Button(materialInfo_frame, text=' 소재 정보 \nClear', command=self.componenteInfoClear)
        componenteInfoClear_btn.grid(row=1, column=5, padx=7, pady=7, rowspan=2)

        # 버튼frmae
        dataBtn_frame = Frame(leftFrame)
        dataBtn_frame.grid(row=3, column=0)
        # dataBtn_frame.pack(fill='both', expand=True, padx=10, pady=10)

        empty_lb1 = Label(dataBtn_frame, text='     ')
        empty_lb1.grid(row=0,column=0, padx=10, pady=3)
        empty_lb2 = Label(dataBtn_frame, text='     ')
        empty_lb2.grid(row=0, column=1, padx=10, pady=3)
        new_frame = LabelFrame(dataBtn_frame, text='신규등록')
        new_frame.grid(row=0, column=2, padx=10, pady=3)
        db_insert_btn = Button(new_frame, text='  Save  ')
        db_insert_btn.grid(row=0, column=0, padx=1, pady=3)

        existing_Frame = LabelFrame(dataBtn_frame, text='기존데이터')
        existing_Frame.grid(row=0, column=3, padx=10, pady=3)
        btn_dataload_btn = Button(existing_Frame, text=' Load ')
        btn_dataload_btn.grid(row=0, column=0, padx=1, pady=3)
        db_delete_btn = Button(existing_Frame, text='  Del  ', fg='#FF0000')
        db_delete_btn.grid(row=0, column=2, padx=9, pady=3)
        db_edit_btn = Button(existing_Frame, text=' Update ')
        db_edit_btn.grid(row=0, column=3, padx=1, pady=3)

        empty_lb3 = Label(dataBtn_frame, text='     ')
        empty_lb3.grid(row=0, column=4, padx=10, pady=3)
        allClear_btn = Button(dataBtn_frame, text=' ALL \n Clear ')
        allClear_btn.grid(row=0, column=5, padx=10, pady=3)

        # rightFrame 내용
        global tree_frame

        bomDate_lb2 = Label(rightFrame, text='날짜 선택')
        bomDate_lb2.place(x=10, y=20)
        bomDate_cmb = ttk.Combobox(rightFrame, height=7, width=13, state='readonly')
        bomDate_cmb.place(x=80, y=20)
        bomDateView_btn = Button(rightFrame, text='조회')
        bomDateView_btn.place(x=210, y=15)
        tree_frame = Frame(rightFrame)
        tree_frame.place(x=10, y=70, width=870, height=530)


    def initialDB(self):
        # <초기화>
        bomDate_e.delete(0,END)
        bomCurrent_cmb.set('')
        bomExRate_e.delete(0,END)
        productSpec_e.delete(0,END)
        productType_cmb.set('')
        productPrice_e.delete(0,END)
        material_cmb.set('')
        materialBuyDate_cmb.set('')
        shank_cmb.set('')
        shankBuyDate_cmb.set('')
        etc_cmb.set('')
        etcBuyDate_cmb.set('')
        innerRight_frame.grid_forget()
        innerRight_frame.grid(row=0, column=1, padx=10)


        conn = sqlite3.connect('BOM.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()

        # <세부내역-완제품 품번>
        list_table = cur.execute('''
                                select name from sqlite_master where type='table' and name='bom_list'
                                ''').fetchall()
        if list_table == []:
            print('bom_list 테이블이 없습니다.')
            productSerial_txt.configure(text=f'SJD-1-1')
        else :
            cur.execute('select * from bom_list')
            rs = cur.fetchall()
            if rs == []:
                productSerial_txt.configure(text=f'SJD-1-1')
            else:
                no = int(rs[-1][0]) + 1
                productSerial_txt.configure(text=f'SJD-1-{no}')

        # <기본정보-통화 cmb 리스트>
        list_table = cur.execute('''
                       select name from sqlite_master where type='table' and name='vendor'
                       ''').fetchall()
        if list_table == []:
            print('vendor 테이블이 없습니다.')
        else:
            current_db = cur.execute('select * from vendor').fetchall()
            current_opt = []
            for row in current_db :
                if row[2] not in current_opt :
                    current_opt.append(row[2])
            bomCurrent_cmb.configure(values=current_opt)

        # <소재정보-원석,원석구매일자 cmb 리스트>
        list_table = cur.execute('''
                        select name from sqlite_master where type='table' and name='warehoused_list'
                                                           ''').fetchall()
        if list_table == []:
            print('warehoused_list 테이블이 없습니다.')
        else:
            list_table = cur.execute('''
                            select name from sqlite_master where type='table' and name='material_info'
                                                                       ''').fetchall()
            if list_table == []:
                print('material_info 테이블이 없습니다.')
            else :
                material_db = cur.execute('select * from material_info').fetchall()
                material_opt = []
                shank_opt= []
                etc_opt = []
                materialBuyDate_opt = []
                shankBuyDate_opt = []
                etcBuyDate_opt = []

                for row in material_db:
                    # print(row) : (1, 'MXPL3010', 'SCD', '단결정 다이아몬드', '원석', '8512.22')
                    searched_id = int(row[0])

                    if row[4] == '원석' :
                        # 원석cmb opt
                        if row[1] not in material_opt :
                            material_opt.append(row[1])
                        # 원석구매일자cmb opt
                        warehousedFilter_db = cur.execute('select * from warehoused_list where material_id=?', (searched_id,)).fetchall()
                        if warehousedFilter_db != [] :
                            for i in warehousedFilter_db :
                                if i[7] not in materialBuyDate_opt :
                                    materialBuyDate_opt.append(i[7])
                    elif row[4] == "샹크" :
                        # 샹크cmb opt
                        if row[1] not in shank_opt :
                            shank_opt.append(row[1])
                        # 샹크구매일자cmb opt
                        warehousedFilter_db = cur.execute('select * from warehoused_list where material_id=?',
                                                          (searched_id,)).fetchall()
                        if warehousedFilter_db != []:
                            for i in warehousedFilter_db :
                                if i[7] not in shankBuyDate_opt:
                                    shankBuyDate_opt.append(i[7])
                    elif row[4] == "기타" :
                        # 기타cmb opt
                        if row[1] not in etc_opt :
                            etc_opt.append(row[1])
                        # 기타구매일자cmb opt
                        warehousedFilter_db = cur.execute('select * from warehoused_list where material_id=?',
                                                          (searched_id,)).fetchall()
                        if warehousedFilter_db != []:
                            for i in warehousedFilter_db :
                                if i[7] not in etcBuyDate_opt:
                                    etcBuyDate_opt.append(i[7])

                material_cmb.configure(values = material_opt)
                shank_cmb.configure(values=shank_opt)
                etc_cmb.configure(values=etc_opt)
                materialBuyDate_cmb.configure(values=materialBuyDate_opt)
                shankBuyDate_cmb.configure(values=shankBuyDate_opt)
                etcBuyDate_cmb.configure(values=etcBuyDate_opt)


        # <첨부파일 폴더경로>
        global picture_dir, current_dir, product_sn
        product_sn = productSerial_txt.cget('text')
        current_dir = os.getcwd()
        picture_dir = current_dir + f'\\document\\product_picture\\{product_sn}'

        # <완제품 사진 유무 체크>
        self.check_productPic()

    def check_productPic(self): # 완제품 사진 유무 체크
        if os.path.exists(picture_dir + '\\') == True:
            productPic_txt.configure(text='있음', background='#6B66FF', fg='#FFFFFF')
        else:
            productPic_txt.configure(text='없음', background='#000000', fg='#FFFFFF')

    ##################### 버튼 클릭 함수 #####################

    def input_today(self): # 오늘날짜 입력(T) 버튼
        today = datetime.today().strftime('%Y-%m-%d')
        bomDate_e.delete(0, END)
        bomDate_e.insert(0, today)
    def basicInfoClear(self): # 기본정보 Clear 버튼
        innerRight_frame.grid_forget()
        bomDate_e.delete(0, END)
        bomCurrent_cmb.set("")
        bomExRate_e.delete(0, END)
    def componenteInfoClear(self): # 소재정보 Clear 버튼
        material_cmb.set("")
        materialBuyDate_cmb.set("")
        shank_cmb.set("")
        shankBuyDate_cmb.set("")
        etc_cmb.set("")
        etcBuyDate_cmb.set("")

    def input_angleTxt(self):
        productSpec_e.insert(END, "˚")
    def input_micronTxt(self):
        productSpec_e.insert(END, "㎛")
    def input_xTxt(self):
        productSpec_e.insert(END, "×")
    def input_pieTxt(self):
        productSpec_e.insert(END, "Ø")
    def input_xCONTxt(self):
        productSpec_e.insert(END, "×CON")
    def input_xCYLTxt(self):
        productSpec_e.insert(END, "×CYL")

    ##################### 파일첨부 화면 #####################
    # 완제품사진 첨부 윈도우 오픈
    def open_attachWin(self):
        global path_e, save_btn, saveFile_win, cancel_btn
        # Layout
        saveFile_win = Toplevel()
        saveFile_win.title('완제품 사진 파일첨부')
        saveFile_win.resizable(False, False)
        row1 = Label(saveFile_win, pady=7)
        row1.pack()
        Label(row1, text='File Name', font=("Georgia", 11)).pack(side='left', padx=3, pady=5)
        path_e = Entry(row1, width=40)
        path_e.pack(side='left', padx=3, pady=5, ipady=2)
        Button(row1, text='파일선택', font=("Georgia", 11), command=self.open_file).pack(side='left', padx=3, pady=5)
        row2 = Label(saveFile_win, pady=7)
        row2.pack()
        save_btn = Button(row2, text='파일 저장', font=("Georgia", 11), command=self.save_file)
        save_btn.pack(side='left', padx=5, pady=5)
        cancel_btn = Button(row2, text='취소', font=("Georgia", 11), command=self.cancel_attache_win)
        cancel_btn.pack(side='left', padx=5, pady=5)

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

    def save_file(self):
        file_path = picture_dir + '\\' + filename
        print('file_path')
        print(file_path)
        print('==============')
        if os.path.exists(file_path) == True:
            print('중복값존재')
            response = msgbox.askyesno('예/아니오', '해당파일이 존재합니다.\n덮어쓰기를 실행할까요?')
            if response == 1:
                shutil.copyfile(file, file_path)
                msgbox.showinfo('파일저장 완료!', '기존파일을 덮어쓰기하였습니다.')
                saveFile_win.destroy()
            else:
                print('덮어쓰기x, 복사x')
                pass
        elif os.path.exists(picture_dir) == True:
            print('picture_dir\sn폴더 까지 존재')
            shutil.copyfile(file, file_path)
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        elif os.path.exists(current_dir + f'\\document\\product_picture') == True:
            print('picture_dir 폴더까지 존재')
            os.mkdir(picture_dir)
            shutil.copyfile(file, file_path)
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        elif os.path.exists(current_dir + '\\document') == True:
            print('document폴더까지만 존재')
            os.mkdir(current_dir + '\\document\\product_picture')
            os.mkdir(picture_dir)
            shutil.copyfile(file, file_path)
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        else:
            print('document폴더 없음->생성')
            os.mkdir(current_dir + '\\document')
            os.mkdir(current_dir + '\\document\\product_picture')
            os.mkdir(picture_dir)
            shutil.copyfile(file, file_path)
            msgbox.showinfo('파일저장 완료!', '파일첨부를 완료했습니다.')
            saveFile_win.destroy()
        self.check_productPic()

    def cancel_attache_win(self):
        saveFile_win.destroy()


    #####################  BOM 조회 트리뷰  ######################

    def create_tree_widget(self):
        columns = ('sn_col', 'name_col', 'namecode_eng_col', 'namecode_kor_col', 'material_kind_col', 'hscode_col',
                   'amount_col', 'ekw_col', 'manufacturer_col', 'country_origin_col', 'vendor_name_col', 'buydate_col',
                   'exchange_col', 'price_col', 'current_col', 'total_price_col', 'document_col',
                   'purchase_doc_valid_col',
                   'origin_doc_valid_col', 'btn_col')
