from tkinter import *
root = Tk()

root.title('my Radio Button App')
root.iconbitmap('star.ico')
root.geometry('500x500')

q = IntVar()
q.get()
q.set('2')
#q gets initialized as 0 and displayed if we do not set it, anyway

def my_click(value):
    my_label = Label(root, text = value)
    my_label.pack()

Radiobutton(root, text='1', variable=q , value=1).pack(anchor='w')
Radiobutton(root, text='2', variable=q, value=2).pack(anchor='w')
Radiobutton(root, text='3', variable=q , value=3).pack(anchor='w')
Radiobutton(root, text='4', variable=q , value=4).pack(anchor='w')

my_label = Label(root, text= q.get())
my_label.pack()

my_button = Button(root, text='Submit', command=lambda:my_click(q.get()))
my_button.pack()
#the lambda expression allows us to pass the value obtained from the radio button to the function my_click()



root.mainloop()