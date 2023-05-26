class A:
    # Class can have only one constructor in python
    # def __init__(self):
    #     print("Default Constructor ")
    # "__" denotes private "_" denotes protected "" denotes default or public before __init__
    def __init__(self, a, b):
        print("Sum of two numbers is: ", a+b)

class B(A):
    def __init__(self):
        # super().__init__()
        super().__init__(5,6)
b=B()
a=A(7,8)