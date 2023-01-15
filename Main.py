from tkinter import *
import mysql.connector as pymysql
from tkinter import messagebox
from AddBooks import *
from DeleteBook import *
from SearchBook import *
from IssueBook import *

mypass = "maukhanmau" #Enter your MySQL connection password
mydatabase="librarynew"


empTable = "empdetail"
stuTable = "studetail"

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("60010x50010")
count = 0
empFrameCount = 0

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def empMenu():
    
    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#f7f1e3",width = 600000, height = 600000)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="Employee MENU", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBooks)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Search Book",bg='black', fg='white', command=searchBook)
    btn4.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="<  BACK",bg='#455A64', fg='white', command=Employee)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    
def stuMenu():
    
    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,btn1,btn2,btn3,btn4,btn5,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#dff9fb",width = 600000, height = 600000)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="Student MENU", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn2 = Button(root,text="Search Book",bg='black', fg='white',command=searchBook)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="<  BACK",bg='#455A64', fg='white', command=Student)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def gettingEmpDetails():
    
    EmpId = en1.get()
    name = en2.get()
    password = en3.get()
        
    try:
        if (type(int(EmpId)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Employee ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Employee ID should be an integer")
        return
        
    sql = "insert into "+empTable+" values ('"+EmpId+"','"+name+"','"+password+"');" 
    cur.execute(sql)
    con.commit()
        
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    
def gettingStuDetails():
    
    Rollno = en1.get()
    name = en2.get()
    password = en3.get()
    
    
    try:
        if (type(int(Rollno)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Roll number should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Roll number should be an integer")
        return

    
    sql = "insert into "+stuTable+" values ('"+Rollno+"','"+name+"','"+password+"');" 
    cur.execute(sql)
    con.commit()
            
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    
    
def gettingLoginDetails():
    
    login = en1.get()
    name = en2.get()
    password = en3.get()
    role = en4.get()
    role.lower()
    if (role == 'emp'):
        sqlLoginID = "select empid from "+empTable+" where password = '"+password+"';"
        sqlName = "select name from "+empTable+" where password = '"+password+"';"
        
        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]
            if(int(login) == int(getLoginID) and name == getName):
                empMenu()
                messagebox.showinfo("SUCCESS","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")        
    elif (role == 'stu'):
        sqlLoginID = "select rollno from "+stuTable+" where password = '"+password+"';"
        sqlName = "select name from "+stuTable+" where password = '"+password+"';"
        
        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]

            if(int(getLoginID) == int(login) and getName == name):
                stuMenu()
                messagebox.showinfo("SUCCESS","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")        
    else:
        messagebox.showinfo("EXCEPTION","Role can only be emp or stu")
        return
        
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    
def EmpRegister():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)
    
    # Employee ID
    lb1 = Label(labelFrame,text="Emp ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.05)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    #Employee Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.2)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    #Employee Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingEmpDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Login both for Employee and Student
def Login():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,SubmitBtn,btn1,btn2
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
    
    # Login ID
    lb1 = Label(labelFrame,text="Login_ID / Roll no. : ", bg='#044F67', fg='white')
    lb1.place(relx=0.02,rely=0.1)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
    
    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.3)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.5)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Role
    lb4 = Label(labelFrame,text="Role (emp/stu) : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.7)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.7, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingLoginDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Registration
def studentRegister():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3

    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)
    
    # Student Roll no
    lb1 = Label(labelFrame,text="Roll No. : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.05)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    # Sudent Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.2)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Student Password
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)
       
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingStuDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
# Employee Home Page 
def Employee():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4",width = 60000, height = 6000)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, Employee", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Register",bg='black', fg='white',command=EmpRegister)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.destroy)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Home Page   
def Student():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFF9C4",width = 600000, height = 600000)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, Student", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Register",bg='black', fg='white', command=studentRegister)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.destroy)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

Canvas1=Canvas(root)
Canvas1.config(bg='light blue')
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Library Management System", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Employee",bg='black', fg='white', command=Employee)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Student",bg='black', fg='white', command=Student)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)

root.mainloop()
