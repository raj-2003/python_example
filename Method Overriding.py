class A:

    def show(self):
        print("show of A")

class B(A):

    def show(self):
        super().show()
        print("show of B")
        
class C(B):

    def show(self):
        super().show()
        print("show of C")

c1 = C()
c1.show()

    

