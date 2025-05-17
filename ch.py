rows = 5  # Number of rows in the pattern

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")  # Print spaces for alignment
    for j in range(i + 1):
        if j == 0 or j == i or i == rows - 1:
            print("* ", end="")  # Print '*' at appropriate places
        else:
            print("  ", end="")  # Print spaces in the middle
    print()  # Move to the next line


def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))


