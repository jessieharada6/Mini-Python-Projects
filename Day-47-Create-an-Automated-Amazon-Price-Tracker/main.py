import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 50
my_email = "testemailsonlynojoke@gmail.com"
password = "1234abcd()"
url = "https://www.amazon.com/Toshiba-Digital-Programmable-Uncooked-One-Touch/dp/B091TW6ND5?ref_=Oct_d_onr_d_678540011&pd_rd_w=g2U3Z&pf_rd_p=f2b556d9-2905-446e-a142-cdce50e9497c&pf_rd_r=XP60YQ76XRE2NYK2ND2N&pd_rd_r=471b8ce1-4f10-44e9-89dd-61a11ba6c2ed&pd_rd_wg=vIM4n&pd_rd_i=B091TW6ND5"
# header checked here http://myhttpheader.com/
headers = {
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(
    url=url,
    headers= headers)

aws_content = response.text
# print(aws_content)

soup = BeautifulSoup(aws_content, "lxml")
price_without_currency = soup.find(name="span", class_="a-size-medium a-color-price").getText().split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# remove white spacing
title = soup.find(id="productTitle").getText().strip()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_as_float}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}"
        )
