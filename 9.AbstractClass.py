class A():
    def abst(self):
        pass
    def nonabst(self):
        print("This not an abstract method")
class B(A):
    def abst(self):
        print("HThis is abstract method")
    def nonabst(self):
        print("This is not abstract method")
a=B()
a.abst()
a.nonabst()