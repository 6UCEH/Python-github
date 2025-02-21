import re

pattern = r'a.*b$'

test_strings = ["ab", "a123b", "axb", "a_b", "abc", "bca", "aanythingb"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match")
