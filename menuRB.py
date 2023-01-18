from tkinter import *
root = Tk()

root.title('my RBMenu app')
root.iconbitmap('apple.ico')
root.geometry('400x400')

PRODUCT = [

    ('Microsoft Surface','Microsoft Surface'),
    ('Google Pixel', 'Google Pixel'),
    ('Asus ROG', 'Asus ROG'),
    ('Macbook Pro', 'Macbook Pro'),
    ('HP OMEN', 'HP OMEN'),
    ('Apple iPhone SE2', 'Apple iPhone SE2'),
    ('BOSE q3 Headphones', 'BOSE q3 Headphones')

]

choice = StringVar()
choice.set('Microsoft Surface')

for text,mode in PRODUCT:
    Radiobutton(root, text=text, variable=choice, value=mode).pack(anchor='w')

def my_click(value):
    my_label = Label(root, text=value)
    my_label.pack()
    
my_button = Button(root, text='buy now', command=lambda:my_click(choice.get()))
my_button.pack()

root.mainloop()