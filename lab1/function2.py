def myfunc():
  global x #save in data not only in function
  x = "fantastic"

myfunc()

print("Python is " + x)