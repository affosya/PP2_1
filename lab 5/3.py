import re

def find_lowercase_with_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

print(find_lowercase_with_underscore("abc_def ghi_jkl")) 
