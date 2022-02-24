import pandas as pd
import datetime as dt
from send_mail import send_mail

data = pd.read_csv('birthdays.csv')
birthdays = {row.names: [row.email, row.day, row.month]
             for (index, row) in data.iterrows()}


with open('letter_templates/letter_1.txt', 'r') as letter:
    template = letter.read()

now = dt.datetime.now()
day = now.day
month = now.month

for (key, value) in birthdays.items():
    if day == value[1] and month == value[2]:
        message = template.replace("[NAME]", key)
        send_mail(message)
