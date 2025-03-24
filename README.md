
# Financial Ratio Calculator

This repository contains a Python-based financial ratio calculator that leverages the `yfinance` API to retrieve and analyze financial data for two companies.

## Overview

The application performs the following key tasks:

1. **Data Retrieval**: Fetches financial statements (income statement and balance sheet components) for two selected companies using the `yfinance` API.
2. **Data Export**: Exports the relevant financial data to an Excel file with two separate sheets—one for each company's data.
3. **Ratio Calculation**: Calculates common financial ratios by extracting the required columns from the fetched data and returns the results in a pandas DataFrame.
4. **Visualization**: Uses `matplotlib` to create side-by-side comparisons of selected financial ratios between the two companies.

## Notes

- The code may encounter issues when fetching certain data due to inconsistencies in how financial statement columns are labeled on Yahoo Finance. Column headers may differ slightly between companies, even when referring to the same metrics.
- Future improvements include implementing `try-except` blocks to better handle exceptions and identify missing or mismatched data during the API call and data processing stages.
