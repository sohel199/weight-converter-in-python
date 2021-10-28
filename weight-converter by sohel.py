from tkinter import *
from tkinter import font

window = Tk()
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)


window.title("created by sohel")
e1 = Label(window, text=" weight in KG",font=(font.ITALIC,10,font.BOLD))
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram",fg="blue")
e4 = Label(window, text="Pound",fg="blue")
e5 = Label(window, text="Ounce",fg="blue")

t2 = Text(window, height=2, width=30,bg="red")
t3 = Text(window, height=2, width=30,bg="yellow")
t1 = Text(window, height=2, width=30,bg="green")


b1 = Button(window, text="Convert", command=from_kg,bd=4)


e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)


window.mainloop()