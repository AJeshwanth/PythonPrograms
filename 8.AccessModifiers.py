# This code will give error as private members and methods can be accessed only in its class
class A:
    __priv="Ravi"
    _protect1="Kohli"
    publ="Dhoni"
    def publmeth(self):
        print("This is Public Method")
    def __primeth(self):
        print("This is Private Method")
    def _prometh(self):
        print("This is protected method")
class B(A):
    def call(self):
        super().publmeth()
        super()._prometh()
        # super().__primeth()
a=B()
a.call()
print("Protected memthod")
a._prometh()
print("Protected member" ,a._protect1)
print(a.__priv)
a.__primeth()