import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

URL = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": "112223"
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=URL, params=parameters)
data = response.json()

yesterday_close_stock = float([value["4. close"] for (key, value) in data["Time Series (Daily)"].items()][0])

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_close_stock = float([value["4. close"] for (key, value) in data["Time Series (Daily)"].items()][1])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_close_stock - before_yesterday_close_stock

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = round(difference / before_yesterday_close_stock * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage) > 1:
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_url = "https://newsapi.org/v2/everything"

    news_parameters = {
        "q": COMPANY_NAME.lower(),
        "sortBy": "publishedAt",
        "apiKey": "112233"
    }

    response = requests.get(url=news_url, params=news_parameters)
    data = response.json()

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    # print(data["articles"][:3])

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    new_list = [{"headline": val["title"], "description": val["description"]} for val in data["articles"][:3]]

    #TODO 9. - Send each article as a separate message via Twilio. 
    for num in range(len(new_list)):
        headline = new_list[num]["headline"]
        description = new_list[num]["description"]
        msg = f"{STOCK_NAME}: {up_down} {percentage}%\n {COMPANY_NAME}\n Headline: {headline}\n Brief: {description}"

        account_sid = "abcd123"
        auth_token = "abcd123"
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_="whatsapp:+1111", body=msg, to="whatsapp:+12222")
        print(message.sid)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

