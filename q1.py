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
        return print("Values not swapped as either/both x and y are not numeric")

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

print("\n---- Task 2 items: -----")
x = "Apple"
y = 10
print(f"Before swap x: {x}")
print(f"Before swap y: {y}")
swap(x, y)

print()

x = 9
y = 17
print(f"Before swap x: {x}")
print(f"Before swap y: {y}")
swap(x, y)
