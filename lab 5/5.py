import re

def match_a_followed_by_anything_ending_b(string):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, string))

print(match_a_followed_by_anything_ending_b("aXYZb"))  
print(match_a_followed_by_anything_ending_b("abc"))    
