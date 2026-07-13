def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    print(f"Your input captured: {s}, reversing it now....")
    # reverse - using Slicing function in python --> print(s[::-1])
    print(f"Reversed string: {s[::-1]}") 
    return s

s = input("Please input string to reverse: ")

string_reverse(s)


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
