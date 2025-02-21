import re

pattern = r'ab{2,3}'

test_strings = ["abb", "abbb", "a", "ab", "abbbb", "abc", "aabb"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")
