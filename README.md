# Financial Ratio Calculator

This repository contains a Python-based financial ratio calculator that leverages the `yfinance` API to retrieve and analyze financial data for two companies.

---

## 📊 Overview

The application performs the following key tasks:

1. **Data Retrieval**: Fetches financial statements (income statement and balance sheet components) for two selected companies using the `yfinance` API.
2. **Data Export**: Saves the relevant financial data to an Excel file, with each company's data on a separate sheet.
3. **Ratio Calculation**: Calculates key financial ratios by extracting the appropriate columns from the financial statements and returns the results in a pandas DataFrame.
4. **Visualization**: Uses `matplotlib` to create side-by-side comparison plots of selected financial ratios between the two companies.

---

## ⚠️ Notes

- Financial statements on Yahoo Finance are **not fully standardized**. As a result, the code may occasionally misread or skip certain columns due to variations in naming conventions across companies.
- This project is still in development and may contain bugs or inconsistent results due to API limitations. (Only can perform on Intel and AMD)

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-ratio-calculator.git
   cd financial-ratio-calculator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

> **Note:** If `requirements.txt` isn't created yet, make sure to include libraries like `yfinance`, `pandas`, `matplotlib`, and `openpyxl`.

---

## 🚀 Usage

1. Run the script:
   ```bash
   python ratio_calculator.py
   ```

2. Enter the ticker symbols when prompted (e.g., `INTC`, `AMD`).

3. The program will:
   - Fetch financial data from Yahoo Finance.
   - Export the data to an Excel file.
   - Calculate and display financial ratios.
   - Plot the ratios for comparison.

---

## 🔧 Roadmap

Planned improvements and features:

- [ ] Add `try-except` blocks to handle data inconsistencies and improve error messaging.
- [ ] Normalize column headers across different companies.
- [ ] Include additional financial ratios (e.g., liquidity, solvency, efficiency metrics).
- [ ] Create a GUI or web-based version using Streamlit or Flask.
- [ ] Allow historical comparison (e.g., over multiple years or quarters).
- [ ] Unit tests for ratio calculation functions.

---

## 📎 License

This project is open source and available under the [MIT License](LICENSE).
