import re

def match_ab_zero_or_more_b(s):
    pattern = r'^ab*$'
    return bool(re.match(pattern, s))


print(match_ab_zero_or_more_b("a"))      
print(match_ab_zero_or_more_b("ab"))     
print(match_ab_zero_or_more_b("abb"))    
print(match_ab_zero_or_more_b("abc"))    
