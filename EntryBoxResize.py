from tkinter import *

root = Tk()

root.title('Resize Entry App')
root.iconbitmap('star.ico')
root.geometry('500x500')
root.configure(background='gray')

def clicked():
    hi_user = 'hello ' + e.get()
    l1 = Label(root, text=hi_user, font=('Arial', 20))
    l1.pack(padx=10,pady=10)

e = Entry(root, width=40, font=('Arial', 40))
e.pack(padx=10, pady=10)

b1 = Button(root, text='Click User', command=clicked)
b1.pack(padx=20, pady=20)

root.mainloop()