import UDF

while True:
    print("*"*30)
    print("1. oddEven")
    print("2. max Of Two Number")
    print("3. max Of Three Number")
    print("4. prime Number")
    print("5. fibbonacci Series")
    print("6. Exit")
    print("*"*30)
    select = int(input("Select your choice : "))


    if select == 1:
        n = int(input("Enter Value : "))
        UDF.oddEven(n)
        print("*"*30)
    elif select == 2:
        n1 = int(input("Enter Value : "))
        n2 = int(input("Enter Value : "))
        UDF.maxOfTwo(n1,n2)
        print("*"*30)
    elif select == 3:
        n1 = int(input("Enter Value : "))
        n2 = int(input("Enter Value : "))
        n3 = int(input("Enter Value : "))
        UDF.maxOfThree(n1,n2,n3)
        print("*"*30)
    elif select == 4:
        n = int(input("Enter Number to check prime or Not : "))
        UDF.primeNum(n)
        print("*"*30)
    elif select == 5:
        n = int(input("Enter range for fibbpnacci series : "))
        UDF.fibo(n)
        print()
        print("*"*30)
    elif select == 6:
        print("Bye.. Bye..")
        break
