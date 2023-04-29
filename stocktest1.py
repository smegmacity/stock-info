import yfinance as yf
import pandas as pd

def get_stock_info(ticker):
    # Get the stock data
    stock = yf.Ticker(ticker)
    df = stock.info

    # Get the company name
    company_name = df.get("longName", "NA")

    # Get the ticker symbol
    ticker_symbol = df.get("symbol", "NA")

    # Get the current price or the most recent close price if market is closed
    if df.get("regularMarketPrice"):
        current_price = df.get("regularMarketPrice")
    else:
        current_price = df.get("regularMarketPreviousClose", "NA")

    # Get the book value
    book_value = df.get("bookValue", "NA")

    # Get the dividend yield
    dividend_yield = df.get("dividendYield", "NA")

    # Get the price-to-book ratio
    price_to_book_ratio = df.get("priceToBook", "NA")

    # Get the price-to-earnings ratio
    price_to_earnings_ratio = df.get("trailingPE", "NA")

    # Get the market cap
    market_cap = df.get("marketCap", "NA")

    # Return a dictionary of the stock information
    return {
        "Company Name": company_name,
        "Ticker Symbol": ticker_symbol,
        "Current Price": current_price,
        "Book Value": book_value,
        "Dividend Yield": dividend_yield,
        "Price-to-Book Ratio": price_to_book_ratio,
        "Price-to-Earnings Ratio": price_to_earnings_ratio,
        "Market Cap": market_cap
    }

# Prompt user to enter a list of ticker symbols separated by commas
ticker_list = input("Enter a list of ticker symbols separated by commas: ")

# Split the input string by commas to get a list of tickers
tickers = [ticker.strip() for ticker in ticker_list.split(",")]

# Create an empty DataFrame to store the stock information
df = pd.DataFrame()

# Loop through the list of tickers and get the stock information for each ticker
for ticker in tickers:
    # Get the stock information
    stock_info = get_stock_info(ticker)

    # Create a DataFrame from the stock information and append it to the main DataFrame
    stock_df = pd.DataFrame(stock_info, index=[0])
    df = pd.concat([df, stock_df])

# Export the DataFrame to an Excel file
df.to_excel(f"{ticker}.xlsx")
