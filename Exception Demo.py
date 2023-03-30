print("*"*50)
try:
    
    a=int(input("enter A:"))
    b=int(input("enter B:"))

    c=a/b

    print("division: ",c)

    l=[1,2,3,4,5]
    index=int(input("enter index number: "))
    print(l[index])

except Exception as error:
    print("Exaption Occured : ",error)


print("*"*50)

'''
except ZeroDivisionError as error:
    print("Exaption Occured : ",error)

except IndexError as error:
    print("Exaption Occured : ",error)
'''
