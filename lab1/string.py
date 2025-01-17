a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])   #exactly like in c++ out-e


for x in "banana":
  print(x) 
  """
output
b 
a
n
a
n
a  
  """


a = "Hello, World!"
print(len(a))
#output - 13 
#because it count every symbol even space and enter




#bool
txt = "The best things in life are free!"
print("free" in txt)#find word free in srt 'txt'
#output - true
 #or another way how we can do it 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #its output


  #negative
txt = "The best things in life are free!"
print("expensive" not in txt)
#output- true

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")




#range
b = "Ertai Bisen!"
print(b[2:5]) #but it dont get last element for example in this case 5
#tai


b = "Hello, World!"
print(b[:5])
#Hello


b = "Hello, World!"
print(b[2:])
#llo, World!



b = "Hello, World!"
print(b[-5:-2])
#count from behind of string




a = "Hello, World!"
print(a.upper())#capital letters
#HELLO, WORLD!


a = "Hello, World!"
print(a.lower())#only lower letters
#hello, world!


a = " Hello, World! "   #remove this space of both sides
print(a.strip())
#Hello, World!



a = "Hello, World!"
print(a.replace("H", "J"))#replace letter by order
#Jello, World


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']



a = "Hello"
b = "World"
c = a + b
print(c)
#HelloWorld


a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World



#F strings


age = 36
txt = f"My name is John, I am {age}"
print(txt)
#My name is John, I am 36


price = 59
txt = f"The price is {price:.2f} dollars"  #float
print(txt)
#The price is 59.00 dollars



txt = f"The price is {20 * 59} dollars"
print(txt)
#The price is 1180 dollars



txt = "We are the so-called \"Vikings\" from the north." #double scoupes
print(txt) 
#We are the so-called "Vikings" from the north.


txt = 'It\'s alright.'
print(txt) 
#It's alright.

txt = "This will insert one \\ (backslash)."
print(txt) 
#This will insert one \ (backslash).


txt = "Hello\nWorld!"#new line like endl in c++
print(txt) 
#Hello
#World!

txt = "Hello\rWorld!"
print(txt) 
#Hello
#World!



txt = "Hello\tWorld!" #tab(3 spaces)
print(txt) 
#Hello   World!


#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#HelloWorld!


"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""