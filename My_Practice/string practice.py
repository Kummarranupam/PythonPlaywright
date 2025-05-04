# a ='''I am a
# Man and live
# in Bangalore'''
# print(a)
#
# b= ('I am  sam\n'
#     'I am nam\n'
#     'I am tiku')
# print(b)




# my_list = [3, 1, 4, 1, 5]
#
# my_list.sort()
# print(my_list)

# my_list = [3, 1, 4, 1, 5]
# new_list = sorted(my_list)
# print(new_list)  # Output: [1, 1, 3, 4, 5]
# print(my_list)   # Output: [3, 1, 4, 1, 5]

import copy

# original = [[1, 2], [3, 4]]
# shallow = copy.copy(original)
#
# shallow[0][0] = 999
# print(original)
# print(shallow)
#
# original = [[1, 2], [3, 4]]
# deep = copy.deepcopy(original)
#
# deep[0][0] = 999
# print(original)  # [[1, 2], [3, 4]] — unaffected
# print(deep)


str = "I go to school everyday"
str2 = str.split()
for i in str2:
    if i == "school":
        print("The string is present:", i)
