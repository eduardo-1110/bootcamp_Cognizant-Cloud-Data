import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle  = Button(root, text='abrir o google',command=google).pack(pady=20)
root.mainloop()