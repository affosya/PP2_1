def count_case_letters(string):
    upper_case = sum(1 for c in string if c.isupper())
    lower_case = sum(1 for c in string if c.islower())
    return upper_case, lower_case

string = "Hello World!"
upper, lower = count_case_letters(string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
