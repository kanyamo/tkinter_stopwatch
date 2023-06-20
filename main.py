import tkinter as tk
import time
from utils import get_result_text


class StopWatchApp:
    def __init__(self, root):
        self.root = root
        self.time = 0
        self.start_time = 0
        self.timer_running = False

        self.label = tk.Label(root, text='0.00', font=('Helvetica', 24))
        self.label.pack()

        self.start_stop_button = tk.Button(
            root, text='Start', command=self.start_or_stop_timer)
        self.start_stop_button.pack()

        self.reset_button = tk.Button(
            root, text='Reset', command=self.reset_timer)
        self.reset_button.pack()

        # New label for displaying the result
        self.result_label = tk.Label(root, text='', font=('Helvetica', 16))
        self.result_label.pack()

    def start_or_stop_timer(self):
        if not self.timer_running:  # if timer is not running, then start the timer
            self.start_timer()
        else:  # if timer is already running, then stop the timer
            self.stop_timer()

    def start_timer(self):
        self.timer_running = True
        self.start_time = time.time()
        self.increment_time()
        self.start_stop_button.config(text='Stop')
        # Clear the result label when starting the timer
        self.result_label.config(text='')

    def stop_timer(self):
        self.timer_running = False
        self.check_result()
        self.start_stop_button.config(text='Start')

    def reset_timer(self):
        self.time = 0
        self.label.config(text='0.00')

    def increment_time(self):
        if self.timer_running:
            self.time = time.time() - self.start_time
            self.label.config(text=f'{self.time:.2f}')
            # after 10 milliseconds, call this method again
            self.root.after(10, self.increment_time)

    def check_result(self):
        diff = abs(10 - self.time)
        result_text = get_result_text(diff)
        self.result_label.config(text=result_text)


root = tk.Tk()
app = StopWatchApp(root)
root.mainloop()
