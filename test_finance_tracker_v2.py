# test_finance_tracker_v2.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 3, 2025
# Description: Enhanced pytest test cases for final Finance Tracker

import pytest
import pandas as pd
import os
from Transaction_v2 import Transaction
from FinanceTracker_v2 import FinanceTracker


@pytest.fixture
def sample_transaction():
    """
    Create a sample transaction for testing.

    Returns:
        Transaction: A sample transaction object
    """
    return Transaction(
        date="2025-11-18",
        mode="Cash",
        category="Food",
        sub_category="Lunch",
        trans_type="Expense",
        amount=15.50,
        notes="Test transaction"
    )


@pytest.fixture
def temp_tracker():
    """
    Create a temporary finance tracker for testing with no initial data.

    Returns:
        FinanceTracker: A finance tracker with temporary test file
    """
    test_file = "test_transactions_temp.csv"

    # Remove test file if it exists to start fresh
    if os.path.exists(test_file):
        os.remove(test_file)

    # Create empty CSV file to prevent sample data creation
    pd.DataFrame(columns=[
        'Date', 'Mode', 'Category', 'Sub Category',
        'Income/Expense', 'Amount', 'Notes'
    ]).to_csv(test_file, index=False)

    # Create tracker with empty file
    tracker = FinanceTracker(test_file)

    yield tracker

    # Cleanup: remove test file after test
    if os.path.exists(test_file):
        os.remove(test_file)


def test_transaction_creation(sample_transaction):
    """
    Test that a Transaction object is created correctly.
    """
    assert sample_transaction.date == "2025-11-18"
    assert sample_transaction.mode == "Cash"
    assert sample_transaction.category == "Food"
    assert sample_transaction.sub_category == "Lunch"
    assert sample_transaction.trans_type == "Expense"
    assert sample_transaction.amount == 15.50
    assert sample_transaction.notes == "Test transaction"


def test_transaction_to_dict(sample_transaction):
    """
    Test that Transaction.to_dict() returns correct dictionary format.
    """
    trans_dict = sample_transaction.to_dict()

    assert isinstance(trans_dict, dict)
    assert trans_dict['Date'] == "2025-11-18"
    assert trans_dict['Category'] == "Food"
    assert trans_dict['Amount'] == 15.50
    assert trans_dict['Notes'] == "Test transaction"


def test_transaction_is_income():
    """
    Test is_income() and is_expense() methods.
    """
    income_trans = Transaction("2025-11-18", "Cash", "Allowance",
                               "From Parents", "Income", 100.0)
    expense_trans = Transaction("2025-11-18", "Cash", "Food",
                                "Lunch", "Expense", 15.0)

    assert income_trans.is_income() == True
    assert income_trans.is_expense() == False
    assert expense_trans.is_income() == False
    assert expense_trans.is_expense() == True


def test_add_transaction(temp_tracker):
    """
    Test adding a transaction to the finance tracker.
    """
    initial_count = len(temp_tracker.transactions)

    temp_tracker.add_transaction(
        date="2025-11-18",
        mode="Card",
        category="Transportation",
        sub_category="Bus fare",
        trans_type="Expense",
        amount=3.00,
        notes="Daily commute"
    )

    assert len(temp_tracker.transactions) == initial_count + 1
    assert temp_tracker.df.shape[0] == initial_count + 1


def test_total_income_calculation(temp_tracker):
    """
    Test that total income is calculated correctly.
    """
    # Add income transactions
    temp_tracker.add_transaction("2025-11-18", "Bank Transfer", "Allowance",
                                 "From Parents", "Income", 500.00)
    temp_tracker.add_transaction("2025-11-19", "Cash", "Allowance",
                                 "Part-time job", "Income", 200.00)

    total_income = temp_tracker.get_total_income()
    assert total_income == 700.00


def test_total_expenses_calculation(temp_tracker):
    """
    Test that total expenses are calculated correctly.
    """
    # Add expense transactions
    temp_tracker.add_transaction("2025-11-18", "Cash", "Food",
                                 "Lunch", "Expense", 15.00)
    temp_tracker.add_transaction("2025-11-18", "Card", "Transportation",
                                 "Bus", "Expense", 3.00)
    temp_tracker.add_transaction("2025-11-19", "Cash", "Entertainment",
                                 "Movie", "Expense", 12.00)

    total_expenses = temp_tracker.get_total_expenses()
    assert total_expenses == 30.00


