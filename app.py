import tkinter as tk
import time
from utils import get_result_text, get_light_text
from constants import AppText, AppColors
import random
from high_score import HighScoreManager, HighScore
from widgets import CustomLabel


class StopWatchApp:
    def __init__(self, root: tk.Tk):
        # root configuration
        self.root = root
        self.root.title(AppText.TITLE)
        self.root.geometry('400x600')
        self.root.configure(bg=AppColors.BG)

        # initialize the state of the app
        self.time = 0
        self.start_time = 0
        self.timer_running = False
        # time that player should stop the timer
        self.target_time = 5 * random.randint(2, 6)

        # load high score
        self.high_score_manager = HighScoreManager()
        self.high_score_manager.load()

        # initialize the widgets
        self.target_time_label = CustomLabel(
            root,
            text=f'STOP at {self.target_time:.2f} !',
            font=('Helvetica', 16),
        )
        self.target_time_label.pack()

        self.timer_label = CustomLabel(
            root, text='0.00', font=('Helvetica', 24))
        self.timer_label.pack()

        self.start_stop_button = tk.Button(
            root,
            text=AppText.START,
            command=self.start_or_stop_timer,
        )
        self.start_stop_button.pack()

        self.reset_button = tk.Button(
            root,
            text=AppText.RESET,
            command=self.reset_timer,
        )
        self.reset_button.pack()

        self.result_label = CustomLabel(root, text='', font=('Helvetica', 16))
        self.result_label.pack()

        # best several high scores
        self.high_score_table = tk.Frame(root, bg=AppColors.BG)
        self.high_score_table.pack()

        for i, high_score in enumerate(self.high_score_manager.high_scores):
            for j, (key, value) in enumerate(high_score.to_dict().items()):
                if i == 0:
                    header = CustomLabel(
                        self.high_score_table,
                        text=key,
                        font=('Helvetica', 16),
                    )
                    header.grid(row=0, column=j)
                cell = CustomLabel(
                    self.high_score_table,
                    text=value,
                    font=('Helvetica', 16),
                )
                cell.grid(row=i + 1, column=j)

    def start_or_stop_timer(self):
        if not self.timer_running:  # if timer is not running, then start the timer
            self.start_timer()
        else:  # if timer is already running, then stop the timer
            self.stop_timer()

    def start_timer(self):
        self.timer_running = True
        self.start_time = time.time()
        self.increment_time()
        self.start_stop_button.config(text=AppText.STOP)
        # Clear the result label when starting the timer
        self.result_label.config(text='')
        # disable the reset button when timer is running
        self.reset_button.config(state=tk.DISABLED)

    def stop_timer(self):
        self.timer_running = False
        self.check_result()
        self.start_stop_button.config(text=AppText.START)
        # enable the reset button when timer is stopped
        self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.time = 0
        self.timer_label.config(text='0.00')
        self.target_time = 5 * random.randint(2, 6)
        self.target_time_label.config(
            text=f'STOP at {self.target_time:.2f} !')
        self.result_label.config(text='')

    def increment_time(self):
        # main loop function of the timer
        if self.timer_running:
            self.time = time.time() - self.start_time
            self.timer_label.config(
                text=f'{self.time:.2f}', fg=get_light_text(self.time, self.target_time))
            # after 10 milliseconds, call this method again
            self.root.after(10, self.increment_time)

    def check_result(self):
        diff = abs(self.target_time - self.time)
        result_text = get_result_text(diff)
        self.timer_label.config(text=f'{self.time:.2f}', fg='#000')
        self.result_label.config(text=result_text)

        # update high score
        self.high_score_manager.update(
            HighScore("player_name", diff))
        self.high_score_manager.save()
