name = "Alice"
age = 30
# print("Name:", name, "Age:", age)

# The code assigns values to variables name and age, then prints them with labels.

#  Using sep and end parameter

# print("Pythn",end="#")
# print("ayo")
# print(print('09', '12', '2016', sep='-'))

# Python@GeeksforGeeks
# GFG
# 09-12-2016
# pratik@geeksforgeeks

name = 'Tushar'
age = 23
# print(f"Hello, My name is {name} and I'm {age} years old.")

# Hello, My name is Tushar and I'm 23 years old.
try:
    x, y = input("Enter two values: ").split()
    print("Number of boys: ", x)
    print("Number of girls: ", y)
except:
    print("Invalid input")

a = True
b = False
# print(a and b)
"""
.upper() #HELLO
.lower() #hello
.capitalize() #Hello
.count("ll") #1
"""

x = "hello"
y = 3

print(x * y) 
# hellohellohello

x = "jelo"
y = "wpordf"
print(x+y) #concatination

"""
>
<
<=
>=
==
!=
conditional operator
"""

"""
list: [1,"acb",12.4]
l = [4, True, "hi"]
len(l) #get the length of the list
l.append("any value")   #append the value at the end of the list
l.extend([4,5,6,324,23]) 
l.(pop)     # pop out last element
l.(pop(0))     # pop out 0th element
"""



"""
for i in range(10):
    print(i)
start,stop,step
by default its stop if we put one input
2 input means start and stop
3 input means start,stop,step
for i in range(10,-1,01)

can iterate through list,tuples and the dictonary
"""

x = [3,4,5,32,12,3]

for i in range(len(x)):
    print(x[i])

i = 0

while True:
    print("run")
    i += 1
    if(i == 10):
        break


x = {"key1":12,"key2":123}
for key,value in x.items():
    print(key,value,end=" ")

# when we iterate the dictionary with just i in range type, we get key values only
# to get both key and value, we need to use .items() to get the key value pair

#UNPACK operators

def func(x):
    def func2(y):
        print(x)
        print(y)
    
    return func2

print(func(3)(4))

x = "tim"

def func(name):
    global x
    x = name

print(x) # prints nothing
print(func("tim")) # prints tim
print(x) # prints tim
# the global keyword is used to declare that the variable is global and can be accessed from any where

try:
    x = 5 / 0
except Exception as e:
    print(e)
finally:
    print("this will run no matter what") # this will run no matter what
    # the finally block is used to run the code no matter what happens in the try block

#lambda
#lambda is a small anonymous function that can take any number of arguments but can only have one expression
# it is used to define small functions
#lambda functions are used when we need to pass a function as an argument to another function or when
# we need to return a function from a function

x = lambda x,y: x+y

print(x(0,12))


#map and filter
#map is used to apply a function to each item in an iterable
#filter is used to filter items from an iterable based on a condition
#map and filter return map object and filter object respectively which can be converted to list using list()
#map and filter are used to apply a function to each item in an iterable and filter items from
#an iterable based on a condition respectively

x = [1,2,4,5,6,1,12,534,123,432,12,32,543,12,645,97,0,45]
#map
#mapping take two parameters, first is the function where we can have a object
# and the second is on which we are applying that condiition

mp = map(lambda i: i * 10,x);
mp2 = map(lambda i: i % 10 == 2,x);

print(list(mp));

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
        #match is used to check the value of a variable and execute a block of code if the value
        # matches the specified value
        #match is used to check the value of a variable and execute a block of code if the
        # value matches the specified value