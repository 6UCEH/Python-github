def all_elements_true(tup):
    return all(tup)  

tup = (True, 1, "Hello")  
print(all_elements_true(tup))  

tup2 = (True, 0, "Hello")  
print(all_elements_true(tup2))  
