sname = input("Enter Student Name : ")
rno = int(input("Enter roll no :"))
s1 = int(input("Enter Marks Student 1 : "))
s2 = int(input("Enter Marks Student 2 : "))
s3 = int(input("Enter Marks Student 3 : "))

total = s1 + s2 + s3
per = total/3

print("Student Name is : ",sname)
print("Student Roll no. : ",rno)
print("Marks of subject 1 is : ",s1)
print("Marks of subject 2 is : ",s2)
print("Marks of subject 3 is : ",s3)
print("Total Marks : ",total)
print("Percentage : ",per)


if per>=70:
    print("Distinction")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("Third class")
else:
    print("Fail")
