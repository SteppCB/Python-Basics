# IndexOf: Find the index of a specified item in a list
def index_of(arr, item):
    return arr.index(item)

# Sum: Calculate the sum of all items in a list
def sum_list(arr):
    return sum(arr)

# Filter: Remove all instances of a specified item from a list
def filter_out(arr, item):
    return [x for x in arr if x != item]

# Append: Add an item to the end of a list
def append(arr, item):
    arr.append(item)
    return arr

# Truncate: Remove the last item from a list
def truncate(arr):
    arr.pop()
    return arr

# Concat: Join two lists together
def concat(arr1, arr2):
    return arr1 + arr2

# Insert: Insert an item at a specified index in a list
def insert(arr, item, index):
    arr.insert(index, item)
    return arr

# Square: Square each number in a list
def square(arr):
    return list(map(lambda x: x**2, arr))

# Example usage
arr = [1, 2, 3, 5, 6]
arr_example = [1, 2, 3]
filter_arr = [1, 2, 3, 5, 6, 2, 4, 2]
square_arr = [1, 2, 4, 5]
