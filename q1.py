def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        x, y = y, x
        print(f"Both x and y are numeric, swapping values now")
        print(f"The value of x is now = {x} and the value of y is now = {y}")
        return x, y
    else:
        return -1

# Prompt for user's input
print("Please input a numeric value of x")
x_userinput = input()
print("Please input a numeric value of y")
y_userinput = input()

# Convert user input of value x and y to numeric
try:
    x = float(x_userinput)
    y = float(y_userinput)

# Error handling if user input value of x and y failed to convert to numeric
except ValueError:
    x = x_userinput
    y = y_userinput

# Trigger function call
output = swap(x, y)

# Handling if the output is -1
if output == -1:
    print("x and/or y are not numeric, returning value -1")
