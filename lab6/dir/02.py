import os

path = "/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-2/lab6/dir"

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))
