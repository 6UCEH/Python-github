def print_permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i+1:]
            print_permutations(remaining, prefix + s[i])

# Пример использования
string = input("Введите строку: ")
print_permutations(string)
