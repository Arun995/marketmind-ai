import os
import re
import streamlit as st
from main import run


os.getenv("GROQ_API_KEY")



st.set_page_config(
    page_title="MarketMind AI",
    page_icon="📈",
    layout="wide"
)


st.title("📈 MarketMind AI")
st.subheader("Multi-Agent Stock Research Assistant")

st.write(
    "Analyze a stock using a Financial Market Analyst and a Strategic Stock Trader."
)

stock_symbol = st.text_input(
    "Enter stock ticker",
    placeholder="Example: AAPL, MSFT, TSLA"
).strip().upper()

st.warning(
    "Educational use only. This application does not provide financial advice. "
    "Market data may be delayed or incomplete."
)


def extract_recommendation(text):
    """
    Extracts Buy, Sell, or Hold from the trader's response.
    """

    pattern = r"(?:Trading Decision|Recommendation)\s*:\s*\**\s*(BUY|SELL|HOLD)"

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE
    )

    if match:
        return match.group(1).upper()

    # Fallback search
    fallback = re.search(
        r"\b(BUY|SELL|HOLD)\b",
        text,
        flags=re.IGNORECASE
    )

    if fallback:
        return fallback.group(1).upper()

    return "NOT AVAILABLE"


def display_recommendation(recommendation):
    """
    Displays the recommendation in a large, consistent format.
    """

    if recommendation == "BUY":
        st.success("### 🟢 BUY")

    elif recommendation == "SELL":
        st.error("### 🔴 SELL")

    elif recommendation == "HOLD":
        st.warning("### 🟡 HOLD")

    else:
        st.info("### ℹ️ Recommendation unavailable")


if st.button("🔍 Analyze Stock", type="primary"):

    if not stock_symbol:
        st.error("Please enter a stock ticker.")
        st.stop()

    st.markdown("---")
    st.header(f"Analysis for {stock_symbol}")

    with st.spinner(f"AI agents are analyzing {stock_symbol}..."):

        try:
            result = run(stock_symbol)

            analyst_report = result.get("analyst_report", "")
            trading_decision = result.get("trading_decision", "")

            if analyst_report:
                st.header("📊 Financial Market Analysis")
                st.markdown(analyst_report)

            if trading_decision:

                st.markdown("---")
                st.header("🎯 Strategic Trading Decision")

                recommendation = extract_recommendation(
                    trading_decision
                )

                st.subheader("Recommendation")
                display_recommendation(recommendation)

                st.markdown("### Supporting Analysis")

                # Remove the recommendation line from the original output
                cleaned_decision = re.sub(
                    r"(?:\*\*)?(Trading Decision|Recommendation)(?:\*\*)?"
                    r"\s*:\s*(?:\*\*)?\s*(BUY|SELL|HOLD)(?:\*\*)?",
                    "",
                    trading_decision,
                    flags=re.IGNORECASE
                )

                st.markdown(cleaned_decision)

        except Exception as error:
            st.error("Something went wrong while analyzing the stock.")
            st.exception(error)