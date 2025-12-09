# FinanceTracker_v2.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 3, 2025
# Description: Enhanced FinanceTracker class with advanced analytics and budget management

import pandas as pd
from datetime import datetime, timedelta
from Transaction_v2 import Transaction


class FinanceTracker:
    """
    Enhanced finance tracker with budgeting, analytics, and advanced features.
    Manages all financial transactions for the student finance tracker.
    """

    def __init__(self, csv_file='transactions.csv'):
        """
        Initialize the FinanceTracker with a CSV file.

        Args:
            csv_file (str): Path to the CSV file storing transactions
        """
        self.csv_file = csv_file
        self.transactions = []
        self.df = None
        self.budgets = {}  # Dictionary to store category budgets
        self.load_data()

    def load_data(self):
        """
        Load transaction data from CSV file.
        Creates a new file with sample data if it doesn't exist.
        """
        try:
            # Read CSV file using pandas
            self.df = pd.read_csv(self.csv_file)

            # Add Notes column if it doesn't exist (backward compatibility)
            if 'Notes' not in self.df.columns:
                self.df['Notes'] = ''

            # Convert DataFrame rows to Transaction objects
            for _, row in self.df.iterrows():
                trans = Transaction(
                    date=row['Date'],
                    mode=row['Mode'],
                    category=row['Category'],
                    sub_category=row['Sub Category'],
                    trans_type=row['Income/Expense'],
                    amount=row['Amount'],
                    notes=row.get('Notes', '')
                )
                self.transactions.append(trans)

        except FileNotFoundError:
            # Create empty DataFrame if file doesn't exist
            self.df = pd.DataFrame(columns=[
                'Date', 'Mode', 'Category', 'Sub Category',
                'Income/Expense', 'Amount', 'Notes'
            ])
            # Create sample data for demonstration
            self._create_sample_data()

    def _create_sample_data(self):
        """
        Create comprehensive sample transaction data for demonstration.
        """
        sample_transactions = [
            # November transactions
            ("2025-11-01", "Bank Transfer", "Allowance", "From Parents", "Income", 800.0, "Monthly allowance"),
            ("2025-11-02", "Cash", "Food", "Breakfast", "Expense", 8.5, "Campus cafe"),
            ("2025-11-02", "Card", "Transportation", "Bus fare", "Expense", 3.0, "To university"),
            ("2025-11-03", "Cash", "Food", "Lunch", "Expense", 12.0, "Lunch with friends"),
            ("2025-11-04", "Online", "Entertainment", "Movie ticket", "Expense", 15.0, "Weekend movie"),
            ("2025-11-05", "Cash", "Food", "Dinner", "Expense", 18.5, "Dinner out"),
            ("2025-11-06", "Card", "Household", "Groceries", "Expense", 45.0, "Weekly groceries"),
            ("2025-11-07", "Cash", "Food", "Snacks", "Expense", 6.5, "Study snacks"),
            ("2025-11-08", "Bank Transfer", "Allowance", "Part-time job", "Income", 150.0, "Weekly paycheck"),
            ("2025-11-09", "Card", "Transportation", "Metro", "Expense", 4.5, "Monthly pass"),
            ("2025-11-10", "Cash", "Food", "Lunch", "Expense", 13.0, "Campus food court"),
            ("2025-11-11", "Online", "Other", "Online subscription", "Expense", 9.99, "Netflix"),
            ("2025-11-12", "Cash", "Food", "Coffee", "Expense", 5.5, "Study coffee"),
            ("2025-11-13", "Card", "Entertainment", "Concert", "Expense", 35.0, "Live music"),
            ("2025-11-14", "Cash", "Food", "Dinner", "Expense", 22.0, "Restaurant"),
            ("2025-11-15", "Card", "Household", "Cleaning supplies", "Expense", 18.0, "Apartment cleaning"),
            # December transactions
            ("2025-12-01", "Bank Transfer", "Allowance", "From Parents", "Income", 800.0, "Monthly allowance"),
            ("2025-12-02", "Cash", "Food", "Breakfast", "Expense", 9.0, "Morning coffee"),
            ("2025-12-02", "Card", "Transportation", "Bus fare", "Expense", 3.0, "Daily commute"),
            ("2025-12-03", "Cash", "Food", "Lunch", "Expense", 14.0, "Quick lunch"),
        ]

        for trans_data in sample_transactions:
            self.add_transaction(*trans_data)

        self.save_data()

    def add_transaction(self, date, mode, category, sub_category, trans_type, amount, notes=""):

        # Create new transaction object
        new_trans = Transaction(date, mode, category, sub_category, trans_type, amount, notes)
        self.transactions.append(new_trans)

        # Update DataFrame - use loc to avoid FutureWarning
        new_index = len(self.df)
        trans_dict = new_trans.to_dict()
        self.df.loc[new_index] = trans_dict

    def save_data(self):
        """
        Save all transactions to the CSV file.
        """
        self.df.to_csv(self.csv_file, index=False)

    def get_total_income(self, start_date=None, end_date=None):
        """
        Calculate total income from all transactions or within date range.

        Args:
            start_date (str): Optional start date filter
            end_date (str): Optional end date filter

        Returns:
            float: Total income amount
        """
        if self.df.empty:
            return 0.0

        df_filtered = self.df.copy()

        # Apply date filters if provided
        if start_date:
            df_filtered = df_filtered[df_filtered['Date'] >= start_date]
        if end_date:
            df_filtered = df_filtered[df_filtered['Date'] <= end_date]

        income_df = df_filtered[df_filtered['Income/Expense'] == 'Income']
        return float(income_df['Amount'].sum()) if not income_df.empty else 0.0


    def get_balance(self):
        """
        Calculate current balance (income - expenses).

        Returns:
            float: Current balance
        """
        return self.get_total_income() - self.get_total_expenses()

    def get_expense_by_category(self, start_date=None, end_date=None):
        """
        Group expenses by category and calculate totals.

        Args:
            start_date (str): Optional start date filter
            end_date (str): Optional end date filter

        Returns:
            dict: Dictionary with categories as keys and total amounts as values
        """
        if self.df.empty:
            return {}

        df_filtered = self.df.copy()

        # Apply date filters if provided
        if start_date:
            df_filtered = df_filtered[df_filtered['Date'] >= start_date]
        if end_date:
            df_filtered = df_filtered[df_filtered['Date'] <= end_date]

        expense_df = df_filtered[df_filtered['Income/Expense'] == 'Expense']
        if expense_df.empty:
            return {}

        # Use pandas groupby to sum amounts by category
        category_totals = expense_df.groupby('Category')['Amount'].sum()
        return category_totals.to_dict()

    def get_monthly_summary(self):
        """
        Get income and expense summary by month.

        Returns:
            dict: Dictionary with month as key and {income, expense, balance} as value
        """
        if self.df.empty:
            return {}

        df_copy = self.df.copy()
        df_copy['Month'] = pd.to_datetime(df_copy['Date']).dt.to_period('M')

        summary = {}
        for month in df_copy['Month'].unique():
            month_data = df_copy[df_copy['Month'] == month]
            income = float(month_data[month_data['Income/Expense'] == 'Income']['Amount'].sum())
            expense = float(month_data[month_data['Income/Expense'] == 'Expense']['Amount'].sum())
            summary[str(month)] = {
                'income': income,
                'expense': expense,
                'balance': income - expense
            }

        return summary

    def get_recent_transactions(self, n=10):
        """
        Get the most recent n transactions.

        Args:
            n (int): Number of recent transactions to retrieve

        Returns:
            pandas.DataFrame: DataFrame containing recent transactions
        """
        if self.df.empty:
            return self.df
        return self.df.tail(n)

    def filter_by_date_range(self, start_date, end_date):
        """
        Filter transactions by date range.

        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format

        Returns:
            pandas.DataFrame: Filtered transactions
        """
        if self.df.empty:
            return self.df

        filtered_df = self.df[
            (self.df['Date'] >= start_date) &
            (self.df['Date'] <= end_date)
            ]
        return filtered_df

    def filter_by_category(self, category):
        """
        Filter transactions by category.

        Args:
            category (str): Category to filter by

        Returns:
            pandas.DataFrame: Filtered transactions
        """
        if self.df.empty:
            return self.df

        return self.df[self.df['Category'] == category]

    def filter_by_type(self, trans_type):
        """
        Filter transactions by type (Income or Expense).

        Args:
            trans_type (str): "Income" or "Expense"

        Returns:
            pandas.DataFrame: Filtered transactions
        """
        if self.df.empty:
            return self.df

        return self.df[self.df['Income/Expense'] == trans_type]


    def get_budget(self, category):
        """
        Get budget for a category.

        Args:
            category (str): Category name

        Returns:
            float: Budget amount or None if not set
        """
        return self.budgets.get(category)

    def check_budget_status(self, category):
        """
        Check if spending is within budget for a category.

        Args:
            category (str): Category name

        Returns:
            dict: Status with spent amount, budget, remaining, and percentage
        """
        if category not in self.budgets:
            return None

        budget = self.budgets[category]
        spent = self.get_expense_by_category().get(category, 0.0)
        remaining = budget - spent
        percentage = (spent / budget * 100) if budget > 0 else 0

        return {
            'budget': budget,
            'spent': spent,
            'remaining': remaining,
            'percentage': percentage,
            'over_budget': spent > budget
        }

    def get_spending_trend(self, category=None, days=30):
        """
        Get spending trend for last N days.

        Args:
            category (str): Optional category filter
            days (int): Number of days to analyze

        Returns:
            pandas.DataFrame: Daily spending data
        """
        if self.df.empty:
            return pd.DataFrame()

        # Get date range
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        # Filter by date range
        df_filtered = self.filter_by_date_range(start_date, end_date)

        # Filter by category if specified
        if category:
            df_filtered = df_filtered[df_filtered['Category'] == category]

        # Filter expenses only
        df_filtered = df_filtered[df_filtered['Income/Expense'] == 'Expense']

        if df_filtered.empty:
            return pd.DataFrame()

        # Group by date and sum amounts
        df_filtered['Date'] = pd.to_datetime(df_filtered['Date'])
        trend = df_filtered.groupby('Date')['Amount'].sum().reset_index()
        trend.columns = ['Date', 'Amount']

        return trend


    def delete_transaction(self, index):
        """
        Delete a transaction by index.

        Args:
            index (int): Index of transaction to delete
        """
        if 0 <= index < len(self.transactions):
            del self.transactions[index]
            self.df = self.df.drop(index).reset_index(drop=True)
            self.save_data()