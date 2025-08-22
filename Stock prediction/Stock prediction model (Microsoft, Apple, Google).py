# This will predict stock prices by using learning models

#Install the dependencies 
import yfinance as yf
import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#Ticker List
tickers = ["MSFT", "AAPL", "GOOGL"]

#Get the stock data
df = yf.download(tickers, start="2020-01-01", end="2025-01-01")


# Get Adjusted Close Price
if 'Adj Close' in df.columns:
    df = df [['Adj Close']]
elif 'Close' in df.columns:
    df = df[['Close']]
else:
    raise KeyError("Adjusted Close price column not found!")
print(df.head())

for ticker in tickers:
    print(f"\nPredicting for {ticker}:")
    if ('Adj Close', ticker) in df.columns:
        prices = df[('Adj Close', ticker)].dropna().values
    elif ('Close', ticker) in df.columns:
        prices = df[('Close', ticker)].dropna().values
    else:
        print(f"No price data for {ticker}")
        continue

# Create Features and labels
x = []
y = []
window = 5
for i in range(len(prices) - window):
    x.append(prices[i:i+window])
    y.append(prices[i+window])

x = np.array(x)
y = np.array(y)

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

# Train Model
model = LinearRegression()
model.fit(x_train, y_train)

# Prediction
predictions = model.predict(x_test)

# Evaluation
print("First 5 predictions:", predictions[:5])
print("First 5 actual:", y_test[:5])