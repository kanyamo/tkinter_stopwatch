from pathlib import Path


class AppColors:
    BG_HEX = 0xec
    BG = f"#{format(BG_HEX, 'x')*3}"
    TEXT_HEX = 0x0
    TEXT = f"#{format(TEXT_HEX, 'x')*3}"
    PRIMARY = "#8BC34A"
    SECONDARY = "#9CCC65"
    ACCENT = "#FF8A65"
    DISABLED = "#BDBDBD"


class AppText:
    TITLE = "Stopwatch"
    START = "START"
    STOP = "STOP"
    RESET = "RESET"
    RESULTS = [
        "Perfect!",
        "Great!",
        "Good!",
        "Not bad!",
        "Keep practicing!",
    ]


class AppSize:
    WIDTH = 400
    HEIGHT = 600


RESULT_THRESHOLDS = [
    0.02,
    0.1,
    0.2,
    0.5,
    1.0,
]

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
ASSET_DIR = BASE_DIR / "assets"
HIGH_SCORE_FILENAME = DATA_DIR / "high_scores.json"
