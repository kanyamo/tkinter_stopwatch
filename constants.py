from pathlib import Path


class AppText:
    TITLE = "Stopwatch"
    START = "START"
    STOP = "STOP"
    RESET = "RESET"


RESULT_TEXT_THRESHOLDS = [
    (0.02, "Perfect!"),
    (0.1, "Great!"),
    (0.2, "Good!"),
    (0.5, "Not bad!"),
    (1.0, "Keep practicing!"),
]

DATA_DIR = Path(__file__).parent / "data"
HIGH_SCORE_FILENAME = DATA_DIR / "high_scores.json"
