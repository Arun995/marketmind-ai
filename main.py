from dotenv import load_dotenv

# Load environment variables before importing the crew
load_dotenv()

from crew import stock_crew


def run(stock_symbol: str):

    stock_symbol = stock_symbol.upper().strip()

    if not stock_symbol:
        raise ValueError("Stock symbol cannot be empty.")

    result = stock_crew.kickoff(
        inputs={
            "stock": stock_symbol
        }
    )

    analyst_report = ""
    trading_decision = ""

    if result.tasks_output:

        if len(result.tasks_output) >= 1:
            analyst_report = result.tasks_output[0].raw

        if len(result.tasks_output) >= 2:
            trading_decision = result.tasks_output[1].raw

    return {
        "stock": stock_symbol,
        "analyst_report": analyst_report,
        "trading_decision": trading_decision
    }


if __name__ == "__main__":

    output = run("AAPL")

    print("\n===== FINANCIAL ANALYST REPORT =====\n")
    print(output["analyst_report"])

    print("\n===== STRATEGIC TRADING DECISION =====\n")
    print(output["trading_decision"])