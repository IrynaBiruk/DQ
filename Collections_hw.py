
import random
import string

# Step 1: Create a list of random number of dictionaries
num_dicts = random.randint(2, 10)  # Random number of dictionaries between 2 and 10
list_of_dicts = []  # Initialize an empty list to store the dictionaries

for i in range(num_dicts):
    num_keys = random.randint(1, 5)  # Random number of keys per dictionary (1 to 5 for simplicity)
    keys = random.sample(string.ascii_lowercase, num_keys)  # Random unique keys from a-z
    dict_values = {key: random.randint(0, 100) for key in keys}  # Assign random values (0-100) to keys
    list_of_dicts.append(dict_values)  # Append the dictionary to the list

# Step 2: Combine the dictionaries into one common dictionary
common_dict = {}  # Initialize an empty dictionary to store the combined results

for idx, d in enumerate(list_of_dicts):
    for key, value in d.items():
        # Create a unique key by appending the index of the dictionary if the key already exists
        if key in common_dict:
            # If the current value is greater than the stored value, update it
            if value > common_dict[key][0]:
                common_dict[key] = (value, idx + 1)
        else:
            # Store the value and the index of the dictionary where it came from
            common_dict[key] = (value, idx + 1)

# Format the keys based on whether they appear in multiple dictionaries or not
final_dict = {f"{key}_{val[1]}" if list_of_dicts.count(key) > 1 else key: val[0] for key, val in common_dict.items()}

# Print the generated list of dictionaries and the final combined dictionary
print("List of dictionaries:", list_of_dicts)
print("Combined dictionary:", final_dict)
