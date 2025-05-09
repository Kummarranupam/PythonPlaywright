dict1 = {"name": "Anupam", "Age": "35", "gender": "Male", "Place": "Bangalore"}

# Convert to a list of items
items = list(dict1.items())

# Find indexes of "Age" and "gender"
age_index = next(i for i, (k, _) in enumerate(items) if k == "Age")
gender_index = next(i for i, (k, _) in enumerate(items) if k == "gender")

# Swap the items at those positions
items[age_index], items[gender_index] = items[gender_index], items[age_index]

# Rebuild the dictionary with new order
swapped_dict = dict(items)

print("Original Dictionary:", dict1)
print("Swapped Dictionary:", swapped_dict)