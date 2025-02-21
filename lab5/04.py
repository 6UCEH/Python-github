import re

pattern = r'[A-Z][a-z]+'

test_strings = ["Hello", "World", "Python", "UPPER", "lower", "CamelCase", "A", "Zebra"]

for string in test_strings:
    if re.search(pattern, string):
        print(f"'{string}' contains a match")
    else:
        print(f"'{string}' does not match")
