from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/word-list.csv")
to_learn = data.to_dict("records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_card["English"])


window = Tk()
window.title("Flash Card")
window.config(width=900, height=600, bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img,  highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img,  highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)

next_card()

window.mainloop()