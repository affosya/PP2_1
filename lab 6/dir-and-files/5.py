def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")


data = ["Item 1", "Item 2", "Item 3"]
filename = "output.txt"
write_list_to_file(filename, data)
