import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print("Directory part:", os.path.dirname(path))
        print("File part:", os.path.basename(path))
    else:
        print(f"Path does not exist: {path}")


path = "./example.txt"  
check_path(path)
