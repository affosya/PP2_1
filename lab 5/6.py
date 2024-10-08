import re

def replace_space_comma_dot_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

print(replace_space_comma_dot_with_colon("Hello, World. How are you?"))  

