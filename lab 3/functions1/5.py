def reverse_words(input_string):
    # Split the input string into words
    words = input_string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage:
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed sentence:", result)
