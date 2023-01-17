from tkinter import *
root = Tk()

root.title('My Button')
root.iconbitmap('apple.ico')
root.geometry('500x500')


#now when the button is clicked this label will display
#the .pack() command will display the label beneath the button while the 
#.grid() command will not work as the button already controls the geometry
# it results in this error 'cannot use geometry manager grid inside . which already has slaves managed by pack'
def my_click():
    my_label = Label(root, text='welcome to the app', fg='#3371FF').pack()

my_button = Button(root, text='click this button', command=my_click, fg='black', bg='#33FFCA', padx=30, pady=30)
my_button.pack() #the button wont do anything eithout the command argument
#fg and bg args are the foreground and background colors, they accept hex and colors, padx, pady arg is padding and takes and int variable

root.mainloop()