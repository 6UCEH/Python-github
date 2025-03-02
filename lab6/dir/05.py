my_list = ["Apple", "Banana", "Cherry", "Date"]

file_path = "/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-2/lab6/dir/example_05.txt"

with open(file_path, "w") as file:
    for item in my_list:
        file.write(item + "\n")

print("List has been written to", file_path)
