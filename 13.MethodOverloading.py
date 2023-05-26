# In Python we can achieve method overloading using multipledisptach
from multipledispatch import dispatch

@dispatch(int, int)
def sum(a, b):
    print("Sum of two numbers is: ", a+b)

@dispatch(int, int, int)
def sum(a,b, c):
    print("Sum of three numbers is: ", a+b+c)
sum(5,6)
sum(5,6,7)

@dispatch(int, str)
def add(i, s):
    print("Adding number to string: ", s+str(i))
@dispatch(int, int)
def add(a,b):
    print("Multiplication of two numbers: ", a*b)
add(5, "STR")
add(5,6)

@dispatch(int, int)
def sub(a, b):
    print("Subtraction of two numbers is: ", a-b)

@dispatch(int, int)
def sub(a, b):
    print("Subtraction of two numbers is: ", a-b)
sub(10,5)