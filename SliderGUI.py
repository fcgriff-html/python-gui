from tkinter import *
root = Tk()

root.title('slider gui app')
root.iconbitmap('apple.ico')
root.geometry('500x500')

vertical_slider = Scale(root,from_=250,to=0,orient=VERTICAL)
vertical_slider.pack(anchor='w')

horizontal_slider = Scale(root,from_=0,to=250,orient=HORIZONTAL)
horizontal_slider.pack(anchor='w')

def slider():
    l1 = Label(root, text='vert label').pack()
    vert_label = Label(root, text=vertical_slider.get()).pack()
    l2 = Label(root, text='hori label ').pack()
    hori_label = Label(root, text=horizontal_slider.get()).pack()

vert_button = Button(root, text='click vert', command=slider)
vert_button.pack()

root.mainloop()