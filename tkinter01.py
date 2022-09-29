from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

window = Tk()
window.title("NQT Form")
window.geometry("800x500")

label = Label(window, text="Hello NQT", fg="red", font=("Arial", 50))
label.grid(column=0, row=0)

txt = Entry(window, width=20)
txt.grid(column=0, row=1)

def handleButton():
    label.config(text=("Hi, " + txt.get()))


def showInfo():
    messagebox.showinfo("NQT form", (combo.get() + " được chọn"))

btn = Button(window, text="Say Hello", command=showInfo)
btn.grid(column=1, row=1)

combo = Combobox(window, values=("Select 1",
                                 "Select 2",
                                 "Select 3",
                                 "Select 4"), )
combo.grid(column=0, row=2)



window.mainloop()