from constants import RESULT_TEXT_THRESHOLDS


def get_result_text(diff):
    for threshold, text in RESULT_TEXT_THRESHOLDS:
        if diff <= threshold:
            return f"Result: {text}"
    return f"Result: You were {diff:.2f} seconds off"
