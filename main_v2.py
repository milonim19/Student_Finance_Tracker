# main_v2.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 3, 2025
# Description: Final enhanced GUI application with advanced features

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
from FinanceTracker_v2 import FinanceTracker
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class FinanceTrackerGUI:
    """
    Enhanced GUI application for the Student Finance Tracker.
    Features: Analytics, budgets, visualizations, filtering, and export.
    """

    def __init__(self, root):
        """
        Initialize the GUI application.

        Args:
            root: tkinter root window
        """
        self.root = root
        self.root.title("Student Finance Tracker - Final Version")
        self.root.geometry("1200x800")

        # Initialize finance tracker
        self.tracker = FinanceTracker()

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)

        # Create tabs
        self.create_dashboard_tab()
        self.create_transactions_tab()
        self.create_analytics_tab()
        self.create_budget_tab()

        # Display initial data
        self.update_all_displays()

        def create_dashboard_tab(self):
        """
        Create the main dashboard tab with summary and quick actions.
        """
        dashboard_frame = ttk.Frame(self.notebook)
        self.notebook.add(dashboard_frame, text="📊 Dashboard")

        # Title
        title_label = ttk.Label(dashboard_frame, text="Financial Dashboard",
                                font=('Arial', 20, 'bold'))
        title_label.pack(pady=10)

        # Summary cards frame
        cards_frame = ttk.Frame(dashboard_frame)
        cards_frame.pack(pady=10, padx=20, fill='x')

        # Income card
        income_card = ttk.LabelFrame(cards_frame, text="💰 Total Income", padding=20)
        income_card.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
        self.income_label = ttk.Label(income_card, text="$0.00",
                                      font=('Arial', 24, 'bold'), foreground='green')
        self.income_label.pack()

        # Expenses card
        expense_card = ttk.LabelFrame(cards_frame, text="💸 Total Expenses", padding=20)
        expense_card.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        self.expense_label = ttk.Label(expense_card, text="$0.00",
                                       font=('Arial', 24, 'bold'), foreground='red')
        self.expense_label.pack()

        # Balance card
        balance_card = ttk.LabelFrame(cards_frame, text="💵 Balance", padding=20)
        balance_card.grid(row=0, column=2, padx=10, pady=5, sticky='ew')
        self.balance_label = ttk.Label(balance_card, text="$0.00",
                                       font=('Arial', 24, 'bold'))
        self.balance_label.pack()

        # Configure grid weights
        cards_frame.columnconfigure((0, 1, 2), weight=1)

        # Quick stats frame
        stats_frame = ttk.LabelFrame(dashboard_frame, text="Quick Statistics", padding=10)
        stats_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # Recent transactions preview
        ttk.Label(stats_frame, text="Recent Transactions",
                  font=('Arial', 12, 'bold')).pack(pady=5)

        # Treeview for recent transactions
        columns = ('Date', 'Category', 'Type', 'Amount')
        self.dashboard_tree = ttk.Treeview(stats_frame, columns=columns,
                                           show='headings', height=8)

        for col in columns:
            self.dashboard_tree.heading(col, text=col)
            self.dashboard_tree.column(col, width=150)

        scrollbar = ttk.Scrollbar(stats_frame, orient=tk.VERTICAL,
                                  command=self.dashboard_tree.yview)
        self.dashboard_tree.configure(yscroll=scrollbar.set)

        self.dashboard_tree.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.pack(side=tk.RIGHT, fill='y')


    def create_transactions_tab(self):
        """
        Create the transactions tab for adding and viewing transactions.
        """
        trans_frame = ttk.Frame(self.notebook)
        self.notebook.add(trans_frame, text="💳 Transactions")

        # Add transaction form
        form_frame = ttk.LabelFrame(trans_frame, text="Add New Transaction", padding=10)
        form_frame.pack(pady=10, padx=20, fill='x')

        # Row 1: Date and Mode
        row1 = ttk.Frame(form_frame)
        row1.pack(fill='x', pady=5)

        ttk.Label(row1, text="Date:").pack(side=tk.LEFT, padx=5)
        self.date_entry = ttk.Entry(row1, width=15)
        self.date_entry.pack(side=tk.LEFT, padx=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        ttk.Label(row1, text="Mode:").pack(side=tk.LEFT, padx=5)
        self.mode_var = tk.StringVar()
        self.mode_combo = ttk.Combobox(row1, textvariable=self.mode_var,
                                       values=["Cash", "Card", "Online", "Bank Transfer"],
                                       width=15)
        self.mode_combo.pack(side=tk.LEFT, padx=5)
        self.mode_combo.set("Cash")

        # Row 2: Category and Subcategory
        row2 = ttk.Frame(form_frame)
        row2.pack(fill='x', pady=5)

        ttk.Label(row2, text="Category:").pack(side=tk.LEFT, padx=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(row2, textvariable=self.category_var,
                                           values=["Food", "Transportation", "Household",
                                                   "Entertainment", "Other", "Allowance"],
                                           width=15)
        self.category_combo.pack(side=tk.LEFT, padx=5)
        self.category_combo.set("Food")

        ttk.Label(row2, text="Sub Category:").pack(side=tk.LEFT, padx=5)
        self.subcategory_entry = ttk.Entry(row2, width=20)
        self.subcategory_entry.pack(side=tk.LEFT, padx=5)

        # Row 3: Type and Amount
        row3 = ttk.Frame(form_frame)
        row3.pack(fill='x', pady=5)

        ttk.Label(row3, text="Type:").pack(side=tk.LEFT, padx=5)
        self.type_var = tk.StringVar(value="Expense")
        ttk.Radiobutton(row3, text="Income", variable=self.type_var,
                        value="Income").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(row3, text="Expense", variable=self.type_var,
                        value="Expense").pack(side=tk.LEFT, padx=5)

        ttk.Label(row3, text="Amount ($):").pack(side=tk.LEFT, padx=5)
        self.amount_entry = ttk.Entry(row3, width=15)
        self.amount_entry.pack(side=tk.LEFT, padx=5)

        # Row 4: Notes
        row4 = ttk.Frame(form_frame)
        row4.pack(fill='x', pady=5)

        ttk.Label(row4, text="Notes:").pack(side=tk.LEFT, padx=5)
        self.notes_entry = ttk.Entry(row4, width=50)
        self.notes_entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        # Add button
        add_button = ttk.Button(form_frame, text="➕ Add Transaction",
                                command=self.add_transaction)
        add_button.pack(pady=10)
        # Filter and display frame
        display_frame = ttk.LabelFrame(trans_frame, text="Transaction History", padding=10)
        display_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # Filter controls
        filter_frame = ttk.Frame(display_frame)
        filter_frame.pack(fill='x', pady=5)

        ttk.Label(filter_frame, text="Filter:").pack(side=tk.LEFT, padx=5)

        ttk.Label(filter_frame, text="Category:").pack(side=tk.LEFT, padx=5)
        self.filter_category_var = tk.StringVar(value="All")
        filter_cat_combo = ttk.Combobox(filter_frame, textvariable=self.filter_category_var,
                                        values=["All", "Food", "Transportation", "Household",
                                                "Entertainment", "Other", "Allowance"],
                                        width=12)
        filter_cat_combo.pack(side=tk.LEFT, padx=5)

        ttk.Label(filter_frame, text="Type:").pack(side=tk.LEFT, padx=5)
        self.filter_type_var = tk.StringVar(value="All")
        filter_type_combo = ttk.Combobox(filter_frame, textvariable=self.filter_type_var,
                                         values=["All", "Income", "Expense"],
                                         width=10)
        filter_type_combo.pack(side=tk.LEFT, padx=5)

        ttk.Button(filter_frame, text="🔍 Apply Filter",
                   command=self.apply_filter).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="🔄 Clear Filter",
                   command=self.clear_filter).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="📥 Export CSV",
                   command=self.export_transactions).pack(side=tk.LEFT, padx=5)

        # Search bar
        search_frame = ttk.Frame(display_frame)
        search_frame.pack(fill='x', pady=5)

        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="🔍 Search",
                   command=self.search_transactions).pack(side=tk.LEFT, padx=5)

        # Transaction list
        columns = ('Date', 'Mode', 'Category', 'Sub Category', 'Type', 'Amount', 'Notes')
        self.trans_tree = ttk.Treeview(display_frame, columns=columns,
                                       show='headings', height=15)

        for col in columns:
            self.trans_tree.heading(col, text=col)
            if col == 'Notes':
                self.trans_tree.column(col, width=150)
            else:
                self.trans_tree.column(col, width=100)

        scrollbar = ttk.Scrollbar(display_frame, orient=tk.VERTICAL,
                                  command=self.trans_tree.yview)
        self.trans_tree.configure(yscroll=scrollbar.set)

        self.trans_tree.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.pack(side=tk.RIGHT, fill='y')

    def create_analytics_tab(self):
        """
        Create the analytics tab with visualizations.
        """
        analytics_frame = ttk.Frame(self.notebook)
        self.notebook.add(analytics_frame, text="📈 Analytics")

        # Title
        ttk.Label(analytics_frame, text="Financial Analytics",
                  font=('Arial', 16, 'bold')).pack(pady=10)

        # Controls frame
        control_frame = ttk.Frame(analytics_frame)
        control_frame.pack(pady=10)

        ttk.Button(control_frame, text="📊 Show Category Breakdown",
                   command=self.show_category_chart).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="📈 Show Monthly Trend",
                   command=self.show_monthly_trend).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="📉 Show Spending Trend",
                   command=self.show_spending_trend).pack(side=tk.LEFT, padx=5)

        # Chart frame
        self.chart_frame = ttk.Frame(analytics_frame)
        self.chart_frame.pack(fill='both', expand=True, padx=20, pady=10)

    def add_transaction(self):
        """
        Add a new transaction from the input fields.
        """
        try:
            # Get input values
            date = self.date_entry.get()
            mode = self.mode_var.get()
            category = self.category_var.get()
            subcategory = self.subcategory_entry.get()
            trans_type = self.type_var.get()
            amount = float(self.amount_entry.get())
            notes = self.notes_entry.get()

            # Validate inputs
            if not subcategory:
                messagebox.showwarning("Input Error", "Please enter a subcategory!")
                return

            if amount <= 0:
                messagebox.showwarning("Input Error", "Amount must be greater than 0!")
                return

            # Add transaction
            self.tracker.add_transaction(date, mode, category, subcategory,
                                         trans_type, amount, notes)
            self.tracker.save_data()

            # Clear input fields
            self.subcategory_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.notes_entry.delete(0, tk.END)

            # Update all displays
            self.update_all_displays()

            messagebox.showinfo("Success", "Transaction added successfully!")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount!")

    def apply_filter(self):
        """
        Apply filters to transaction display.
        """
        self.display_transactions()

    def clear_filter(self):
        """
        Clear all filters.
        """
        self.filter_category_var.set("All")
        self.filter_type_var.set("All")
        self.display_transactions()

    def search_transactions(self):
        """
        Search transactions by keyword.
        """
        keyword = self.search_var.get()
        if not keyword:
            messagebox.showwarning("Search", "Please enter a search keyword!")
            return

        results = self.tracker.search_transactions(keyword)
        self.display_filtered_transactions(results)

    def export_transactions(self):
        """
        Export transactions to CSV file.
        """
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if filename:
            try:
                self.tracker.export_to_csv(filename)
                messagebox.showinfo("Success", f"Transactions exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def set_budget(self):
        """
        Set budget for a category.
        """
        try:
            category = self.budget_category_var.get()
            amount = float(self.budget_amount_entry.get())

            if not category:
                messagebox.showwarning("Input Error", "Please select a category!")
                return

            if amount <= 0:
                messagebox.showwarning("Input Error", "Budget must be greater than 0!")
                return

            self.tracker.set_budget(category, amount)
            self.budget_amount_entry.delete(0, tk.END)
            self.update_budget_display()

            messagebox.showinfo("Success", f"Budget set for {category}: ${amount:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount!")

    def update_summary(self):
        """
        Update the financial summary on dashboard.
        """
        income = self.tracker.get_total_income()
        expenses = self.tracker.get_total_expenses()
        balance = self.tracker.get_balance()

        self.income_label.config(text=f"${income:.2f}")
        self.expense_label.config(text=f"${expenses:.2f}")
        self.balance_label.config(text=f"${balance:.2f}")

        # Color code balance
        if balance >= 0:
            self.balance_label.config(foreground='green')
        else:
            self.balance_label.config(foreground='red')

    def display_transactions(self):
        """
        Display transactions with current filters.
        """
        # Clear existing items
        for item in self.trans_tree.get_children():
            self.trans_tree.delete(item)

        # Get filtered data
        df = self.tracker.df.copy()

        # Apply category filter
        if self.filter_category_var.get() != "All":
            df = df[df['Category'] == self.filter_category_var.get()]

        # Apply type filter
        if self.filter_type_var.get() != "All":
            df = df[df['Income/Expense'] == self.filter_type_var.get()]

        # Display transactions (newest first)
        for idx in range(len(df) - 1, -1, -1):
            row = df.iloc[idx]
            self.trans_tree.insert('', tk.END, values=(
                row['Date'],
                row['Mode'],
                row['Category'],
                row['Sub Category'],
                row['Income/Expense'],
                f"${row['Amount']:.2f}",
                row.get('Notes', '')
            ))

    def display_filtered_transactions(self, df):
        """
        Display a filtered DataFrame of transactions.
        """
        # Clear existing items
        for item in self.trans_tree.get_children():
            self.trans_tree.delete(item)

        # Display filtered transactions
        for idx in range(len(df) - 1, -1, -1):
            row = df.iloc[idx]
            self.trans_tree.insert('', tk.END, values=(
                row['Date'],
                row['Mode'],
                row['Category'],
                row['Sub Category'],
                row['Income/Expense'],
                f"${row['Amount']:.2f}",
                row.get('Notes', '')
            ))

    def update_dashboard_transactions(self):
        """
        Update recent transactions on dashboard.
        """
        # Clear existing items
        for item in self.dashboard_tree.get_children():
            self.dashboard_tree.delete(item)

        # Get recent transactions
        recent = self.tracker.get_recent_transactions(10)

        # Display transactions (newest first)
        for idx in range(len(recent) - 1, -1, -1):
            row = recent.iloc[idx]
            self.dashboard_tree.insert('', tk.END, values=(
                row['Date'],
                row['Category'],
                row['Income/Expense'],
                f"${row['Amount']:.2f}"
            ))

    def update_budget_display(self):
        """
        Update budget status display.
        """
        self.budget_text.delete(1.0, tk.END)

        if not self.tracker.budgets:
            self.budget_text.insert(tk.END, "No budgets set yet.\n")
            return

        self.budget_text.insert(tk.END, "=" * 80 + "\n")
        self.budget_text.insert(tk.END, "BUDGET STATUS REPORT\n")
        self.budget_text.insert(tk.END, "=" * 80 + "\n\n")

        for category in self.tracker.budgets:
            status = self.tracker.check_budget_status(category)
            if status:
                self.budget_text.insert(tk.END, f"Category: {category}\n")
                self.budget_text.insert(tk.END, f"  Budget:    ${status['budget']:.2f}\n")
                self.budget_text.insert(tk.END, f"  Spent:     ${status['spent']:.2f}\n")
                self.budget_text.insert(tk.END, f"  Remaining: ${status['remaining']:.2f}\n")
                self.budget_text.insert(tk.END, f"  Usage:     {status['percentage']:.1f}%\n")

                if status['over_budget']:
                    self.budget_text.insert(tk.END, "  ⚠️ OVER BUDGET!\n", 'warning')
                elif status['percentage'] > 80:
                    self.budget_text.insert(tk.END, "  ⚠️ Close to limit\n", 'warning')
                else:
                    self.budget_text.insert(tk.END, "  ✓ Within budget\n", 'ok')

                self.budget_text.insert(tk.END, "\n")

        # Configure tags for colors
        self.budget_text.tag_config('warning', foreground='red')
        self.budget_text.tag_config('ok', foreground='green')

    def show_category_chart(self):
        """
        Show pie chart of expenses by category.
        """
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Get category data
        categories = self.tracker.get_expense_by_category()

        if not categories:
            ttk.Label(self.chart_frame, text="No expense data available",
                      font=('Arial', 14)).pack(pady=20)
            return

        # Create pie chart
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)

        labels = list(categories.keys())
        sizes = list(categories.values())
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']

        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.set_title('Expense Distribution by Category', fontsize=14, fontweight='bold')

        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def show_monthly_trend(self):
        """
        Show bar chart of monthly income vs expenses.
        """
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Get monthly data
        monthly_data = self.tracker.get_monthly_summary()

        if not monthly_data:
            ttk.Label(self.chart_frame, text="No data available",
                      font=('Arial', 14)).pack(pady=20)
            return

        # Prepare data
        months = list(monthly_data.keys())
        incomes = [monthly_data[m]['income'] for m in months]
        expenses = [monthly_data[m]['expense'] for m in months]

        # Create bar chart
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)

        x = range(len(months))
        width = 0.35

        ax.bar([i - width / 2 for i in x], incomes, width, label='Income', color='green', alpha=0.7)
        ax.bar([i + width / 2 for i in x], expenses, width, label='Expenses', color='red', alpha=0.7)

        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Amount ($)', fontsize=12)
        ax.set_title('Monthly Income vs Expenses', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(months, rotation=45)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)

        fig.tight_layout()

        # Embed chart
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def show_spending_trend(self):
        """
        Show line chart of daily spending trend.
        """
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Get spending trend
        trend_data = self.tracker.get_spending_trend(days=30)

        if trend_data.empty:
            ttk.Label(self.chart_frame, text="No spending data available for last 30 days",
                      font=('Arial', 14)).pack(pady=20)
            return

        # Create line chart
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(trend_data['Date'], trend_data['Amount'], marker='o',
                linewidth=2, markersize=6, color='#ff6b6b')

        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Daily Spending ($)', fontsize=12)
        ax.set_title('30-Day Spending Trend', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        # Rotate x-axis labels
        fig.autofmt_xdate()
        fig.tight_layout()

        # Embed chart
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def update_all_displays(self):
        """
        Update all displays in the application.
        """
        self.update_summary()
        self.display_transactions()
        self.update_dashboard_transactions()
        self.update_budget_display()


def main():
    """
    Main function to run the application.
    """
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":

    main()


