RESULT_TEXT_THRESHOLDS = [
    (0.02, "Perfect!"),
    (0.1, "Great!"),
    (0.2, "Good!"),
    (0.5, "Not bad!"),
    (1.0, "Keep practicing!"),
]


def get_result_text(diff):
    for threshold, text in RESULT_TEXT_THRESHOLDS:
        if diff <= threshold:
            return f"Result: {text}"
    return f"Result: You were {diff:.2f} seconds off"
