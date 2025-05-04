# def swap_item_positions(d):
#     """
#     Returns a dictionary with reversed item positions.
#     """
#     reversed_items = list(d.items())[::-1]
#     return dict(reversed_items)
#
# # Original dictionary
# d = {
#     "name": "Anupam",
#     "Age": "35",
#     "gender": "Male",
#     "Place": "Bangalore"
# }
#
# print("Original dictionary:")
# print(d)
#
# swapped_dict = swap_item_positions(d)
#
# print("\nDictionary after swapping item positions:")
# print(swapped_dict)
#

# def swap_2nd_and_3rd(d):
#     """
#     Swaps the 2nd and 3rd items in the dictionary `d`.
#     """
#     items = list(d.items())
#     if len(items) >= 3:
#         # Swap the 2nd (index 1) and 3rd (index 2) items
#         items[1], items[2] = items[2], items[1]
#     return dict(items)
#
# # Original dictionary
# dict1 = {
#     "name": "Anupam",
#     "Age": "35",
#     "gender": "Male",
#     "Place": "Bangalore"
# }
#
# print("Original dictionary:")
# print(dict1)
#
# swapped_dict = swap_2nd_and_3rd(dict1)
#
# print("\nDictionary after swapping 2nd and 3rd items:")
# print(swapped_dict)


def swap_items(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]

# Example usage
my_list = [10, 20, 30, 40, 50]
print("Before swapping:", my_list)

# Swap values at index 1 and 3
swap_items(my_list, 1, 3)
print("After swapping:", my_list)
