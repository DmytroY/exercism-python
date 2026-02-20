import math

def square_root(number):
    result = 0
    while(result*result <= number):
        result += 1
    return result - 1
