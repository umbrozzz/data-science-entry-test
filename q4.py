def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    print(f"Your input captured: {s}, reversing it now....")
    # reverse string - using Slicing function in python --> print(s[::-1]) and hold value in variable
    reversed_str = s[::-1]
    print(f"Reversed string: {reversed_str}")
    return reversed_str
    
s = input("Please input string to reverse: ")

string_reverse(s)

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print ("\n---- Task 2 items: -----")
string_reverse("Hello World")
string_reverse("Python")
