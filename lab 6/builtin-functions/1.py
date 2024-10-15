from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4]
result = multiply_list(numbers)
print("Product of numbers:", result)
