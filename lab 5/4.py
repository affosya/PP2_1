import re

def find_upper_followed_by_lower(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

print(find_upper_followed_by_lower("Hello World"))  
