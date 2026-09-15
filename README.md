# MarketMind AI

## Multi-Agent Stock Research Assistant

MarketMind AI is a multi-agent AI application built with CrewAI that analyzes stock market data and generates a cautious Buy, Sell, or Hold recommendation.

The application uses two specialized AI agents:

1. **Financial Market Analyst**
   - Retrieves available stock information from Yahoo Finance.
   - Reviews the current price and daily price movement.
   - Summarizes the available market observations.

2. **Strategic Stock Trader**
   - Reviews the financial analyst’s report.
   - Provides a Buy, Sell, or Hold recommendation.
   - Explains the supporting reasons, risks, and missing information.

## Workflow

User enters a stock ticker  
↓  
Yahoo Finance retrieves available stock data  
↓  
Financial Market Analyst analyzes the data  
↓  
Strategic Stock Trader reviews the analysis  
↓  
Final stock research report is displayed in Streamlit

## Technologies Used

- Python
- CrewAI
- CrewAI Tools
- Google Gemini
- Streamlit
- Yahoo Finance
- yfinance
- python-dotenv

## Project Structure

marketmind-ai/
│
├── agents.py
├── tasks.py
├── crew.py
├── main.py
├── app.py
├── tools/
│   └── stock_tool.py
├── requirements.txt
├── .env.example
└── .gitignore

## Installation

Clone the repository:

    git clone https://github.com/your-username/marketmind-ai.git

Move into the project directory:

    cd marketmind-ai

Create a virtual environment:

    python -m venv venv

Activate the virtual environment on Windows:

    venv\Scripts\activate

Install the dependencies:

    pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the project root:

    GOOGLE_API_KEY=your_google_api_key

Never upload your `.env` file or API keys to GitHub.

## Run the Application

Start the Streamlit application:

    streamlit run app.py

Then open the local Streamlit URL shown in the terminal.

## Example Stock Tickers

- AAPL - Apple
- MSFT - Microsoft
- GOOGL - Alphabet
- AMZN - Amazon
- TSLA - Tesla
- NVDA - NVIDIA

Enter the stock ticker symbol, not the full company name.

## Model Information

This project uses Google Gemini through the Google Generative AI integration.

The model may be available through Google's free tier, depending on the selected model, account, usage limits, and current Google pricing policies. Free-tier access is not unlimited and may be subject to rate limits or usage restrictions.

## Features

- Multi-agent AI workflow
- Role-based financial analysis
- Yahoo Finance data integration
- Sequential CrewAI task execution
- Buy, Sell, or Hold recommendation
- Streamlit user interface
- Basic error handling
- Educational financial analysis disclaimer

## Limitations

- Market data may be delayed or incomplete.
- The application does not perform complete technical analysis.
- Fundamental indicators may not be included.
- The recommendation depends on the available data and LLM output.
- The application does not guarantee investment returns.
- The system should not be used as the only basis for financial decisions.

## Disclaimer

This application is created for educational and research purposes only.

It does not provide professional financial advice. Stock trading involves substantial risk, and market data may be delayed or inaccurate. Always conduct independent research and consult a qualified financial professional before making investment decisions.

## Future Improvements

- Add historical price analysis.
- Add moving averages and RSI.
- Add volatility calculations.
- Add trading volume comparisons.
- Add fundamental indicators such as P/E ratio and market capitalization.
- Add charts for stock price trends.
- Add support for multiple stocks.
- Add structured JSON output.
- Add report download functionality.
- Add better validation and error handling.
