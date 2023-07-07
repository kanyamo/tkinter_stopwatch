import tkinter as tk
from tkinter import messagebox
import time
from utils import get_result_index, get_light_text, get_result_text
from constants import AppText, AppColors, AppSize, ASSET_DIR
import random
from high_score import HighScoreManager, HighScore
from widgets import CustomLabel, CustomButton
try:
    from pygame import mixer
except ImportError:
    answer = messagebox.askyesno(
        "Import Error",
        "Pygame is not installed. Do you want to install it now?"
    )
    if answer:
        import os
        os.system('pip install -r requirements.txt')
        from pygame import mixer
    else:
        exit()


class StopWatchApp:
    def __init__(self, root: tk.Tk):
        # root configuration
        self.root = root
        self.root.title(AppText.TITLE)
        self.root.geometry(f'{AppSize.WIDTH}x{AppSize.HEIGHT}')
        self.root.minsize(AppSize.WIDTH, AppSize.HEIGHT)
        self.root.configure(bg=AppColors.BG)
        self.root.grid_columnconfigure(0, weight=1)
        for i in range(2):
            self.root.grid_rowconfigure(i, weight=1)

        # initialize the state of the app
        self.time = 0
        self.start_time = 0
        self.timer_running = False
        # time that player should stop the timer
        self.target_time = 2 * random.randint(5, 10)

        # load sound
        mixer.init()
        self.start_sound = mixer.Sound(ASSET_DIR / "se" / "perfect.wav")
        self.click_sound = mixer.Sound(ASSET_DIR / "se" / "click.wav")
        self.running_sound = mixer.Sound(ASSET_DIR / "se" / "running.wav")
        self.running_sound.set_volume(0.5)
        self.result_sounds = [
            mixer.Sound(ASSET_DIR / "se" / "perfect.wav"),
            mixer.Sound(ASSET_DIR / "se" / "great.wav"),
            mixer.Sound(ASSET_DIR / "se" / "good.wav"),
            mixer.Sound(ASSET_DIR / "se" / "bad.wav"),
            mixer.Sound(ASSET_DIR / "se" / "bad.wav"),
            self.click_sound,
        ]

        # load high score
        self.high_score_manager = HighScoreManager()
        self.high_score_manager.load()

        # initialize the widgets
        self.timer_container = tk.Frame(root, bg=AppColors.BG)
        self.timer_container.grid(row=0, column=0, padx=10, pady=10)

        self.target_time_label = CustomLabel(
            self.timer_container,
            text=f'STOP at {self.target_time:.2f} !',
            font=('Helvetica', 16),
        )
        self.target_time_label.pack()

        self.timer_label = CustomLabel(
            self.timer_container, text='0.00', font=('Helvetica', 36))
        self.timer_label.pack()

        self.button_container = tk.Frame(self.timer_container, bg=AppColors.BG)
        self.button_container.pack()

        self.start_stop_button = CustomButton(
            self.button_container,
            text=AppText.START,
        )
        self.start_stop_button.bind('<Button-1>', self.start_or_stop_timer)
        self.start_stop_button.grid(row=0, column=0, padx=10, pady=10)

        self.reset_button = CustomButton(
            self.button_container,
            text=AppText.RESET,
            bg=AppColors.ACCENT,
            activebackground=AppColors.ACCENT,
            command=self.reset_timer,
        )
        self.reset_button.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = CustomLabel(
            self.timer_container, text='', font=('Helvetica', 16))
        self.result_label.pack()

        # best several high scores
        self.high_score_table = tk.Frame(root, bg=AppColors.BG)
        self.high_score_table.grid(row=1, column=0, padx=10, pady=10)

        for i, high_score in enumerate(self.high_score_manager.high_scores):
            for j, (key, value) in enumerate(
                {"rank": i + 1, **high_score.to_dict()}.items()
            ):
                # dont display the player name in the table
                if key == "name":
                    continue
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

    def start_or_stop_timer(self, _):
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
        self.reset_button.config(state=tk.DISABLED, bg=AppColors.DISABLED)
        self.start_sound.play()
        self.running_sound.play(-1)

    def stop_timer(self):
        self.timer_running = False
        self.check_result()
        self.start_stop_button.config(text=AppText.START)
        # enable the reset button when timer is stopped
        self.reset_button.config(state=tk.NORMAL, bg=AppColors.ACCENT)
        self.running_sound.stop()

    def reset_timer(self):
        self.time = 0
        self.timer_label.config(text='0.00')
        self.target_time = 2 * random.randint(5, 10)
        self.target_time_label.config(
            text=f'STOP at {self.target_time:.2f} !')
        self.result_label.config(text='')
        self.click_sound.play()

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
        index = get_result_index(diff)
        result_text = get_result_text(diff)
        self.timer_label.config(text=f'{self.time:.2f}', fg='#000')
        self.result_label.config(text=result_text)
        self.result_sounds[index].play()

        # update high score
        self.high_score_manager.update(
            HighScore("player_name", diff))
        self.high_score_manager.save()
