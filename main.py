##################### Extra Hard Starting Project ######################
# -------------- MODULES -------------- #
import os
import smtplib
import datetime as dt
import pandas
import random

# -------------- COLLECTING DATA -------------- #
letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
today = dt.datetime.now()
df = pandas.read_csv("birthdays.csv")

# -------------- CHECKING BIRTHDAYS -------------- #
for i in range(len(df)):
    if df.month[i] == today.month and df.day[i] == today.day:
        random_letter = random.choice(letter_templates)

        # -------------- REPLACING NAME -------------- #
        with open(random_letter, "r") as file:
            content = file.read()

        new_content = content.replace("[NAME]", df.name[i])

        with open(random_letter, "w") as file:
            file.write(new_content)

        with open(random_letter, "r") as file:
            final_letter = file.read()

        # -------------- SENDING EMAILS -------------- #
        MY_EMAIL = os.environ.get("MY_EMAIL")
        MY_PASSWORD = os.environ.get("MY_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject: Birthday Wisher\n\n{final_letter}")

        # -------------- RETURNING ORIGINAL TEXT -------------- #
        with open(random_letter, "r") as file:
            edited_content = file.read()

        original_content = edited_content.replace(df.name[i], "[NAME]")

        with open(random_letter, "w") as file:
            file.write(original_content)
