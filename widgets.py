from constants import AppColors
import tkinter as tk

# define the custom widgets


class CustomLabel(tk.Label):
    """
    Custom label widget
    """

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        if not kwargs.get('bg'):
            self.configure(bg=AppColors.BG)
        if not kwargs.get('fg'):
            self.configure(fg=AppColors.TEXT)
