def all_true(tup):
    return all(tup)


tup = (True, True, False)
result = all_true(tup)
print("Are all elements true?", result)
