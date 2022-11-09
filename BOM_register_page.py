from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import sqlite3

class Bom_register():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1500x800')
        self.window.resizable(False, False)
