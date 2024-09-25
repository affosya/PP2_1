class StringOperations:
    def get_string(self):
        # Get string input from the user
        return input("Enter a string: ")

    def print_string(self, input_string):
        # Print the string in uppercase
        print(input_string.upper())

# Example Usage
string_op = StringOperations()
user_string = string_op.get_string()  # Get user input
string_op.print_string(user_string)  # Print the uppercase string
