def oddEven(n):
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n,"is odd")



def maxOfTwo(x,y):
    if x > y:
        print(x,"is greter Number")
    else:
        print(y,"is greter Number")



def maxOfThree(x,y,z):
    if x > y:
        if x > z:
            print(x,"is greter Number")
        else:
            print(z,"is greter Number")
    elif y > z:
        print(y,"is greter Number")
    else:
        print(z,"is greter Number")



def primeNum(n):
    if n % 2 != 0:
        for i in range(3,int(n/2)+1,3):
            if n % i == 0:
                print(n, "is not prime Number")
                break
        else:
            print(n,"is prime Number")
    else:
        print(n, "is not prime Number")



def fibo(n):
    a,b=0,1
    while b<n:
        print(b,end = " ")
        a,b=b,a+b
print()
