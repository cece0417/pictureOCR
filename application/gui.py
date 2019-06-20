#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import tkinter
from tkinter.filedialog import askopenfilename
from PIL import Image
from pytesseract import pytesseract

CUR_DIR   = os.path.dirname(os.path.abspath(__file__))
LANG_DIR  = CUR_DIR + '/' + 'lang'
BIN_DIR   = CUR_DIR + '/' + 'bin'
MAC_BIN   = BIN_DIR + '/' + 'macos/tesseract'
WIN_BIN   = BIN_DIR + '/' + 'win/Tesseract-OCR/tesseract'
LINUX_BIN = BIN_DIR + '/' + 'linux/tesseract'

pytesseract.tesseract_cmd = WIN_BIN
os.environ['TESSDATA_PREFIX'] = LANG_DIR

def testPil(filepath):
    filepath = e.get()
    label.delete(0.0, tkinter.END)
    warn.delete(0.0, tkinter.END)

    try:
        a = Image.open(filepath)
        text = pytesseract.image_to_string(a, lang='chi_sim')

        label.insert(tkinter.INSERT, text)
    except Exception as err:
        print("---------------", err)
        warn.delete(0.0, tkinter.END)
        warn.insert(tkinter.INSERT, err)

def selectPath():
    path__ = askopenfilename()
    var.set(path__)

window = tkinter.Tk()
window.title('Picture OCR')
window.geometry("600x800")
tkinter.Label(window, text="图片路径:").pack()
# choose filepath
var = tkinter.StringVar()
e = tkinter.Entry(window, width=100, textvariable=var)
filepath = var.get()
e.pack()
tkinter.Button(window, text="路径选择", command=selectPath).pack()

s = tkinter.StringVar()
# label = tkinter.Entry(window, textvariable=s, bg='pink', width=100, justify='left')
label = tkinter.Text(window, bg='pink')
label.pack()
button = tkinter.Button(window, text="运行", bg='white', command=lambda: testPil(filepath))
button.pack()
warn = tkinter.Text(window, bg='white')
warn.pack()

def delete():
    label.delete(0.0, tkinter.END)

window.mainloop()


