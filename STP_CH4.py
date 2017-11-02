#Defining a function
#function syntax. no caps and underscores between words
def f(x):
    return x*2

result = f(2)
print(result)
print(f(2)-1)

def f():
    return 2

result = f()
print(result)

def f(x, y, z):
    return (x+y+z)

result = f(2,3,4)
print(result)

#Built-in functions
print(len("Colorado"))

print(str(100))
print(int("1"))
print(float(100))

# age = input("How old are you?")
age = "44"
int_age = int(age)
if int_age <= 44:
    print(int_age,"! Spring chicken!")
else:
    print(int_age, "! Don't buy the big jar of mayo!")

#Reusing functions
def even_odd(x):
    if x % 2 == 0:
        print("Even Steven!")
    else:
        print("Odd Todd!")

even_odd(2)
even_odd(3)

# Required and default parameters
def f(x=2):
    return x**x

print(f())
for i in range(3,7):
    print(f(i))

#Excepion handling
a = 5
b = 0
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero")

try:
    b = int("Hundo")
except ValueError:
    print("b should be a number")

#Docstrings. when parameters need to be a particular type
def add(x,y):
    """
    Returns x + y
    :param x: int
    :param y: int
    :return: int sum of x andy
    """
    return(x+y)

#Challenge 1. Define a function that squares a number
def square_it(x=44):
    """
    Rertuns x ** 2
    :param x: int
    :return: x squared
    """
    return x**2

print(square_it())

#Challenge 2. Define a function that accepts a string as a parameter and prints it
def write(x):
    """
    Returns none. Output string
    :param x: any
    :return: none
    """
    print(x)

write("Colorado")

#Challenge 3. Write a function with 1 required parapmeter and 2 optional
def product(x,y=2,z=4):
    """
    Returns x * y * z
    :param x: int
    :param y: int
    :param z: int
    :return: product of x, y, and z
    """
    return(x*y*z)

print(product(5,6,7))

# Challenge 4. Write 2 functions are nd pass the 1st into the 2nd
def half(x):
    """
    return x/2
    :param x: int
    :return: x / 2
    """
    return x/2

def quad(x):
    """
    return x * 4
    :param x: int
    :return: x * 4
    """
    return(x*4)

y = half(10)
z = quad(y)
print(y,z)

#Error handle a string to float conversion
def checknum(userString):
    """
    return userString as a float
    :param userString: string
    :return: float
    """
    try:
        userString = float(userString)
        return userString
    except ValueError:
        print("Function requires a number as a string")

z = "50.2"
print(checknum(z))