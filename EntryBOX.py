from tkinter import *
root = Tk()

root.title('my entry box')
root.iconbitmap('apple.ico')
root.geometry('500x500')

#entry is an entry box that operated within root
e = Entry(root, width=50, fg='black').pack()

def my_click():
    my_label = Label(root, text='hello ' + e.get()).pack()
    #the above grabs the text from the entry and displays it

my_button = Button(root, text='Enter your name', padx=10, pady=10, bg='white', fg='green', command=my_click).pack()

root.mainloop()
