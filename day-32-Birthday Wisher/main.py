import smtplib
from datetime import datetime
import random

email_sender = "sample@gmail.com"
email_pass = "sampelpasss"
send_to = "sample@gmail.com"


def send_email(day, msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email_sender, email_pass)

        connection.sendmail(email_sender, send_to, msg=f"Subject:{day} Quotes\n\n {msg}")
        connection.close()


with open("quotes.txt", mode="r") as data_file:
    list_data = [item.strip() for item in data_file]

now = datetime.now()
week_day = now.weekday()

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if week_day < 5:
    send_email(day=days_of_week[week_day], msg=random.choice(list_data))