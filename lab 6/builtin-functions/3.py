def is_palindrome(string):
    return string == string[::-1]


string = "madam"
result = is_palindrome(string)
print(f"Is '{string}' a palindrome?", result)
