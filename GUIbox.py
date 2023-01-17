from tkinter import * 
root = Tk()

root.title('my gui app')
root.iconbitmap('star.ico')
root.geometry("500x500")

my_label = Label(root, text='my new gui app').grid(row=0, column=0)
my_label2 = Label(root, text='this is line 2').grid(row=1, column=0)

#my_label.grid(row=0, column = 1)
#my_label2.grid(row=0, column = 2)

root.mainloop()