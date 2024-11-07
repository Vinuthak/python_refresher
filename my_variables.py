"""
    python creates a value ad store it somewhere then name it..
    right side happens first and then name it(variable)
    A Var is created the moment a value is assigned

"""
#many values to multiple values.
x,y,z = "Orange","Banana", "Cherry"
print(x)
print(y)
print(z)
#unpack a collection
#If you have a collection of values in a list,tuple etc,
# Python allows you to extract the values into variables.This is called unpacking.
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
print("Hello","World")#output is Hello World

#Global variables
x = "Awesome"
def myfun():
    print("Python is " + x)
myfun()
#Create a variable inside a funct with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)