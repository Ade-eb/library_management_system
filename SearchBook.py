from tkinter import *
from tkinter import messagebox
import mysql.connector as pymysql

mypass = "root1234" #Enter your mysql connection password
mydatabase="librarynew"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" #Book Table
    

def search():
    
    global SearchBtn,labelFrame,lb1,en1,quitBtn,root,Canvas1
    
    name = str(en1.get())
    SearchBtn.destroy()
    quitBtn.destroy()
    lb1.destroy()
    en1.destroy()
    
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.25
    
    Label(labelFrame, text="%-10s%-30s%-20s%-30s%-20s"%('BID','Title','Subject','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    cur.execute("select * from "+bookTable+" where title='"+name+"';")
    searched_books= cur.fetchall()
    print(searched_books)
    for i in searched_books:
            Label(labelFrame, text="%-10s%-30s%-20s%-30s%-20s"%(i),bg='black',fg='white').place(relx=0.07,rely=y)
                
    quitBtn = Button(root,text="< Back",bg='#455A64', fg='white', command=searchBook)
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    
def searchBook(): 
    
    global en1,SearchBtn,lb1,labelFrame,quitBtn,Canvas1,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="light green",width = 60000, height = 60000)
    Canvas1.pack(expand=True,fill=BOTH)
      
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)
        
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="SEARCH BOOK", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)   
        
    lb1 = Label(labelFrame,text="Enter Name : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SearchBtn = Button(root,text="Search",bg='#264348', fg='white',command=search)
    SearchBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#455A64', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
