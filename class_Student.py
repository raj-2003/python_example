class Student():

    def getData(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def putData(self):
        print("Student First name : ",self.fname)
        print("Student Last name : ",self.lname)


s1 = Student()
fname = input("Enter First name : ")
lname = input("Enter Last name : ")
s1.getData(fname,lname)
s1.putData()
