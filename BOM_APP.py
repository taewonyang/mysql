from tkinter import *
import vendor_register_page, material_stocked_page, material_info_page


class App() :
    def __init__(self, root):
        self.window = root
        self.window.resizable(False, False)

        menu_frame = LabelFrame(self.window, text='Menu')
        menu_frame.pack(padx=7,pady=4)
        vendor_register_btn = Button(menu_frame, text='구매처 등록/조회', command=self.go_vendor_register)
        vendor_register_btn.pack(side='left', padx=5, pady=5, ipady=3, ipadx=3)
        material_list_btn = Button(menu_frame, text='원자재 입고 리스트 ', command=self.go_material_stocked)
        material_list_btn.pack(side='left', padx=5, pady=5, ipady=3, ipadx=3)
        material_info_btn = Button(menu_frame, text='원자재 정보 ' , command=self.go_material_info)
        material_info_btn.pack(side='left', padx=5, pady=5, ipady=3, ipadx=3)

    def go_vendor_register(self):
        win = Toplevel()
        vendor_register_page.Register_window(win)

    def go_material_stocked(self):
        win = Toplevel()
        material_stocked_page.StockedList_window(win)

    def go_material_info(self):
        win=Toplevel()
        material_info_page.Material_Info(win)



def startApp() :
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__' :
    startApp()