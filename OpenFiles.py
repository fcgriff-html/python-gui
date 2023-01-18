from tkinter import *
from tkinter import filedialog #this import allows for the filebrowser functionality
#from PIL import Image,ImageTK
root = Tk()

root.title('Open Files App')
root.iconbitmap('apple.ico')
root.geometry('500x500')

def click():
    root.filename = filedialog.askopenfilename(initialdir='C:\'', title='Select File',filetypes=(('jpg files', '*.jpg'), ('all files', '*.*')))

b1 = Button(root, text='open file', command=click)
b1.pack()

my_label = Label(root, text='All Done')
my_label.pack()

root.mainloop()