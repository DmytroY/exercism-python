verses = (
    "",
    "and a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
    )

days = (
    "",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)

def helper(n) -> str:
    result = "On the " + days[n] + " day of Christmas my true love gave to me: "
    if n == 1:
        return result + "a Partridge in a Pear Tree."
    
    for i in range(n, 0, -1):
        print(i)
        result += verses[i]

    return result

def recite(start, end) -> list:
    result = []
    for i in range(start, end +1):
        result.append(helper(i))
    return result