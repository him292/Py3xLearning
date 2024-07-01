# Hybrid Inheritance ( Multiple Inheritance + Multilevel Inheritance )
class A:
    def methodA(self):
        print("Method A from class A")

class B(A):
    def methodB(self):
        print("Method B from class B")

class C(A):
    def methodC(self):
        print("Method C from class C")

class D(B,C): # so now it can inherit all the methods above since it can access all of the above
    def methodD(self):
        print("Method D from class D")

d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()