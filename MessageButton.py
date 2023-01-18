from tkinter import *
from tkinter import messagebox
root = Tk()

root.title('Message Button App')
root.iconbitmap('apple.ico')
root.geometry('500x500')

def popup():
    messagebox.showinfo('this is a message popup box','hello this is the content of the messagebox') #this is the title of the popup box
#the content sizing is determined by the content size, no need for geometric resizing

def popup2():
    messagebox.showerror('error window', 'you messed up, friend')

def popup3():
    messagebox.askokcancel('ok/cancel window', 'Continue?')

def popup4():
    messagebox.askquestion('question window', 'do you want to build a snowman?')

def popup5():
    messagebox.askyesno('yes/no window', 'am i the fairest of them all?')

b1 = Button(root, text='popup1', command=popup)
b1.pack()

b2 = Button(root, text='popup2', command=popup2)
b2.pack()

b3 = Button(root, text='popup3', command=popup3)
b3.pack()

b4 = Button(root, text='popup4', command=popup4)
b4.pack()

b5 = Button(root, text='popup5', command=popup5)
b5.pack()

root.mainloop()