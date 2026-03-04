col_dict = {
    "black":  [0, ""],
    "brown":  [1, "±1%"],
    "red":    [2, "±2%"],
    "orange": [3, ""],
    "yellow": [4, ""],
    "green":  [5, "±0.5%"],
    "blue":   [6, "±0.25%"],
    "violet": [7, "±0.1%"],
    "grey":   [8, "±0.05%"],
    "white":  [9, ""],
    "gold":   [-1, "±5%"],
    "silver": [-1, "±10%"],
}

def resistor_label(colors) -> str:
    if colors == ["black"]:
        return "0 ohms"

    r = 0
    for item in colors[0:-2]:
        r = 10 * r + col_dict.get(item)[0]
    
    r = r * pow(10, col_dict.get(colors[-2])[0])

    if r < 1000:
        return f"{r:g} ohms {col_dict.get(colors[-1])[1]}"
    
    if r < 1000000:
        return f"{r/1000:g} kiloohms {col_dict.get(colors[-1])[1]}"
    
    return f"{r/1000000:g} megaohms {col_dict.get(colors[-1])[1]}"
