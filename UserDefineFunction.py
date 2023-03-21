# Function with no argument & no return value

def printLine():
    print("*"*40)

printLine()
print("Demo of User Define Function")
printLine()

# Function with argument & no return value

def add(a,b):
    print("Addition of two Numbers are : ",a+b)

n1 = int(input("Enter first value : "))
n2 = int(input("Enter second value : "))
add(n1,n2)
printLine()

# Function with argument & return value

def sub(a,b):
    return a-b

n1 = int(input("Enter first value : "))
n2 = int(input("Enter second value : "))
ans = sub(n1,n2)
print("Substraction of two numbers is : ",ans)
printLine()

