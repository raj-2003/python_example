n = int(input("Enter value : "))

x = 0
y = 1

if n == 0:
    print(n)
elif n < 0:
    print("Invalid Input")
else:
    print(x)
    
while y < n:
    print(y)
    x,y = y,x+y

