# add: Should be able to add numbers
def add(num1, num2):
    return num1 + num2

# subtract: Should be able to subtract numbers
def subtract(num1, num2):
    return num1 - num2

# multiply: Should be able to multiply with precision
def multiply(num1, num2):
    return num1 * num2

# parse_int: should convert strings to integer numbers
def parse_int(s):
    return int(s)

# add_and_return_2_decimal_places: should return a number value, rounded to 2 decimal places
# Example: 1.23453 + 5.37873 should return 6.61 and the return type should be a number
def add_and_return_2_decimal_places(num1, num2):
    return round(num1 + num2, 2)
