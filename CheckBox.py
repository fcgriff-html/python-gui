from tkinter import *
root = Tk()

root.title('check box app')
root.iconbitmap('apple.ico')
root.geometry('500x500')

a = StringVar() #this is the value that we initialize to hold the on/off value from the checkbox

c = Checkbutton(root, text='python', variable=a, onvalue='OK', offvalue='NO')
c.deselect() #this starts the check button unchecked
c.pack()

def click():
    my_label = Label(root,text=a.get()).pack()

b1 = Button(root, text='show value', command=click)
b1.pack()

root.mainloop()