"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


#int and str
x = 5
y = "John"
print(type(x))
print(type(y))
"""
output
<class 'int'>
<class 'str'>
"""




#float
x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output 

20.5
<class 'float'>
"""

 #complex
x1 = 1j

#display x:
print(x1)

#display the data type of x:
print(type(x1)) 
"""
#output 
# 1j
# <class 'complex'>
"""
#Tuple
x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
('apple', 'banana', 'cherry')
<class 'tuple'>
"""




#Range
x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
range(0, 6)
<class 'range'>
"""



#Dict
x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
{'name': 'John', 'age': 36}
<class 'dict'>
"""





#set
x = {"cherry", "banana", "apple"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
{'cherry', 'apple', 'banana'}
<class 'set'>
"""





#frozenset
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
frozenset({'cherry', 'banana', 'apple'})
<class 'frozenset'>
"""




#Boolean
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
True
<class 'bool'>
"""





#bytes
x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
b'Hello'
<class 'bytes'>
"""



#bytearray
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output

bytearray(b'\x00\x00\x00\x00\x00')
<class 'bytearray'>

"""




#memoryview
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output
<memory at 0x00A78FA0>
<class 'memoryview'>

"""




#none
x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 
"""
output

None
<class 'NoneType'>
"""


"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""