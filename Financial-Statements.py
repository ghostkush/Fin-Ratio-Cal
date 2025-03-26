import yfinance as yf
import pandas as pd

# Define companies to compare
companies = [
    {"ticker": "C", "name": "Citigroup Inc."},
    {"ticker": "WFC", "name": "Wells Fargo & Company"}
]

# Function to fetch financial data from Yahoo Finance
def get_financials(ticker):
    stock = yf.Ticker(ticker)
    income_stmt = stock.financials.transpose()
    balance_sheet = stock.balance_sheet.transpose()
    return income_stmt, balance_sheet

# Fetch financial data for both companies
financial_data = {company["ticker"]: get_financials(company["ticker"]) for company in companies}

# Filter data for the year 2024
filtered_income_data = {}
filtered_balance_data = {}
for ticker, (income_stmt, balance_sheet) in financial_data.items():
    if '2024-12-31' in income_stmt.index:
        filtered_income_data[ticker] = income_stmt.loc['2024-12-31']
    if '2024-12-31' in balance_sheet.index:
        filtered_balance_data[ticker] = balance_sheet.loc['2024-12-31']

# Convert filtered data to DataFrames
df_income_filtered = pd.DataFrame(filtered_income_data).transpose()
df_balance_filtered = pd.DataFrame(filtered_balance_data).transpose()

# Export financial data to Excel
excel_path = "financial_statement.xlsx"
with pd.ExcelWriter(excel_path) as writer:
    df_income_filtered.to_excel(writer, sheet_name="Income Statement", index=True)
    df_balance_filtered.to_excel(writer, sheet_name="Balance Sheet", index=True)

print(f"Income statement and balance sheet for 2024 saved to {excel_path}")