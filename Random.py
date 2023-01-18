from tkinter import *
from random import randint
root = Tk()

root.title('Random Winner App')
root.iconbitmap('apple.ico')
root.geometry('500x500')

def pick():
    lst = [
        'P1',
        'P2',
        'P3',
        'P4',
        'P5',
        'P6',
        'P7',
        'P8',
    ]

    entry_set = set(lst)
    unique_list = list(entry_set)
    our_num = len(unique_list)-1
    rand = randint(0,our_num)

    winner_label = Label(root, text=unique_list[rand], font=('Helvetica', 30))
    winner_label.pack(padx=20, pady=20)

poster_label = Label(root, text='Random Winner', font=('Arial Black', 25))
poster_label.pack(padx=10,pady=10)

winButton = Button(root, text='Pick Your Winner', command=pick, font=('Arial', 30))
winButton.pack(padx=20, pady=20)

root.mainloop()