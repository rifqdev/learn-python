from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()

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

generate_password_btn = Button(text="Generate Password")
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=37, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()