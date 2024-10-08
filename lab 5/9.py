import re

def insert_space_before_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

print(insert_space_before_capitals("HelloWorldExample"))  
