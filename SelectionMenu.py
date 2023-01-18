from tkinter import *
root = Tk()

root.title('Option app')
root.iconbitmap('apple.ico')
root.geometry('400x400')

def open():
    my_label = Label(root, text=clicked.get())
    my_label.grid(row=2,column=2,ipadx=30,pady=10)

options = [
    'iPhone XR',
    'iPhone SE',
    'iPhone X',
    'iPhone X Max',
    'Google Pixel',
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root,clicked,*options)
drop.grid(row=0,column=1,padx=10,pady=10)

my_button = Button(root, text='Submit', command=open)
my_button.grid(row=0,column=2,padx=10,pady=10)

root.mainloop()