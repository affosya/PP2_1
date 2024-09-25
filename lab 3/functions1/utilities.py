# utilities.py

def unique_elements(input_list):
    return list(dict.fromkeys(input_list))  # Removes duplicates while preserving order

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Removes spaces and makes lowercase
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)
