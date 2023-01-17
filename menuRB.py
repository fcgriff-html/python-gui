from tkinter import *
root = Tk()

root.title('my RBMenu app')
root.iconbitmap('apple.ico')
root.geometry('400x400')

PRODUCT = [

    ('Microsoft Surface',''),
    ('Google Pixel', ''),
    ('Asus ROG', ''),
    ('Macbook Pro', ''),
    ('HP OMEN X', ''),
    ('Lenovo Legion', '')

]

choice = StringVar()
choice.set('Microsoft Surface')