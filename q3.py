import json
import os

FILE_NAME = "q3database.json"

# 1. Load existing data if the file exists; otherwise start empty
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        dct = json.load(file)
else:
    dct = {}

# 2. Script

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
    
    # Return updated dictionary
    return dct

# Prompt user to input the key and value
key = input("Input Key: ")
value = input("Input Value: ")

update_dictionary(dct, key, value)

# output the updated dictionary
print(dct)

# 3. Save the dictionary to the hard drive before the program exits
with open(FILE_NAME, "w") as file:
    json.dump(dct, file, indent=4)


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
