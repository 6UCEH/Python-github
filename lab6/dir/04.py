file_path = "/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-2/lab6/dir/01.py"  # Укажите путь к вашему файлу

with open(file_path, "r") as file:
    line_count = sum(1 for _ in file)

print("Number of lines:", line_count)
