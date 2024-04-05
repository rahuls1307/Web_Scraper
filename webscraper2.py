import requests
import pandas as pd

def get_news_sentiment(url, ticker, filename):
  """Fetches news sentiment data for a company and saves to a DataFrame and Excel sheet.

  Args:
      url: The URL for the Alpha Vantage API endpoint.
      ticker: The stock ticker symbol of the company.
      filename: The name of the Excel file to save the data.
  """
  r = requests.get(url)
  data = r.json()
  print(data)

  # Check if data is valid before proceeding
  if 'Error Message' in data:
    print(f"Error retrieving data for {ticker}: {data['Error Message']}")
    return

  # Create a pandas DataFrame from the data
  df = pd.DataFrame(data['feed'])

  # Save DataFrame to Excel sheet
  df.to_excel(filename, sheet_name=ticker)

# Replace with your actual API key and desired file name
url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&time_from=20180101T0000&time_to=20240901T0000&tickers={}&sort=LATEST&apikey=YOUR_API_KEY'
tickers = ['GOOGL', 'TSLA', 'GOOG', 'META', 'UNH', 'XOM', 'LLY', 'JNJ', 'V', 'PG', 'MA', 'AVGO', 'HD', 'CVX', 'MRK', 'ABBV', 'COST', 'PEP', 'ADBE']
for ticker in tickers:
  filename = ticker + '.xlsx'
  get_news_sentiment(url.format(ticker), ticker, filename)
  print(f"News sentiment data for {ticker} saved to {filename}")