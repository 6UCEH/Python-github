import os

path = "/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-2/lab6/dir"

if os.path.exists(path):
    print("Path exists!")
    print("Directory:", os.path.dirname(path))
    print("Filename:", os.path.basename(path))
else:
    print("Path does not exist!")
