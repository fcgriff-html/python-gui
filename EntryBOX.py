from tkinter import *
root = Tk()

root.title('my entry box')
root.iconbitmap('apple.ico')
root.geometry('500x500')

#entry is an entry box that operated within root
#if you try to do a one liner here, you set e to the result of the .pack() command
#this in turn makes it so that you cannot access the internal portions of the entry
e = Entry(root, width=50, fg='black')
e.pack()

def my_click():
    my_label = Label(root, text='hello ' + e.get()).pack()
    #the above grabs the text from the entry and displays it

my_button = Button(root, text='Enter your name', padx=10, pady=10, bg='white', fg='green', command=my_click).pack()

root.mainloop()
