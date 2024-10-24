def fizz_buzz(num):
    # Check if num is either an integer or a float
    if type(num) not in [int, float]:
        return False

    # Apply the fizzbuzz logic
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num
