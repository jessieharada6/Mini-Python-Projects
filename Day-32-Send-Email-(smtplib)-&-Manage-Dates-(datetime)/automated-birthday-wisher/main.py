# # SMTP: simple mail transfer protocol
# import smtplib
#
# my_email = "testemailsonlynojoke@gmail.com"
# password = "1234abcd()"
#
# # connect to gmail server
# # yahoo: smtp.mail.yahoo.com
# # with - no need to close the connection
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # tls
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="jessie.harada@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(type(now))
# print(type(year))
# # monday: 0
# print(day_of_week)
#
# # int = ... => this param has default value
# date_of_birth = dt.datetime(year=1996, month=12, day=15)

# MOTIVATIONAL QUOTE ON MONDAYS VIA EMAIL
import datetime as dt
import random
import smtplib

def send_email(content):
    my_email = "testemailsonlynojoke@gmail.com"
    password = "1234abcd()"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{content}")

now = dt.datetime.now()
day_of_week = now.weekday()

quote_list = []
with open("quotes.txt", "r") as file:
    quote_list = file.readlines()
    quote = random.choice(quote_list)
    # can still access the quote outside

print(quote)
if day_of_week == 0:
    send_email(quote)

