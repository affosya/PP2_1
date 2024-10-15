import os

def list_items(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    print("Directories:", directories)
    print("Files:", files)
    print("All items:", os.listdir(path))


path = "./"  
list_items(path)
