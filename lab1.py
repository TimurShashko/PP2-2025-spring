#home and intro
print("Hello, world!")

#get started
import sys

print(sys.version)

#syntax
if 5 > 2:
  print("Five is greater than two!")

#comments
#This is a comment #this is also a comment

"""
This is a comment
written in
more than just one line
"""

#variables
x = 5
y = "John"
print(x)
print(y)

myvar = "John" #Legal variable names
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#assign values to multiple variables in one line: 
x, y, z = "Orange", "Banana", "Cherry"
a = b = c = "Orange"
print(x + y + z)

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Data types
x = "Hello World"	                #str	
x = 20	                            #int	
x = 20.5	                        #float	
x = 1j	                            #complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	                    #range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                        #bool	
x = b"Hello"	                    #bytes	
x = bytearray(5)	                #bytearray	
x = memoryview(bytes(5))	        #memoryview	
x = None	                        #NoneType



#Python numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#python casting 
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#python strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing Strings
b = "Hello, World!"
print(b[2:5])
#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Modify Strings
#Upper Case
a = "Hello, World!"
print(a.upper())
#Lower Case
a = "Hello, World!"
print(a.lower())
#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#concentrate strings
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Python - Format - Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Escape charachters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#String methods
a = "testik"
a_cap = a.capitalize()
print(a_cap)
