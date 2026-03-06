import math

def egg_count(display_value) -> int:
    count = 0
    while display_value > 0:
        count += display_value % 2
        display_value = math.floor(display_value / 2)
    return count