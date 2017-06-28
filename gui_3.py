import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text = "Height:")
label1.grid(row = 0, column = 0)
label2 = tk.Label(root, text = "Width:")
label2.grid(row = 1, column = 0)

entry1 = tk.Entry(root)
entry1.grid(row = 0, column = 1)
entry2 = tk.Entry(root)
entry2.grid(row = 1, column = 1)

checkbutton = tk.Checkbutton(root, text = "Preserve aspect")
checkbutton.grid(row = 2, column = 0, rowspan = 1, columnspan = 2, sticky=tk.W)#sticky设置控件的对其方位，这里设置为靠西(左西右东)


button1 = tk.Button(root, text = "Zoom in")
button1.grid(row = 2, column = 2)
button1 = tk.Button(root, text = "Zoom out")
button1.grid(row = 2, column = 3)

root.mainloop()
