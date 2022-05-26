import tkinter as tk

def insert_point():
    return 3+4


window = tk.Tk()
window.title('my window')
##窗口尺寸
window.geometry('200x200')
#定义一个输入框entry
var = tk.StringVar()    # 这时文字变量储存器
l = tk.Label(window,
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack()


b=tk.Button(window,text='确认',width=15, height=2,command=insert_point)
b.pack()
#定义一个文本框 Text t=tk.Text(window,height=2) t.pack() ##显示出来 window.mainloop()
window.mainloop()
