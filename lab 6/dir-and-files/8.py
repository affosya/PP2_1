import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"File {path} has been deleted.")
    else:
        print(f"File {path} does not exist or is not accessible.")


path_to_delete = "file_to_delete.txt"
delete_file(path_to_delete)
