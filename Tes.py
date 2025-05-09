from collections import Counter

# Given string
text = "Anupam loves python program"

# Step 1: Reverse the string word-wise
reversed_wordwise = ' '.join(text.split()[::-1])

# Step 2: Count characters
char_count = Counter(reversed_wordwise)

# Output
print("Original string:")
print(text)

print("\nWord-wise reversed string:")
print(reversed_wordwise)

print("\nCharacter counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
