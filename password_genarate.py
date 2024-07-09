from tkinter import *
import random
import string
def password():
    if fname.get() == "":
        message.config(text='please fill fname')
    elif lname.get() == "":
        message.config(text='please fill lname')
    elif email.get() == "":
        message.config(text='please fill email')
    elif fname.get() == email.get() == "":
        lname.config("")
    elif fname.get() == lname == "":
        email.config("")
    elif lname.get() == email.get() == "":
        fname.config("")
    else:
        message.config(text='')
        fname.get() != "" + lname.get() != "" + email.get() != ""
        ps.config(text="")
        length = 8
        btn1 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        ps.delete(0, END)
        ps.insert(END, btn1)

root=Tk()
f1=Frame(root,bg="light blue",width=400,height=400)
f1.pack()
lbl1=Label(f1,text="PASSWORD GENERATOR",relief=RIDGE,font="bold",bg="red",bd=5)
lbl1.place(x=70,y=20)
lbl2=Label(f1,text="FName :",bg="grey",fg="black",font="bold",relief=RIDGE)
lbl2.place(x=20,y=90)
lbl3=Label(f1,text='LName :',bg="grey",fg="black",font="bold",relief=RIDGE)
lbl3.place(x=20,y=135)
lbl4=Label(f1,text="Email_ID :",bg="grey",fg="black",font="bold",relief=RIDGE)
lbl4.place(x=20,y=180)
message=Label(f1,bg="light blue",font="arial 12 bold",fg="black")
message.place(x=150,y=340)
ps=Entry(f1,relief=SOLID,font="bold",width=20)
ps.place(x=100,y=230)

btn1=Button(f1,text="Click",command=password,relief=RIDGE,font="bold",bg="red",bd=5)
btn1.place(x=150,y=280,width=100,height=40)

fname=Entry(f1,font="bold")
fname.place(x=120,y=90,height=30,width=270)
lname=Entry(f1,font="bold")
lname.place(x=120,y=135,height=30,width=270)
email=Entry(f1,font="bold")
email.place(x=120,y=180,height=30,width=270)
root.mainloop()