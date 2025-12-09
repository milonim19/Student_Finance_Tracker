# ui_theme_fintech.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 8, 2025
# Description: Base fintech UI theme for the app. Sets safe fonts and modern ttk styles.
# Also prevents macOS font issues and keeps the overall UI clean.

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


def apply_fintech_theme(root: tk.Tk):
    # Apply colors
    BG = "#F7FAFC"
    SURFACE = "#FFFFFF"
    TEXT = "#0F172A"
    MUTED = "#475569"
    ACCENT = "#2563EB"
    ACCENT_2 = "#1D4ED8"
    ACCENT_SOFT = "#DBEAFE"
    BORDER = "#E2E8F0"

    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    try:
        root.configure(bg=BG)
    except tk.TclError:
        pass






    # Labels
    style.configure("TLabel", background=SURFACE, foreground=TEXT)

    # Buttons
    style.configure("TButton",
                    padding=8,
                    background=ACCENT,
                    foreground="#FFFFFF",
                    borderwidth=0,
                    font=("TkDefaultFont", 10, "bold"))
    style.map("TButton",
              background=[("active", ACCENT_2), ("disabled", BORDER)],
              foreground=[("disabled", "#94A3B8")])



    # Combobox
    style.configure("TCombobox", fieldbackground=SURFACE, background=SURFACE)
    style.configure("TEntry", fieldbackground=SURFACE, background=SURFACE)

    # Treeview
    style.configure("Treeview",
                    background=SURFACE,
                    fieldbackground=SURFACE,
                    foreground=TEXT,
                    rowheight=28,
                    bordercolor=BORDER,
                    borderwidth=1)
    style.configure("Treeview.Heading",
                    background=SURFACE,
                    foreground=TEXT,
                    font=("TkDefaultFont", 10, "bold"))
    style.map("Treeview",
              background=[("selected", ACCENT_SOFT)],
              foreground=[("selected", ACCENT_2)])

    # Scrollbar
    style.configure("Vertical.TScrollbar", background=SURFACE, troughcolor=BG, bordercolor=BORDER)
    style.configure("Horizontal.TScrollbar", background=SURFACE, troughcolor=BG, bordercolor=BORDER)
