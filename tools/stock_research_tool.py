import yfinance as yf
from crewai.tools import tool


@tool("Yahoo Finance Stock Data Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieves available recent stock price data from Yahoo Finance.
    """

    try:
        ticker = yf.Ticker(stock_symbol.upper())
        history = ticker.history(period="5d")

        if history.empty:
            return f"No market data found for {stock_symbol.upper()}."

        latest = history.iloc[-1]
        previous = history.iloc[-2] if len(history) > 1 else None

        current_price = float(latest["Close"])

        if previous is not None:
            previous_close = float(previous["Close"])
            change = current_price - previous_close
            percentage_change = (change / previous_close) * 100
        else:
            change = 0
            percentage_change = 0

        volume = int(latest["Volume"])

        return (
            f"Stock: {stock_symbol.upper()}\n"
            f"Current Price: {current_price:.2f} USD\n"
            f"Daily Change: {change:+.2f} USD\n"
            f"Daily Percentage Change: {percentage_change:+.2f}%\n"
            f"Latest Trading Volume: {volume:,}\n"
            f"Data Source: Yahoo Finance\n"
            f"Note: Data may be delayed or incomplete."
        )

    except Exception as error:
        return f"Unable to retrieve data for {stock_symbol.upper()}: {error}"
