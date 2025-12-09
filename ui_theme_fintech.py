# ui_theme_fintech.py
# Authors: Group 3 - Vanshika Kukreja, Miloni Mehta
# Date: December 8, 2025
# Description: Base fintech UI theme for the app. Sets safe fonts and modern ttk styles.
# Also prevents macOS font issues and keeps the overall UI clean.

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

def _set_default_fonts(root: tk.Tk):
    #Safely set default fonts using Tk named fonts.
    try:
        default = tkfont.nametofont("TkDefaultFont")
        text = tkfont.nametofont("TkTextFont")
        fixed = tkfont.nametofont("TkFixedFont")
    except tk.TclError:
        default = tkfont.Font(name="TkDefaultFont", exists=False)
        text = tkfont.Font(name="TkTextFont", exists=False)
        fixed = tkfont.Font(name="TkFixedFont", exists=False)

    preferred = ["Segoe UI", "SF Pro Text", "Helvetica", "Arial"]
    family = None
    for fam in preferred:
        try:
            if fam in tkfont.families(root):
                family = fam
                break
        except Exception:
            pass
    if family is None:
        family = default.cget("family")

    for f in (default, text):
        try:
            f.configure(family=family, size=10)
        except Exception:
            pass
    try:
        fixed.configure(size=10)
    except Exception:
        pass


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

# Setting fonts
    _set_default_fonts(root)

    # Frames
    style.configure("TFrame", background=BG)
    style.configure("TLabelframe", background=SURFACE, borderwidth=1, relief="solid")
    style.configure("TLabelframe.Label", background=SURFACE, foreground=TEXT, font=("TkDefaultFont", 11, "bold"))
    style.map("TLabelframe", background=[("active", SURFACE)])

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

    # Tabs
    style.configure("TNotebook", background=BG, borderwidth=0)
    style.configure("TNotebook.Tab", padding=[12, 6], background=SURFACE, foreground=MUTED)
    style.map("TNotebook.Tab",
              background=[("selected", ACCENT_SOFT)],
              foreground=[("selected", ACCENT_2)])

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
