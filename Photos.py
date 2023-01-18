from tkinter import *
from PIL import Image,ImageTk #apparently the PIL library can be reached by pip install Pillow LOL
root = Tk()

root.title('Photo app')
root.iconbitmap('apple.ico')
root.geometry('500x500')

img1 = ImageTk.PhotoImage(Image.open('[your image to open]'))
label = Label(root, image= img1)
label.pack()

def quit_file():
    root.quit()

qbutton = Button(root, text='Exit Image', command=quit_file)
qbutton.pack()

root.mainloop()