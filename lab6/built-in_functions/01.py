def multiply_list(numbers):
    it = iter(numbers)  
    result = next(it, 1)  
    
    for num in it:
        result *= num  
        
    return result


nums = [2, 3, 4, 5]
print("Product of list:", multiply_list(nums))  # Вывод: 120
