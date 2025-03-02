def is_palindrome(s):
    s = "".join(filter(str.isalnum, s)).lower()  
    return s == s[::-1]  

text = "A man, a plan, a canal, Panama!"
print(is_palindrome(text))  # Вывод: True
