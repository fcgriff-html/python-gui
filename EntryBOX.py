from tkinter import *
root = Tk()

root.title('my entry box')
root.iconbitmap('apple.ico')
root.geometry('500x500')

#entry is an entry box that operated within root
e = Entry(root, width=50, fg='red').pack()

root.mainloop()
