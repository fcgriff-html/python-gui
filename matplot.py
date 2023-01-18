from tkinter import *
import matplotlib.pyplot as plt # pip install -U pip, pip install -U matplotlib
import numpy as np
root = Tk()

root.title('matplot app')
root.iconbitmap('star.ico')
root.geometry('500x500')
root.configure(background='grey')

def graphs():
    house = np.random.normal(20000, 25000, 5000)
    plt.hist(house, 80)
    plt.show()

def graph_get():
    exp_val = [1500, 600, 700, 400, 250]
    exp_labels = ['House rent', 'Internet Bill', 'Food', 'Fuel Charges', 'Others']

    plt.pie(exp_val, label=exp_labels, radius=1.5, autopct='%0.2f%%') #autopct displays the percentage rounded to the decimal format
    plt.axis('equal')
    plt.show()

b1 = Button(root, text='result.get', command=graph_get)
b1.pack()

root.mainloop()