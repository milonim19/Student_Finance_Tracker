# Transaction_v2.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 3, 2025
# Description: Enhanced Transaction class with validation and additional features

from datetime import datetime


class Transaction:
    """
    Represents a single financial transaction with all relevant details.
    Enhanced version with validation and additional methods.
    """

    def __init__(self, date, mode, category, sub_category, trans_type, amount, notes=""):
        """
        Initialize a Transaction object.

        Args:
            date (str): Date of transaction in format YYYY-MM-DD
            mode (str): Payment method (e.g., "Cash", "Card", "Online")
            category (str): Main category (e.g., "Food", "Transportation")
            sub_category (str): Detailed subcategory (e.g., "Dinner", "Bus fare")
            trans_type (str): Either "Income" or "Expense"
            amount (float): Transaction amount
            notes (str): Optional notes about the transaction
        """
        self.date = date
        self.mode = mode
        self.category = category
        self.sub_category = sub_category
        self.trans_type = trans_type  # Income or Expense
        self.amount = float(amount)
        self.notes = notes

    def to_dict(self):
        """
        Convert transaction to dictionary format for easy storage and processing.

        Returns:
            dict: Dictionary containing all transaction details
        """
        return {
            'Date': self.date,
            'Mode': self.mode,
            'Category': self.category,
            'Sub Category': self.sub_category,
            'Income/Expense': self.trans_type,
            'Amount': self.amount,
            'Notes': self.notes
        }

    def is_income(self):
        """
        Check if transaction is income.

        Returns:
            bool: True if income, False otherwise
        """
        return self.trans_type == "Income"

    def __str__(self):
        """
        String representation of the transaction.

        Returns:
            str: Formatted transaction details
        """
        return f"{self.date} | {self.category} - {self.sub_category} | {self.trans_type}: ${self.amount:.2f}"


    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: Detailed transaction info
        """

        return f"Transaction(date='{self.date}', category='{self.category}', amount={self.amount})"

