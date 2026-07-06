def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return y,x
    
print ("Please input a numeric value of x")
x = input()
print ("Please input a numeric value of y")
y = input()

if x.isnumeric() and y.isnumeric():
   print("x and y are numeric, swapping values now")
   x, y = swap(x,y)
   print(f"The value of x is now = {x} and the value of y is now = {y}")
elif (x.isnumeric() or y.isnumeric()):
    print("Either x or y is numberic, returning value -1")
else:
    print("x and y are not numeric, returning value -1")
