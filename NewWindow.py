from tkinter import *
root = Tk()

root.title('new window app')
root.iconbitmap('apple.ico')
root.geometry('500x500')

def click():
    new = Toplevel()
    new.title('new window')
    new.iconbitmap('star.ico')
    new.geometry('400x400')

    label = Label(new, text='opened a new window')
    label.pack()

    b2 = Button(new, text='exit', command=new.quit) #this closes the new window and the old window
    b2.pack()

b1 = Button(root, text='open a new window', command=click)
b1.pack()

mainloop()

#mainloop() and root.mainloop() seem to operate the same way