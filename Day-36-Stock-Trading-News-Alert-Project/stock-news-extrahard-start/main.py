import requests
import datetime as dt
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5%
# between yesterday and the day before yesterday then print("Get News").
stock_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "PZ2E7YWVTCFCX72G"
}

response = requests.get(url=stock_endpoint, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_closing_price = float(data_list[0]["4. close"])
the_day_before_closing_price = float(data_list[1]["4. close"])
# print(yesterday_closing_price, the_day_before_closing_price)
difference_price = yesterday_closing_price - the_day_before_closing_price
up_down = None
if difference_price <= 0:
    up_down = "🔻"
else:
    up_down = "🔺"

difference = round(abs(difference_price) / yesterday_closing_price) * 100
print(difference)

# should be >= 5, this is for testing purposes
if difference >= 0:
    # print("Get news")

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # 8ea8c686fca940cebf348295fe1c3dd0
    news_endpoint = "https://newsapi.org/v2/everything"
    today = dt.datetime.now().date()
    news_parameters = {
        "q": "tesla",
        "from": today.strftime('%Y-%m-%d'),
        "sortBy": "publishedAt",
        "apiKey": "8ea8c686fca940cebf348295fe1c3dd0",
        "language": "en"
    }

    response = requests.get(url=news_endpoint, params=news_parameters)
    response.raise_for_status()
    data=response.json()["articles"][:3]
    formatted_articles = [f"{STOCK}: {up_down}{difference}% \nHeadline: {article['title']} \nBrief: {article['description']}"for article in data]
    print(formatted_articles)





## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# PZ2E7YWVTCFCX72G
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=PZ2E7YWVTCFCX72G

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


# today = dt.datetime.now().date() - dt.timedelta(3)
# yesterday = today - dt.timedelta(1)
# today.strftime('%Y-%m-%d')