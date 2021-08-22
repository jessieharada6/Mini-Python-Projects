##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import os
import smtplib
# 1. Update the birthdays.csv

NAME = "[NAME]"
def send_email(content):
    my_email = "testemailsonlynojoke@gmail.com"
    password = "1234abcd()"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Happy birthday!\n\n{content}")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day  = now.day

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
for data in data_dict:
    if data['month'] == month and data['day'] == day:
        random_file = random.choice(os.listdir("letter_templates"))
        # file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        # can use the file path to open as well
        with open(f"letter_templates/{random_file}") as file:
            letter = file.read()
            # produce a new string
            letter = letter.replace(NAME, f"{data['name']}")
            send_email(letter)