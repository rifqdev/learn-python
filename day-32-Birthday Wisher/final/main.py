##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import smtplib
import random

email_sender = "sample@gmail.com"
email_pass = "sampleepass"
send_to = "sample@gmail.com"


def send_email(name, msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email_sender, email_pass)

        connection.sendmail(email_sender, send_to, msg=f"Subject:Happy Birthday {name}\n\n {msg}")
        connection.close()



now = dt.datetime.now()
date_now = now.day

df = pd.read_csv("birthdays.csv")
person = df[df["day"] == date_now]

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

if person.empty:
    print("Empty")
else:
    file_path = random.choice(letter_templates)
    with open(f"letter_templates/{file_path}", mode="r") as letter:
        template = letter.read()
        name = person["name"].values[0]
        new_template = template.replace("[NAME]", name)
        send_email(name=name, msg=new_template)



