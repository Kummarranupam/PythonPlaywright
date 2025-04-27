import copy

list1 = [1,3,5,7,9]
list2 = list1.copy()
print(list2)

list2[1]=2
print(list2)
print(list1)

list3 = [4,5,6,7,8]
list4=copy.deepcopy(list3)
#print(list4)
list4[2]=9
print(list4)
print(list3)


#perfect square
def valid_square(num):
    square = int(num**0.5)
    check = square**2==num
    return check

valid_square(10)
# False
valid_square(36)
# True