from constants import AppColors
import tkinter as tk

# define the custom widgets


class CustomLabel(tk.Label):
    """
    Custom label widget
    """

    def __init__(self, master, *args, **kwargs):
        kwargs.setdefault('bg', AppColors.BG)
        kwargs.setdefault('fg', AppColors.TEXT)
        super().__init__(master, *args, **kwargs)


class CustomButton(tk.Button):
    """
    Custom button widget
    """

    def __init__(self, master, *args, **kwargs):
        kwargs.setdefault('bg', AppColors.PRIMARY)
        kwargs.setdefault('fg', AppColors.TEXT)
        kwargs.setdefault('activebackground', AppColors.SECONDARY)
        kwargs.setdefault('activeforeground', AppColors.TEXT)
        kwargs.setdefault('borderwidth', 0)
        kwargs.setdefault('width', 10)
        kwargs.setdefault('height', 2)
        super().__init__(master, *args, **kwargs)
