from crewai import Task
from agents.analyst_agent import analyst_agent


get_stock_analysis = Task(
    description=(
        "Analyze the recent performance of {stock}. "
        "Use the Yahoo Finance stock data tool to retrieve "
        "available current price and daily price movement. "
        "Only discuss information returned by the tool. "
        "Do not invent volume, volatility, or technical indicators."
    ),
    expected_output=(
        "A clean Markdown report containing:\n"
        "- Stock symbol\n"
        "- Current price\n"
        "- Daily price change\n"
        "- Daily percentage change\n"
        "- Available market observations\n"
        "- Data limitations"
    ),
    agent=analyst_agent
)
