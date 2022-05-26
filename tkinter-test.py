import tkinter


def hello():
    print("hello")


root=tkinter.Tk()
root.title('我的tk测试')
thelabel=tkinter.Label(root,text='我的第一个窗口')
thelabel.pack()
root.mainloop()
