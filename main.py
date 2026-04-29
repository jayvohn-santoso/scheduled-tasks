##################### Extra Hard Starting Project ######################
# -------------- MODULES -------------- #
import os
import smtplib
import datetime as dt
import pandas
import random

# -------------- COLLECTING DATA -------------- #
letter_templates = [
    "letter_templates/letter_1.txt", 
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"]

today = dt.datetime.now()

df = pandas.read_csv("birthdays.csv")

# -------------- CHECKING BIRTHDAYS -------------- #
for i in range(len(df)):
    if int(df.month[i]) == today.month and int(df.day[i]) == today.day:
        random_letter = random.choice(letter_templates)

        # -------------- REPLACING NAME -------------- #
        with open(random_letter, "r") as file:
            content = file.read()

        letter_content = content.replace("[NAME]", df.name[i])
        
        # -------------- SENDING EMAILS -------------- #
        MY_EMAIL = os.environ.get("MY_EMAIL")
        MY_PASSWORD = os.environ.get("MY_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=df.email[i],
                                msg=f"Subject: Birthday Wisher\n\n{letter_content}")
