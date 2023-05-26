class A:
    def method1(self):
        print("This is class A")
    def common(self):
        print("This is common method for A")
class B(A):
    def method2(self):
        print("This is class B")
    def common(self):
        print("This is common method for B")
class C(B):
    def method3(self):
        print("This is class C")
    def common(self):
        print("This is common method for C")
a=A()
b=B()
c=C()
a.method1()
b.method1()
b.method2()
c.method1()
c.method2()
c.method3()
c.common()