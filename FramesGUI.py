from tkinter import *
root=Tk()

root.title('frame GUI app')
root.iconbitmap('apple.ico')
root.geometry('800x800')

frame = LabelFrame(root, text='frame widget', padx=100, pady=100)
frame.grid(padx=20, pady=20)

def my_click():
    label1 = Label(frame,text='hello user',fg='blue')
    label1.grid(row=10,column=10)

b1 = Button(frame,text='click', command=my_click) #f you put my_click() instead of my_click, the button will execute the function on init
b1.grid(row=0,column=1)

c = Button(frame,text='exit', command=root.quit)
c.grid(row=0,column=3)

root.mainloop()