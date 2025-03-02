import os

file_path = "/Users/bisert/Desktop/2SEM/PP2/Python-github/Python-github-2/A1.txt"


if os.path.exists(file_path):

    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"Файл '{file_path}' удалён.")
    else:
        print(f"Ошибка: Нет прав для удаления '{file_path}'.")
else:
    print(f"Ошибка: Файл '{file_path}' не существует.")
