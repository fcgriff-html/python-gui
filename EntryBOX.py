from tkinter import *
root = Tk()

root.title('my entry box')
root.iconbitmap('apple.ico')
root.geometry('500x500')

#entry is an entry box that operated within root
#if you try to do a one liner here, you set e to the result of the .pack() command
#this in turn makes it so that you cannot access the internal portions of the entry
e = Entry(root, width=50, fg='black')
e.grid(row=0, column=1)
#you can say .pack(), but .grid will alow you to organize where the textbox appears
#grid also prevents the screen from filling with the result

ee = Entry(root, width=30, fg="black")
ee.grid(row=0, column=2)
def my_click():
    my_label = Label(root, text='hello ' + e.get()).grid(row=3, column=1)
    #the above grabs the text from the entry and displays it
    e.delete(0, END)

def my_click2():
    my_label2 = Label(root, text='hello ' + ee.get()).grid(row=3, column=2)
    ee.delete(0, END)

my_button = Button(root, text='Enter your first name', padx=10, pady=10, bg='white', fg='green', command=my_click)
my_button.grid(row=2, column=1)

my_button2 = Button(root, text='Enter your last name', padx=10, pady=10, bg='white', fg='green', command=my_click2)
my_button2.grid(row=2, column=2)


#because there is a pack() command we cant use grid, so we have to adjust the pack to grid

root.mainloop()
