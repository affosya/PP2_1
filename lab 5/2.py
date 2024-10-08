import re

def match_a_followed_by_2_to_3_b(string):
    pattern = r'ab{2,3}'
    return bool(re.fullmatch(pattern, string))

print(match_a_followed_by_2_to_3_b("abb"))   
print(match_a_followed_by_2_to_3_b("abbbb")) 
