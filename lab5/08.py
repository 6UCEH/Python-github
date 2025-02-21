import re

text = "HelloWorldExample"
result = re.split(r'(?=[A-Z])', text)

print(result)
