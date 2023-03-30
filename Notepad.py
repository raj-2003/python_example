from tkinter import *
from tkinter.filedialog import *
root = Tk()
root.geometry('400x570')
root.title('Notepad')
root.resizable(height=False,width=False)
#button Function
def openfile():
    file = askopenfile(mode='r',filetypes=[('filename','*.txt')])
    if file is not None:
        content = file.read()
        text.insert(INSERT,content)
def savefile():
    new_file = asksaveasfile(mode='w',filetypes=[('filename','.txt')])
    if new_file is None:
        return
    text1 = text.get(1.0,END)
    new_file.write(text1)
    new_file.close()
    
def clearfile():
    text.delete(1.0,END)

#Text Box
text = Text(root,font=("Arial",11),bg="Yellow",wrap=WORD)
text.pack(padx=10,pady=40)

#button

Button(root,text='Open',font=("Arial",11),bg='blue',fg='white',bd=0,cursor='hand2',command=openfile).place(x=50,y=452)
Button(root,text='Save',font=("Arial",11),bg='green',fg='white',bd=0,cursor='hand2',command=savefile).place(x=130,y=452)
Button(root,text='Clear',font=("Arial",11),bg='purple',fg='white',bd=0,cursor='hand2',command=clearfile).place(x=210,y=452)
Button(root,text='Exit',font=("Arial",11),bg='red',fg='white',bd=0,cursor='hand2',command=lambda :exit()).place(x=290,y=452)
mainloop()
