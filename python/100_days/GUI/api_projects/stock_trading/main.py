import os
import requests
from twilio.rest import Client

ACC_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")


parameters = {
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
    "interval": "60min",
    "apikey": STOCK_KEY
}

# You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in  data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price - day_before_yesterday_closing_price))
diff_percentage = (difference / float(yesterday_closing_price)) * 100

if diff_percentage > 1:
    news_parameter = {
        "apiKey": NEWS_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, news_parameter)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles]

    client = Client(ACC_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+13613265660",
            to="+2348138133145"
        )
        print(message.status)