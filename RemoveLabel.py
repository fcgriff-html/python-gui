from tkinter import *
root = Tk()

root.title('Remove Label App')
root.iconbitmap('apple.ico')
root.geometry('500x500')
root.configure(background='gray')

def click_add():
    global l1 #global tag allows us to ignore the scope of l1 in this function
    l1 = Label(root, text='whats up')
    l1.pack()
    b1['state'] = DISABLED

def click_del():
    l1.destroy() #this only destroys the last added label
    b1['state'] = NORMAL

b1 = Button(root, text='display label', command=click_add)
b1.pack(padx=20, pady=20)

b2 = Button(root, text='delete label', command=click_del)
b2.pack(padx=10, pady=10)

root.mainloop()