def test_balance_calculation(temp_tracker):
    """
    Test that balance is calculated correctly as income minus expenses.
    """
    # Add income
    temp_tracker.add_transaction("2025-11-18", "Bank Transfer", "Allowance",
                                 "From Parents", "Income", 500.00)

    # Add expenses
    temp_tracker.add_transaction("2025-11-18", "Cash", "Food",
                                 "Lunch", "Expense", 50.00)
    temp_tracker.add_transaction("2025-11-19", "Card", "Transportation",
                                 "Metro", "Expense", 30.00)

    balance = temp_tracker.get_balance()
    assert balance == 420.00


def test_expense_by_category(temp_tracker):
    """
    Test grouping expenses by category using pandas groupby.
    """
    # Add expenses in different categories
    temp_tracker.add_transaction("2025-11-18", "Cash", "Food",
                                 "Breakfast", "Expense", 10.00)
    temp_tracker.add_transaction("2025-11-18", "Cash", "Food",
                                 "Lunch", "Expense", 15.00)
    temp_tracker.add_transaction("2025-11-18", "Card", "Transportation",
                                 "Bus", "Expense", 5.00)

    category_totals = temp_tracker.get_expense_by_category()

    assert category_totals['Food'] == 25.00
    assert category_totals['Transportation'] == 5.00


def test_date_range_filtering(temp_tracker):
    """
    Test filtering transactions by date range.
    """
    # Add transactions on different dates
    temp_tracker.add_transaction("2025-11-01", "Cash", "Food", "Lunch", "Expense", 10.00)
    temp_tracker.add_transaction("2025-11-15", "Cash", "Food", "Dinner", "Expense", 20.00)
    temp_tracker.add_transaction("2025-11-30", "Cash", "Food", "Breakfast", "Expense", 8.00)

    # Test income calculation with date range
    income_mid_month = temp_tracker.get_total_expenses(
        start_date="2025-11-10",
        end_date="2025-11-20"
    )

    assert income_mid_month == 20.00




def test_search_transactions(temp_tracker):
    """
    Test searching transactions by keyword.
    """
    # Add transactions with specific keywords
    temp_tracker.add_transaction("2025-11-18", "Cash", "Food",
                                 "Pizza for dinner", "Expense", 20.00,
                                 notes="Dominos pizza")
    temp_tracker.add_transaction("2025-11-19", "Card", "Food",
                                 "Burger lunch", "Expense", 12.00)
    temp_tracker.add_transaction("2025-11-20", "Cash", "Transportation",
                                 "Bus fare", "Expense", 3.00)

    # Search for "pizza"
    results = temp_tracker.search_transactions("pizza")

    assert len(results) == 1
    assert "Pizza" in results.iloc[0]['Sub Category'] or "pizza" in results.iloc[0]['Notes']


def test_monthly_summary(temp_tracker):
    """
    Test monthly summary calculation.
    """
    # Add transactions in different months
    temp_tracker.add_transaction("2025-11-10", "Bank Transfer", "Allowance",
                                 "Monthly", "Income", 800.00)
    temp_tracker.add_transaction("2025-11-15", "Cash", "Food",
                                 "Lunch", "Expense", 50.00)
    temp_tracker.add_transaction("2025-12-10", "Bank Transfer", "Allowance",
                                 "Monthly", "Income", 800.00)

    summary = temp_tracker.get_monthly_summary()

    assert len(summary) >= 2
    assert any('2025-11' in month for month in summary.keys())
    assert any('2025-12' in month for month in summary.keys())


def test_save_and_load_data(temp_tracker):
    """
    Test that data can be saved to CSV and loaded correctly.
    """
    # Add some transactions
    temp_tracker.add_transaction("2025-11-18", "Cash", "Food",
                                 "Dinner", "Expense", 20.00, "Italian restaurant")
    temp_tracker.add_transaction("2025-11-18", "Bank Transfer", "Allowance",
                                 "From Dad", "Income", 300.00, "Weekly allowance")

    # Save data
    temp_tracker.save_data()

    # Create new tracker and load the same file
    new_tracker = FinanceTracker(temp_tracker.csv_file)

    # Verify data was loaded correctly
    assert len(new_tracker.transactions) == 2
    assert new_tracker.get_total_income() == 300.00
    assert new_tracker.get_total_expenses() == 20.00

    # Cleanup
    if os.path.exists(new_tracker.csv_file):
        os.remove(new_tracker.csv_file)


def test_empty_tracker(temp_tracker):
    """
    Test that empty tracker returns zero values correctly.
    """
    assert temp_tracker.get_total_income() == 0.0
    assert temp_tracker.get_total_expenses() == 0.0
    assert temp_tracker.get_balance() == 0.0
    assert temp_tracker.get_expense_by_category() == {}


