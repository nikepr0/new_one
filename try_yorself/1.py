#1
print("Hello, World!") 
#----------------------------------
#2
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
 print("Five is greater than two!") 
x = 5
y = "Hello, World!"
#2.2
print("Python is fun!") 
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!") 

print("Hello"); print("How are you?"); print("Bye bye!") 
#----------------------------------
#3
print("Hello World!")
print("Hello World!")
print("I am learning Python.")
print("It is awesome!")
print("This will work!")
print('This will also work!')
print("Hello World!", end=" ")
print("I will print on the same line.")

#3.2
print(3)
print(358)
print(50000)

print(3 + 3)
print(2 * 5)
print("I am", 35, "years old.")
#----------------------------------
#4
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

x = 5
y = "John"
print(type(x))
print(type(y)) 

a = 4
A = "Sally"
#A will not overwrite a 
#4.2
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Camel Case:
#Each word, except the first, starts with a capital letter:
myVariableName = "John"
#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"
#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"
#4.3
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#4.4
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#4.5
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

#----------------------------------

#5
x = "Hello World" 	#str 	
x = 20 	#int 	
x = 20.5 	#float 	
x = 1j 	#complex 	
x = ["apple", "banana", "cherry"]# 	list 	
x = ("apple", "banana", "cherry") #	tuple 	
x = range(6) 	#range 	
x = {"name" : "John", "age" : 36} 	#dict 	
x = {"apple", "banana", "cherry"} 	#set 	
x = frozenset({"apple", "banana", "cherry"}) #	frozenset 	
x = True 	#bool 	
x = b"Hello" 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5))# 	memoryview 	
x = None #    NoneType

#----------------------------------
#6  
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z)) 

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)) 

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z)) 
import random

print(random.randrange(1, 10)) 
#----------------------------------
#7
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

#----------------------------------
#8
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#\' 	Single Quote 	
#\\ 	Backslash 	
#\n 	New Line 	
#\r 	Carriage Return 	
#\t 	Tab 	
#\b 	Backspace 	
#\f 	Form Feed 	
#\ooo 	Octal value 	
#\xhh 	Hex value
