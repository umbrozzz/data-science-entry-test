def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input provided must be a list")
    else:
        print(f"Original list: {lst}")
        new_lst = [replace_val if x == find_val else x for x in lst]
        print(f"Finding and replacing {find_val} with {replace_val}")
        print(f"Modified list: {new_lst}")
    return new_lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


print("\n---- Task 2 items: -----")
find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print()
find_and_replace(["apple", "banana", "apple"], "apple", "orange")
