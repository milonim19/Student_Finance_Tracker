# main_v2_fintech.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 8, 2025
# Description: This is a wrapper around existing main_v2 FinanceTrackerGUI to apply a fintech ttk theme.
# Keeps the dashboard layout the SAME, only updates styles/colors/fonts.

import tkinter as tk
from ui_theme_fintech import apply_fintech_theme
from main_v2 import FinanceTrackerGUI

def main():
    root = tk.Tk()
    apply_fintech_theme(root)
    app = FinanceTrackerGUI(root)
    root.title("Student Finance Tracker")
    root.minsize(1000, 700)
    root.mainloop()

if __name__ == "__main__":  #calling the main function.
    main()
