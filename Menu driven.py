print("******************** MENU *******************")
print('''1.Gujrati Thali \n2.Punjabi Thali \n3.Chineeze \n4.Pizza \n5.Ice Cream''')
print("*"*40)
user = input("Please Enter item you want to eat : ")

if(user=='1' or user=="Gujrati Thali"):
    print("Your order is placed and will served in 10 min maximum.")
    print("Please Wait.")

elif(user=='2' or user=="Punjabi Thali"):
    print("Your order is placed and will served in 15 min maximum.")
    print("Please Wait.")

elif(user=='3' or user=="Chineeze"):
    print("Your order is placed and will served in 10 min maximum.")
    print("Please Wait.")

elif(user=='4' or user=="Pizza"):
    print("Your order is placed and will served in 20 min maximum.")
    print("Please Wait.")

elif(user=='5' or user=="Ice Cream"):
    print("Your order is placed and will served in 5 min maximum.")
    print("Please Wait.")
else:
    print("Sorry..! We don't have this item now. Please Try Another item.")
    
