from tkinter import *
root = Tk()

root.title('Overwrite Labels')
root.iconbitmap('apple.ico')
root.geometry('500x500')

def click():
    global l1
    hello_user = 'Hello ' + e.get()
    l1 = Label(root, text= hello_user, font=('Arial', 25))
    l1.grid(row=3, column=0)
    e.delete(0, END)
    b1['state']=DISABLED

def delete():
    l1.grid_forget()
    b1['state']=NORMAL

e = Entry(root, width=18, font=('Arial', 20))
e.grid(row=0,column=0)

b1 = Button(root, text='name here', command=click)
b1.grid(row=1,column=0)

delbtn = Button(root, text='delete text', command=delete)
delbtn.grid(row=6,column=0)

root.mainloop()