class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("Show from Class : A")

class B(A):
    def getB(self,b):
        self.b = b
    def putB(self):
        print("Show from Class : B")


b1 = B()
b1.getA(20)
b1.putA()
b1.getB(40)
b1.putB()
