def count_case(s):
    upper_count = sum(map(str.isupper, s)) 
    lower_count = sum(map(str.islower, s))  
    
    return upper_count, lower_count


text = "Hello World!"
upper, lower = count_case(text)
print("Upper case letters:", upper)  # Вывод: 2
print("Lower case letters:", lower)  # Вывод: 8
