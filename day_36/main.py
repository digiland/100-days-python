import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "9924d99def464eb8b5f2203b2b99ec4e"
STOCKS_API_KEY = "UTDJTMAVWJ74HJK5"

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": "2022-02-27",
    "language": "en",
    "sortBy": "relevancy",

}
response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()

news = response.json()["articles"]
news = news[:3]


# get stock data
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCKS_API_KEY,
}

r = requests.get(STOCK_ENDPOINT, params=stock_params)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]

yesterdays_data = data_list[0]
y_closing = float(yesterdays_data["4. close"])

day_before = data_list[1]["4. close"]
day_before_closing = float(day_before)

print(y_closing, day_before_closing)

# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
