import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_str)


snake_case = "hello_world_example"
camel_case = snake_to_camel(snake_case)
print(camel_case)
