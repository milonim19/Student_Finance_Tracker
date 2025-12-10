## STUDENT FINANCE TRACKER APP
Your personal finance buddy made by students, for students.
Built with Python + Tkinter and styled like a modern fintech app, it lets you add income/expenses, view totals instantly, and keep your spending organized without any clutter.
  
## Developed by:
  -  VANSHIKA KUKREJA
  -  MILONI MEHTA

## Project Summary
- The project uses at least one advanced Python module (e.g., tkinter/ttk, csv) and has a GUI as the main way the user interacts with the app.
- The GUI includes 5+ interactive features, such as adding transactions, selecting income/expense, entering amounts, viewing totals, loading/saving data, etc.
- There are multiple meaningful classes organized across several .py files that import each other correctly.
- The project includes clear comments and an easy-to-read README explaining how to run the program.

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

## How to run
Run `main_v2_fintech.py` and program is compatible on windows and macOS operating system.
This file is a wrapper around the existing GUI in `main_v2.py` (class `FinanceTrackerGUI`). 
It loads a fintech ttk theme from `ui_theme_fintech.py` and then launches the same app with better styling. Functionality remains unchanged.


## Functionality
1. **Run the app:** `python main_v2_fintech.py`  
2. **Add a few transactions** (income/expense)  
3. **Check totals/balance** update live  
4. **Set budgets**
5. **View charts**
4. **Open `transactions.csv`** to see persistent data  
5. **Run tests:** `python -m pytest -q` (or run the file directly if preferred)

## Notes
If the UI looks gray, the theme probably didn’t load. Please make sure you’re launching `main_v2_fintech.py` (not `main_v2.py`).

