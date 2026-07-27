def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    counter = 0
    # Validate the list for any non-numbers and omit them from the list, this is more for error exception handling
    validate_lst = [x for x in lst if isinstance(x, (int,float)) and not isinstance(x, bool)]
    
    while counter < len(validate_lst):        
        if validate_lst[counter] < 0:
            print(validate_lst[counter])
            return validate_lst[counter]
        counter +=1
    print("No negatives")
    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

print("\n---- Task 2 items: -----")
lst = [3, 5, -1, 7, -2, 8]
find_first_negative(lst)
print()
lst = [2, 10, 7, 0]
find_first_negative(lst)
