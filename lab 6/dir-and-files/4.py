def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)


filename = "example.txt"  
line_count = count_lines_in_file(filename)
print(f"Number of lines in the file: {line_count}")
