# tkinter_stopwatch

## install

Currently, this application has no dependencies other than the standard library.

```
git clone https://github.com/kanyamo/tkinter_stopwatch.git
cd tkinter_stopwatch
```

## run

```
python main.py
```


# Abstract
This is a game to stop the timer perfectly at a certain fixed time. Specifically, the game will be created using the python tkinter module.
The game is played to see how close you can press the stopwatch to a certain time.

# The Rules of Game
The rules are simple. First, when you start the game, the time is displayed. This is the time you should just stop. When the game is displayed, you press the START button to start the counter. 
At that time, the counter will tick the time, but the counter will be hidden in the middle of the game, making it difficult to stop at exactly the right time.
When you think it is just time, press the STOP button to stop the counter; when
you press the STOP button, the time will be displayed, showing the time from when
you press the START button to when you press the STOP button.
Depending on the difference between this time and the specified time, a message will be displayed from highest rating to lowest one: Perfect, Great, Good, Not bad, Keep Practicing”. 
It is extremely difficult to display the message ”Perfect”.
You can also change the target time and start the counter from the beginning by pressing the RESET button.
Please try your best to display a message with a higher rating!

# GUI
This application includes the following GUI elements:
- Rule display text
- Time you should just stop
- Start and stop buttons
- Reset button
- Timer
- Result
- High score

Due to the nature of the game, the timer is not displayed after a certain time determined by the target time. Results will be displayed after the stop button is pressed.
