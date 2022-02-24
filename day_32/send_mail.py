import datetime as dt
import smtplib
import random

my_email = "futurezimbabwe@gmail.com"
password = "Simplythebest"


def send_mail(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="sirdiggaz@yahoo.com", msg=message)
        connection.close()


with open("quotes.txt", "r") as data:
    quotes = data.readlines()


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    quote = random.choice(quotes)
    message = f"Subject: Happy Friday\n\n{quote}"
    send_mail(message)
