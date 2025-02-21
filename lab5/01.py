import re

pattern = r'ab*'

test_strings = ["a", "ab", "abb", "b", "abc", "aabb", ""]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")
