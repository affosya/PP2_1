# main.py

# Importing functions from utilities.py
from functions1.utilities import unique_elements, is_palindrome, histogram

# Using the unique_elements function
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", unique_elements(my_list))

# Using the is_palindrome function
word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

# Using the histogram function
histogram([4, 7, 5])
