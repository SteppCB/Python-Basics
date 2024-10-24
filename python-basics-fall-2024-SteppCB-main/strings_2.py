# reverse_string: you should be able to reverse a string
# Example: "abc" => "cba"
def reverse_string(s):
    return s[::-1]  # Reverses the string using slicing

# capitalize: should return the input in all-caps
# Example: "this is a string" => "THIS IS A STRING"
def capitalize(s):
    return s.upper()  # Converts the string to uppercase

# split_string: should divide a string into substrings and return a list
# Example: "Jane, Doe, 21" => ["Jane", "Doe", "21"]
def split_string(s, splitAt=','):
    return s.split(splitAt)  # Splits the string at the given delimiter
