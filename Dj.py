from tkinter import *
root = Tk()

root.title('DJ App')
root.iconbitmap('apple.ico')
root.geometry('500x500')

vslider1 = Scale(root, from_=300, to=0, orient=VERTICAL)
vslider1.grid(row=0,column=0)

vslider2 = Scale(root, from_=300, to=0, orient=VERTICAL)
vslider2.grid(row=0,column=1)

vslider3 = Scale(root, from_=300, to=0, orient=VERTICAL)
vslider3.grid(row=0,column=2)

vslider4 = Scale(root, from_=300, to=0, orient=VERTICAL)
vslider4.grid(row=0,column=3)

vslider5 = Scale(root, from_=300, to=0, orient=VERTICAL)
vslider5.grid(row=0,column=4)

def value():
    vlabel1=Label(root, text=vslider1.get()).grid(row=0,column=5)
    vlabel2=Label(root, text=vslider2.get()).grid(row=0,column=6)
    vlabel3=Label(root, text=vslider3.get()).grid(row=0,column=7)
    vlabel4=Label(root, text=vslider4.get()).grid(row=0,column=8)
    vlabel5=Label(root, text=vslider5.get()).grid(row=0,column=9)

vbutton = Button(root,text='values',command=value).grid(row=1, column=0)

root.mainloop()