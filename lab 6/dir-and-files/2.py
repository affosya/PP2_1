import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    print(f"Path exists: {exists}")
    print(f"Path is readable: {readable}")
    print(f"Path is writable: {writable}")
    print(f"Path is executable: {executable}")


path = "./example.txt"  
check_access(path)
