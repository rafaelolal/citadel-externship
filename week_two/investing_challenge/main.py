from yahoofinancials import YahooFinancials
import datetime

from moving_averages import moving_average_advice

ticker = input("Enter a stock ticker: ")
days_ago = int(input("Enter the number of days ago to start from: "))

ticker = YahooFinancials(ticker)

today = datetime.datetime.today()
start = today - datetime.timedelta(days=days_ago)

data = ticker.get_historical_price_data(
    start.strftime('%Y-%m-%d'),
    today.strftime('%Y-%m-%d'),
    "daily")

prices = [day["close"] for day in data["AAPL"]["prices"]]

advice = moving_average_advice(prices)
print(advice)
