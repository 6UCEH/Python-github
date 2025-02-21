import re

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower()

camel_case = "ConvertCamelCaseToSnakeCase"
snake_case = camel_to_snake(camel_case)
print(snake_case)
