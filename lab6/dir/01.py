import os

path = "/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-2/lab6/dir"
items = os.listdir(path)

print("Directories:", [d for d in items if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in items if os.path.isfile(os.path.join(path, f))])
print("All items:", items)