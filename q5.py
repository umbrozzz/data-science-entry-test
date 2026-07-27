def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    if isinstance(num, (int,float)) and isinstance (divisor, (int,float)):
        if num % divisor == 0:
            print(f"True, {num} is divisible by {divisor}")
            return True
        else:
            print(f"False, {num} is not divisible by {divisor}")
            return False
    else:
        print("Either num or divisor is not numeric, Please try again.")
    return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print("\n---- Task 2 items: -----")
check_divisibility(10,2)
print()
check_divisibility(7,3)
