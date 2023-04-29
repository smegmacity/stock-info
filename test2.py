import yfinance as yf
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

    # Print the information
    print("Company Name:", company_name)
    print("Ticker Symbol:", ticker_symbol)
    print("Current Price:", current_price)
    print("Book Value:", book_value)
    print("Dividend Yield:", dividend_yield)
    print("Price-to-Book Ratio:", price_to_book_ratio)
    print("Price-to-Earnings Ratio:", price_to_earnings_ratio)
    print("Market Cap:", market_cap)


# Prompt user to enter a ticker symbol
ticker = input("Enter a ticker symbol: ")

# Get the stock information
get_stock_info(ticker)
