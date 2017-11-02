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
