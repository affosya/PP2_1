def copy_file(source, destination):
    with open(source, 'r') as src_file:
        contents = src_file.read()
    
    with open(destination, 'w') as dest_file:
        dest_file.write(contents)


source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
