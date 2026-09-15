from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Review the financial analyst's report for {stock}. "
        "Based only on the available information, provide a cautious "
        "Buy, Sell, or Hold decision. "
        "Clearly explain the reasoning and mention missing data."
    ),
    expected_output=(
        "A clean Markdown report containing:\n"
        "- Recommendation: Buy, Sell, or Hold\n"
        "- Supporting reasons\n"
        "- Main risks\n"
        "- Missing information\n"
        "- Confidence level\n"
        "- Financial disclaimer"
    ),
    agent=trader_agent
)
