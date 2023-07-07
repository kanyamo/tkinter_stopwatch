from constants import RESULT_THRESHOLDS, AppText, AppColors
import math


def get_result_index(diff):
    for i, threshold in enumerate(RESULT_THRESHOLDS):
        if diff <= threshold:
            return i
    return len(RESULT_THRESHOLDS)


def get_result_text(diff):
    index = get_result_index(diff)
    if index == len(RESULT_THRESHOLDS):
        return f"You were {diff:.2f} seconds off!"
    return AppText.RESULTS[index]


def get_light_text(time, target_time):
    hide_start_time = target_time * 0.2
    hide_duration = 3
    if time <= hide_start_time:
        return AppColors.TEXT
    elif time >= hide_start_time + hide_duration:
        return AppColors.BG
    light_diff = time - hide_start_time
    u = light_diff / hide_duration
    color_hex = math.floor(AppColors.TEXT_HEX * (1-u) + AppColors.BG_HEX * u)
    color = f"#{format(color_hex, 'x').zfill(2) * 3}"
    return color
