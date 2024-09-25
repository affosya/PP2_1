import itertools

def print_permutations(input_string):
    # Generate all permutations of the input string
    permutations = itertools.permutations(input_string)
    
    # Convert the permutations from tuple form back to strings and print each one
    for perm in permutations:
        print(''.join(perm))

# Example usage:
user_input = input("Enter a string: ")
print("Permutations of the string are:")
print_permutations(user_input)
