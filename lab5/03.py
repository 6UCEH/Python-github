import re

pattern = r'[a-z]+_[a-z]+'

test_strings = ["hello_world", "test_case", "Python_program", "helloWorld", "abc_def_ghi", "no_underscore"]

for string in test_strings:
    if re.search(pattern, string):
        print(f"'{string}' contains a match")
    else:
        print(f"'{string}' does not match")
