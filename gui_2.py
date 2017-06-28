import tkinter as UI


# 回调函数
def resize(ev=None):
    label.config(font='Hello %d bold' % scale.get())


top = UI.Tk()

top.geometry('250x150')
label = UI.Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=UI.Y, expand=1)

scale = UI.Scale(top, from_=10, to=40, orient=UI.HORIZONTAL, command=resize)
scale.set(12)
# 绘画界面,fill=UI.X,expand=1表示可以被撑开
scale.pack(fill=UI.X, expand=1)

quit = UI.Button(top, text="QUIT", command=top.quit, activeforeground='white', activebackground='red')
quit.pack()
# 消息循环
UI.mainloop()  