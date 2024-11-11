from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters) ]
    password_letters += [random.choice(symbols) for _ in range(nr_symbols)]
    password_letters += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_letters)
    password = "".join(password_letters)

    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        password_entry.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username_email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The account details is:\n Username/Email: {username_email}\n Password: {password}")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username_email} | {password}\n")
                website_entry.delete(0, END)
                username_email_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(135, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_email_label = Label(text="Email/Username:")
username_email_label.grid(column=0, row=2)

username_email_entry = Entry(width=39)
username_email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", command=password_generator)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=37, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()