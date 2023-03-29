from tkinter import *       #tkinter module
import mysql.connector      #mysql connector library(pip install mysql-connector-python)
import tkinter.messagebox as msg

#connect to database
def create_conn():
    return mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "python_example"
        )

#print(create_con())            #call function to check code of function is execute or not


# Insert data to database 
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_mobile.get()=="" or e_email.get()=="":
        msg.showinfo("Insert Status","All fields are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into student (fname,lname,email,mobile) values (%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data inserted successfully..!")

#Search data from database
def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')

    if e_id.get() == "":
        msg.showinfo("Search Status","Id is Mandatory to search")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "Select * from student where id = %s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row = cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showinfo("Search Status", "Id is not found")
        conn.close()

#update data
    
def update_data():
    if e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile=="":
        msg.showinfo("Update Status","All fields are Mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query="update student set fname=%s, lname=%s, email=%s,mobile=%s where id=%s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,"end")
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")
        msg.showinfo("Update Status","Data Updated Successfully")

#Delete Data
def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id is Mandotory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,"end")
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")
        msg.showinfo("Delete Status","Data Deleted successfully")
                



root = Tk()        #object of Tk class                                      
root.geometry("400x400")                                
root.title("My First Tkinter Example")
root.resizable(width=False,height=False)                
#create a label place in root
l_id = Label(root,text="Id", font=("Arial",15))
l_id.place(x=50, y=50)

l_fname = Label(root,text="First Name",font=("Arial",15))
l_fname.place(x=50, y=100)

l_lname = Label(root,text="Last Name",font=("Arial",15))
l_lname.place(x = 50, y=150)

l_email = Label(root,text="Email",font=("Arial",15))
l_email.place(x = 50, y=200)

l_mobile = Label(root,text="Mobile",font=("Arial",15))
l_mobile.place(x = 50, y=250)

#Create a Textbox (Entry)

e_id = Entry(root)
e_id.place(x=200,y=50)

e_fname = Entry(root)
e_fname.place(x=200,y=100)

e_lname = Entry(root)
e_lname.place(x=200,y=150)

e_email = Entry(root)
e_email.place(x=200,y=200)

e_mobile = Entry(root)
e_mobile.place(x=200,y=250)


#Button Creation
insert=Button(root,text="INSERT",font=("Arial",11),fg="White",bg="Black" ,command = insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",font=("Arial",11),fg="White",bg="Black" ,command = search_data)
search.place(x=120,y=300)

update=Button(root,text="UPDATE",font=("Arial",11),fg="White",bg="Black" ,command = update_data)
update.place(x=197,y=300)

delete=Button(root,text="DELETE",font=("Arial",11),fg="White",bg="Black" ,command = delete_data)
delete.place(x=272,y=300)

root.mainloop()



