# def add(*args):
#     numbers = []
#     for n in args:
#         numbers.append(n)
#     return sum(numbers)

# print(add(5,6,6))

from tkinter import *

window = Tk()
window.minsize(width=600, height=300)

my_label = Label(text="I am a label")
my_label.pack()

my_label["text"] = "new text"
# my_label.config(text="new text")

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text

button = Button(text="click me", command=button_clicked)
button.pack()


input = Entry()
input.pack()


window.mainloop()