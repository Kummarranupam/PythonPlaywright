# Program to reverse a string

# strng = "Anupam Kumar"
# strng1=strng[::-1]
# print(strng1)
#
# strng = "Anupam Kumar"
# strng2=strng.split()
# reverse = " ".join(strng2[::-1])
# print(reverse)

# Program to check string is Palindrome(front=back)

str = "radara"
if str ==str[::-1]:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")

#program to create Fibonacci series under range -10

def fibo(n):
    a,b =0,1
    for _ in range(n):
        print(a,end=" ")
        a,b = b,a+b
fibo(10)

#program to create Fibonacci series under range -10 and output in list
def fibo_list(m):
    a, b = 0, 1
    result = []
    for _ in range(m):
        result.append(a)
        a, b = b, a + b
    return result

print(fibo_list(10))

# Program for Factorial(5*4*3*2*1)
def factorial(n):
    if n ==0:
        return  1
    return n* factorial(n-1)
print(factorial(5))

#Program to check Prime number

num = int(input("enter the number:"))
flag =0
for i in range(2,num):
    if num %i==0:
        flag=1
        break
if flag==1:
    print("Not Prime")
else:
    print("Prime")

def is_prime(num):
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is prime
    if num == 2:
        return True

    # check if num is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False
        # if num is not divisible by any number from 2 to num-1, then it is prime
        else:
            return True

print(is_prime(8))  # Returns False
print(is_prime(131))


# Program to return max and min from list

#Program to remove duplicates from list
def remove_duplicates(lst):
    # create an empty set to store unique elements
    # sets only store unique elements, so duplicates will be automatically removed
    new_set = set()

    # loop through the list, adding each element to the set
      for item in lst:
        new_set.add(item)

    # convert the set back to a list
    return list(new_set)

# For example
lst = [1, 2, 3, 2, 1, 4, 5, 3, 6]
new_lst = remove_duplicates(lst)
print("Original list:", lst)
print("List with duplicates removed:", new_lst)



# Write a Python Function That Counts the Number of Vowels in a String
def count_vowels(string):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    # Initialize a counter for vowels
    vowel_count = 0
    # Iterate over each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in vowels:
            # If char is a vowel, increment the vowel count
            vowel_count += 1
    # Return the total number of vowels
    return vowel_count

# Test the function
string = input("Enter a string: ")
print("The number of vowels is:", count_vowels(string))

Fibonacci
def fibonacci_sequence(num):
    # Check if num input is 0 or 1
    if num == 0:
        # return empty list
        return []
    elif num == 1:
        # return 0
        return [0]
    # Initialize the sequence with the first two numbers
    sequence = [0, 1]
    # Append new numbers to the sequence until it has num terms
    while len(sequence) < num:
        # Calculate the next number as the sum of the previous two numbers
        next_num = sequence[-1] + sequence[-2]
        # Append the next number to the sequence
        sequence.append(next_num)
    # Return the complete sequence
    return sequence

# Test the function
n = int(input("Enter the number of terms: "))
print("The Fibonacci sequence:", fibonacci_sequence(n))