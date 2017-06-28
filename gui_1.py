from tkinter import *


def hello():
    print('hello')


def about():
    label = Label(root, text='Jinx\n QQ:446488651', fg='red', bg='black')
    label.pack(expand=YES, fill=BOTH)


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='打开', command=hello)
filemenu.add_command(label='保存')
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='关于作者', command=about)
menubar.add_cascade(label='关于', menu=helpmenu)
root.config(menu=menubar)
root.geometry('200x400')
root.mainloop()