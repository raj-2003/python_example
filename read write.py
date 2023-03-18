file=open("tops1.txt","w")
file.write("this is file managment demo using pyhon")
file.close()
print("file written succesfully")
print("*************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*************************")

file=open("tops1.txt","a")
file.write("\nNow this file is appended.")
file.close()
print("file appended sucessfully.")
print("*************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*************************")


