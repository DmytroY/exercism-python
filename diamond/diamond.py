def rows(letter) -> list:
    n = ord(letter) - ord('A')
    len = 2 * n + 1

    result = []

    for i in range(0, n):
        result.append(make_row(i, len))
    
    for i in range(n, -1, -1):
        result.append(make_row(i, len))

    return result

def make_row(i, len) -> str:
    row = ""
    for j in range(1, len + 1):
        if (j == (len + 1)/2 + i or j == (len + 1)/2 - i):
            row += chr(ord('A') + i)
        else:
            row +=" "
    return row
