#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import sys
import tkinter
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageEnhance
from pytesseract import pytesseract


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

tessdir = os.getenv('TESSDATA_PREFIX', None)
if tessdir is None:
    os.environ['TESSDATA_PREFIX'] = application_path
if application_path not in os.environ['PATH']:
    os.environ['PATH'] = application_path + ';' + os.environ['PATH']


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
print("fff", filepath, "fffffffdd")
tkinter.Button(window, text="路径选择", command=selectPath).pack()


s = tkinter.StringVar()
# label = tkinter.Entry(window, textvariable=s, bg='pink', width=100, justify='left')
label = tkinter.Text(window, bg='pink')
label.pack()

warn = tkinter.Text(window, bg='white')
warn.pack()


def testPil(filepath):
    filepath = e.get()
    label.delete(0.0, tkinter.END)
    warn.delete(0.0, tkinter.END)

    try:
        a = Image.open(filepath)
        a.convert('RGB')
        enhancer = ImageEnhance.Color(a)
        enhancer = enhancer.enhance(0)
        enhancer = ImageEnhance.Brightness(enhancer)
        enhancer = enhancer.enhance(2)
        enhancer = ImageEnhance.Contrast(enhancer)
        enhancer = enhancer.enhance(8)
        enhancer = ImageEnhance.Sharpness(enhancer)
        a = enhancer.enhance(20)
        # a.show()
        text = pytesseract.image_to_string(a, lang='chi_sim')

        label.insert(tkinter.INSERT, text)
    except Exception as err:
        print("---------------", err)
        warn.delete(0.0, tkinter.END)
        warn.insert(tkinter.INSERT, err)


def delete():
    label.delete(0.0, tkinter.END)


button = tkinter.Button(window, text="运行", bg='white', command=lambda: testPil(filepath))
button.pack()
window.mainloop()


