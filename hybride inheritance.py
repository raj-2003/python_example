class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("A :",self.a)

class B(A):
    def getB(self,b):
        self.b = b
    def putB(self):
        print("B :",self.b)


class C(A):
    def getC(self,c):
        self.c = c
    def putC(self):
        print("C :",self.c)


class D(B,C):
    def getD(self,d):
        self.d = d
    def putD(self):
        print("D :",self.d)


d1 = D()
d1.getA(20)
d1.putA()
d1.getB(40)
d1.putB()
d1.getC(60)
d1.putC()
d1.getD(80)
d1.putD()
