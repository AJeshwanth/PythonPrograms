# print(25/0) Generates ZeroDivision Exception
class error(Exception):
    pass
def method(): 
    raise error("There are no arguments")
try:
    # print(25/0)
    # l=[1,2,3,4]
    # l[5]=6
    f=open("a.txt", "r")
    f.write("Hello world")
except ZeroDivisionError:
    print("Zero division error")
except IndexError:
    print("Index Error")
except IOError:
    print("Input Error")
except FileNotFoundError:
    print("File does not exists")
finally:
    print("This is finally block")
method()
