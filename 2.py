# -*- coding:utf-8 -*-
import pybase64

import threading
import tkinter as  tk
from tkinter.filedialog import askopenfilename





def picture2base(path):
   imageSuffix = path.split('.')[-1]
   with open(path, 'rb') as img:
      # 使用base64进行编码
      b64encode = pybase64.b64encode(img.read())
      s = b64encode.decode()
      base64 = 'data:image/{};base64,{}'.format(imageSuffix, s)
      # 返回base64编码字符串
      return base64
      print(base64)
def openfile():
   global filename
   filename = askopenfilename()

   var1.set(filename)
   A=picture2base(filename)
   text.insert(tk.INSERT,A)
   return filename
   # f = open(filename)
   # f.read()



root = tk.Tk()
root.title("BASE64转换")
root.geometry("1024x768+200+200")

b=tk.Button(text="打开要转换的图片",command=openfile)
b.place(x=0,y=10)
var1 = tk.StringVar()    #创建变量
lb =tk.Label(root,bg='white',width=80,height=2,textvariable=var1)
lb.place(x=150,y=10)
text= tk.Text(root,bg='white',width=270,height=80)
text.place(x=14,y=60)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
