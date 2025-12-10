# STUDENT FINANCE TRACKER APP
# PROGRAMMED AND DESIGNED BY VANSHIKA KUKREJA AND MILONI MEHTA 

# Student Finance Tracker (v2)

A simple Tkinter app to track income/expenses, see totals, and keep everything in one place. This is built for our class project (Python)

## Why this repo exists
We wanted a lightweight finance tool with a modern 'fintech' look (dark, minimal, readable).

## How to run
Run `main_v2_fintech.py` and program is compatible on windows and macOS operating system.
This file is a wrapper around the existing GUI in `main_v2.py` (class `FinanceTrackerGUI`). 
It loads a fintech ttk theme from `ui_theme_fintech.py` and then launches the same app with better styling. Functionality remains unchanged.

## Features
- Add income/expense transactions
- Auto-calc totals and balance
- Reads data from CSV, `transactions.csv` 
- Clean ttk styling with a fintech vibe
- Basic pytests

## Project structure
```
├── main_v2_fintech.py      # wrapper that applies the fintech ttk theme, then runs the GUI
├── ui_theme_fintech.py     # ttk theme setup (colors, fonts, styles)
├── main_v2.py              # original GUI 
├── FinanceTracker_v2.py    # data processing and handling 
├── Transaction_v2.py       # Transaction dataclass / model
├── test_finance_tracker_v2.py  # pytests
└── transactions.csv        # sample data file (created/used by the app)
```

## Requirements
- Python 3.9+
- Tkinter/ttk (usually included with Python)


## Functionality
1. **Run the app:** `python main_v2_fintech.py`  
2. **Add a few transactions** (income/expense)  
3. **Check totals/balance** update live  
4. **Set budgets**
5. **View charts**
4. **Open `transactions.csv`** to see persistent data  
5. **Run tests:** `python -m pytest -q` (or run the file directly if preferred)

## Notes
- If the UI looks default/gray, the theme probably didn’t load — make sure you’re launching `main_v2_fintech.py` (not `main_v2.py`).

