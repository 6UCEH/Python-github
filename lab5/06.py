import re

pattern = r'[ ,.]'
replacement = ':'

text = "Hello, world. This is a test string."

result = re.sub(pattern, replacement, text)

print(result)
