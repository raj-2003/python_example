'''x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
'''

P = int(input("enter value for P: "))  
Q = int(input("enter value for Q: "))  
   
temp = P  
P = Q  
Q = temp  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  
