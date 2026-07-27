def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """   
    # Check if key exist in dct, if so, capture the original value
    if key in dct:
        print(f"Key exist, original value for '{key}': {dct[key]}")
        
    # Update key = value pairing if exist or add it if it does not exist
    dct[key] = value
    print(f"New value for '{key}': {dct[key]}")
    
    # Return updated dictionary
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print ("\n---- Task 2 items: -----")

update_dictionary({}, "name", "Alice")
print()
update_dictionary({"age": 25}, "age", 26)
