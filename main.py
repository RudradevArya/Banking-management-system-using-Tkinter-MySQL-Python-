import tkinter as Tk
from tkinter import *
import tkinter.messagebox
import mysql.connector
from PIL import Image

mydb = mysql.connector.connect(user = 'root',
                               passwd = '1234',
                               auth_plugin = 'mysql_native_password',
                               database = 'BankDB2'
                               )



mycursor = mydb.cursor(buffered = True)



#Tkinter login stuff starts


import tkinter as tk   
import tkinter.messagebox as mb
import random
import tkinter.ttk




import mysql.connector

db_connection = mysql.connector.connect(
host= "localhost",
user= "root",
password= "1234")

db_cursor = db_connection.cursor(buffered=True)


class Login_Success_Window(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("250x250")
         self.title("Registration Successful")
         self.configure(background="#ff80ff")
         self.lbl_Login_success = tk.Label(self, text="Login Success", font=("Source Serif Pro Semibold", 15), bg="yellow", fg="blue")
         self.lbl_Login_success.place(relx=0.150 , rely=0.111, height=21, width=250)

         # create OK button
         self.btn_register = tk.Button(self, text="OK", font=("Source Serif Pro Semibold", 11), bg="yellow", fg="blue",command=self.delete_login_success)
         #self.btn_register.pack(side = tk.BOTTOM)
         self.btn_register.place(relx=0.467, rely=0.311, height=21, width=30)
   def delete_login_success(self):
        mb.showinfo('Information', "Login Successful " + str(username))
        self.destroy()
        self.original_frame.show()


class RegisterWindow(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("600x450+485+162")
         self.title("Register")
         self.configure(background="#ff80ff")

         self.lblRegister = tk.Label(self, text="Registration Page", font=("Source Serif Pro Semibold", 16), bg="yellow", fg="blue")
         self.lblFName = tk.Label(self, text="Enter FirstName:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblLName= tk.Label(self, text="Enter LastName:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblLName = tk.Label(self, text="Enter LastName:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblUId = tk.Label(self, text="Enter UserId:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblPwd = tk.Label(self, text="Enter Password:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblPin = tk.Label(self, text="Enter Pin:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblContactNo = tk.Label(self, text="Enter Contact No:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblCity = tk.Label(self, text="Enter City:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")
         self.lblState = tk.Label(self, text="Enter State:", font=("Source Serif Pro Semibold", 10), bg="blue", fg="yellow")

         self.txtFName = tk.Entry(self)
         self.txtLName = tk.Entry(self)
         self.txtUId = tk.Entry(self)
         self.txtPwd = tk.Entry(self)
         self.txtContact = tk.Entry(self)
         self.txtCity = tk.Entry(self)
         self.txtState = tk.Entry(self)

         self.btn_register = tk.Button(self, text=" Register ", font=("Source Serif Pro Semibold", 11), bg="yellow", fg="blue", command=self.register)
         self.btn_cancel = tk.Button(self, text=" Back ", font=("Source Serif Pro Semibold", 11), bg="yellow", fg="blue", command=self.onClose)

         self.lblRegister.place(relx = 0.300, rely = 0.111, height = 30, width = 250)
         self.lblFName.place(relx = 0.308, rely = 0.221, height = 23, width = 100)
         self.lblLName.place(relx = 0.309, rely = 0.296, height = 23, width = 100)
         self.lblUId.place(relx = 0.345, rely = 0.371, height = 23, width = 78)
         self.lblPwd.place(relx = 0.309, rely = 0.446, height = 23, width = 100)
         self.lblContactNo.place(relx = 0.300, rely = 0.521, height = 23, width = 105)
         self.lblCity.place(relx = 0.365, rely = 0.596, height = 23, width = 66)
         self.lblState.place(relx = 0.359, rely = 0.671, height = 23, width = 70)
         self.txtFName.place(relx = 0.490, rely = 0.221, height = 23, relwidth = 0.223)
         self.txtLName.place(relx = 0.490, rely = 0.296, height = 23, relwidth = 0.223)
         self.txtUId.place(relx = 0.490, rely = 0.371, height = 23, relwidth = 0.223)
         self.txtPwd.place(relx = 0.490, rely = 0.446, height = 23, relwidth = 0.223)
         self.txtContact.place(relx = 0.490, rely = 0.521, height = 23, relwidth = 0.223)
         self.txtCity.place(relx = 0.490, rely = 0.596, height = 23, relwidth = 0.223)
         self.txtState.place(relx = 0.490, rely = 0.671, height = 23, relwidth = 0.223)
         self.btn_register.place(relx = 0.350, rely = 0.791, height = 28, width = 70)
         self.btn_cancel.place(relx = 0.605, rely = 0.791, height = 28, width = 70)

   def register(self):

       if db_connection.is_connected() == False:
             db_connection.connect()
    
       db_cursor.execute("CREATE DATABASE IF NOT EXISTS bankdb2")  
       db_cursor.execute("use bankdb2")  
       db_cursor.execute("Create table if not exists login(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),state VARCHAR(30),mobileno VARCHAR(10))")

       db_connection.commit()

       fname = self.txtFName.get()  
       lname = self.txtLName.get() 
       uid = self.txtUId.get()  
       pwd = self.txtPwd.get()  
       contact_no = self.txtContact.get()
       city = self.txtCity.get()  
       state = self.txtState.get()  
      
       if fname == "":
           mb.showinfo('Information', "Please Enter Firstname")
           self.txtFName.focus_set()
           return
       if lname == "":
           mb.showinfo('Information', "Please Enter Lastname")
           self.txtLName.focus_set()
           return
       if uid == "":
           mb.showinfo('Information', "Please Enter User Id")
           self.txtUId.focus_set()
           return
       if pwd == "":
           mb.showinfo('Information', "Please Enter Password")
           self.txtPwd.focus_set()
           return
       
       if contact_no  == "":
           mb.showinfo('Information', "Please Enter Contact Number")
           self.txtContact.focus_set()
           return
       if city == "":
           mb.showinfo('Information', "Please Enter City Name")
           self.txtCity.focus_set()
           return
       if state  == "":
           mb.showinfo('Information', "Enter State Name")
           self.txtState.focus_set()
           return
      
       db_cursor.execute("use bankdb2")
       query ="INSERT INTO login(uid,password,fname,lname,city,state,mobileno) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (uid,pwd,fname,lname,city,state,contact_no )

       try:
            
            db_cursor.execute(query)
            mb.showinfo('Information', "Data inserted Successfully :) ")
            
            db_connection.commit()
       except: 
            mb.showinfo('Information', "Data insertion failed!!! :( ")
           
            db_connection.rollback()
            
            db_connection.close()



   def onClose(self):
       
       self.destroy()
       self.original_frame.show()

class LoginApp(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("Matrix System ")
       self.geometry("600x450")
       self.configure(bg="#ff8040")
       self.lblHeading =tk.Label(self,text="Trupti Bank Login Page", font=("Source Serif Pro Semibold", 16),bg="yellow",fg="blue")
       self.lbluname = tk.Label(self,text="Enter UserName:", font=("Source Serif Pro Semibold", 10),bg="blue",fg="yellow")
       self.lblpsswd = tk.Label(self,text="Enter Password:", font=("Source Serif Pro Semibold", 10),bg="blue",fg="yellow")
       self.txtuname = tk.Entry(self,width=60)
       self.txtpasswd = tk.Entry(self,width=60, show="*")
       self.btn_login = tk.Button(self, text="Login",font=("Source Serif Pro Semibold", 11),bg="yellow",fg="blue",command=self.login)
       self.btn_clear= tk.Button(self, text="Clear",font=("Source Serif Pro Semibold", 11),bg="yellow",fg="blue",command=self.clear_form)
       self.btn_register = tk.Button(self, text="Register", font=("Source Serif Pro Semibold", 11),bg="yellow",fg="blue",command=self.open_registration_window)
       self.btn_exit = tk.Button(self, text="Exit",font=("Source Serif Pro Semibold", 16),bg="yellow",fg="blue" , command=self.exit)
       

       self.lblHeading.place(relx = 0.25, rely = 0.089, height = 41, width = 300)
       self.lbluname.place(relx = 0.235, rely = 0.289, height = 21, width = 106)
       self.lblpsswd.place(relx = 0.242, rely = 0.378, height = 21, width = 102)
       self.txtuname.place(relx = 0.450, rely = 0.289,height = 20, relwidth = 0.273)
       self.txtpasswd.place(relx = 0.450, rely = 0.378, height = 20, relwidth = 0.273)
       self.btn_login.place(relx = 0.070, rely = 0.550, height = 24, width = 150)
       self.btn_clear.place(relx = 0.385, rely = 0.550, height = 24, width = 150)
       self.btn_register.place(relx = 0.695, rely = 0.550, height = 24, width = 150 )
       self.btn_exit.place(relx = 0.75, rely = 0.850, height = 24, width = 70)
       


   def open_registration_window(self):
       self.withdraw()
       window = RegisterWindow(self)
       window.grab_set()


   def open_login_success_window(self):
       self.withdraw()
       window = Login_Success_Window(self)
       window.grab_set()


   def show(self):
      
       self.update()
       self.deiconify()

       

   def login(self):
       if db_connection.is_connected() == False:
           db_connection.connect()
       
       db_cursor.execute("CREATE DATABASE IF NOT EXISTS bankdb2")  
       db_cursor.execute("use bankdb2")
     
       db_cursor.execute("create table if not exists login(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),state VARCHAR(30),mobileno VARCHAR(10))")
       db_connection.commit()


       try:
           global username
           username = str(self.txtuname.get())  
           passwd = str(self.txtpasswd.get()) 
           if username == "" :
               mb.showinfo('Information', "Enter Username")
               self.txtuname.focus_set()
               return
           if passwd == "" :
               mb.showinfo('Information', "Enter Password")
               self.txtpasswd.focus_set()
               return

           print(username)
           print(passwd)
           
           print(query)
           self.open_def_menu()
          
           db_cursor.execute(query)
           rowcount = db_cursor.rowcount
           print(rowcount)
           if db_cursor.rowcount == 1:
              mb.showinfo('Information', "Login Successfull")
              self.open_login_success_window()
        
               
           
              
           else:
               mb.showinfo('Information', "Login failed, Invalid Username or Password. Please Try again!!! :) ")
       except:
        
          db_connection.disconnect()


   def clear_form(self):
    self.txtuname.delete(0, tk.END)
    self.txtpasswd.delete(0, tk.END)
    self.txtuname.focus_set()

   def exit(self):
    MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application',icon='warning')
    if MsgBox == 'yes':
        self.destroy()


if __name__ == "__main__":
  app = LoginApp()
  app.mainloop()



  #
    
    
    






#def main_display():
    #global root
    #root = Tk()
   # root.config(bg = "Black")
    #root.title("Login System")
    #root.geometry("500x300")
    #Label(root,text='Welcome to the Matrix',  bd=20, font=('Segoe UI Semibold', 20, 'bold'), relief="groove", fg="black",
                   #bg="orange",width=300).pack()
    #Label(root,text="").pack()
    #Button(root,text='Log In', height="1",width="20", bd=8, font=('Segoe UI Semibold', 12, 'bold'), relief="groove", fg="black",
                   #bg="orange",command=login).pack()
    #Label(root,text="").pack()
    #Button(root,text='Exit', height="1",width="20", bd = 8, font=('Segoe UI Semibold', 12, 'bold'), relief="groove", fg="black",
                   #bg="orange",command=Exit).pack()
    #Label(root,text="").pack()
    #Button(root,text='v1.0.2', height="1",width="20", bd = 8, font=('Segoe UI Semibold', 12, 'bold'), relief="groove", fg="black",
     #              bg="orange",command=Registration).pack()
    #Label(root,text="").pack()

#main_display()
#root.mainloop()






#Tkinter login stuff over



def Menu():

    print("*" * 157)
    print("|==========================================================|".center(150))
    print("|         +---TRUPTI Banking Management System---+         |".center(150))
    print("|                                                          |".center(150))
    print("|                                        Powered By-       |".center(150))
    print("|                                Tkinter-MySQL Connectivity|".center(150))
    print("|==========================================================|".center(150))
    print("|                       MAIN MENU                          |".center(150))
    print("|==========================================================|".center(150))
    print("|                  1. Insert Record/s                      |".center(150))
    print("|==========================================================|".center(150))
    print("|         2. Display Record/s as per Account Number        |".center(150))
    print("|              a. Sorted as per Account Number             |".center(150))
    print("|              b. Sorted as per Customer Number            |".center(150))
    print("|              c. Sorted as per Customer Balance           |".center(150))
    print("|==========================================================|".center(150))
    print("|    3. Search Record Details as per the account number    |".center(150))
    print("|==========================================================|".center(150))
    print("|                   4. Update Record                       |".center(150))
    print("|==========================================================|".center(150))
    print("|                   5. Delete Record                       |".center(150))
    print("|==========================================================|".center(150))
    print("|      6. Transactions Debit/Withdraw from the account     |".center(150))
    print("|              a. Debit/Withdraw from the account          |".center(150))
    print("|              b. Credit into the Account                  |".center(150))
    print("|==========================================================|".center(150))
    print("|                       7. EXIT                            |".center(150))
    print("|==========================================================|".center(150))
    print("*" * 157)

def MenuSort():
    print("   a. Sorted as per Account Number".center(150))
    print("   b. Sorted as per Customer Number".center(150))
    print("   c. Sorted as per Customer Balance".center(150))
    print("   d. BACK".center(150))

def MenuTransaction():
    print("   a. Debit/Withdraw from the account".center(150))
    print("   b. Credit into the account".center(150))
    print("   c. BACK".center(150))
    
def Create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10), NAME varchar(20), MOBILE varchar(10), EMAIL varchar(20), ADDRESS varchar(20), CITY varchar(10), COUNTRY varchar(20), BALANCE integer(15))')
        print(" [ Table Created ] ".center(52))
        print()
        Insert()
    except:
        print(" [ Table Created ] ".center(52))
        print()
        Insert()

def Insert():
    while True:
        Acc = input(" [ Enter Account Number ] :> ".center(52))
        print()
        Name = input(" [ Enter Name ] :> ".center(52))
        print()
        Mob = input(" [ Enter Mobile ] :> ".center(52))
        print()
        Email = input(" [ Enter Email ] :> ".center(52))
        print()
        Add = input(" [ Enter Address ] :> ".center(52))
        print()
        City = input(" [ Enter City ] :> ".center(52))
        print()
        Country = input(" [ Enter Country ] :> ".center(52))
        print()
        Bal = float(input(" [ Enter Balance ] :> ".center(52)))
        print()
        Rec = [Acc, Name.upper(), Mob, Email.upper(), Add.upper(), City.upper(), Country.upper(), Bal]
        Cmd = "insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch = input(" [ Do you want to enter more records ] :> ")
        print()
        if ch=='N' or ch=='n':
            break

def DispSortAcc():
    try:
        Cmd = "Select * from BANK order by ACCNO"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print("="*157)
        print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("="*157)
        for i in S:
            for j in i:
                print("%14s" % j, end = '  ')
            print()
        print("="*157)
    except:
        print(" [ Table dosent EXIST ] :> ".center(52))
        print()

def DispSortName():
    try:
        Cmd = "Select * from BANK order by NAME"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print("="*157)
        print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("="*157)
        for i in S:
            for j in i:
                print("%14s" % j, end = '  ')
            print()
        print("="*157)
    except:
        print(" [ Table dosent EXIST ] :> ")
        print()

def DispSortBal():
    try:
        Cmd = "Select * from BANK order by Balance"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print("="*157)
        print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("="*157)
        for i in S:
            for j in i:
                print("%14s" % j, end = '  ')
            print()
        print("="*157)
    except:
        print(" [ Table dosent EXIST ] :> ".center(52))
        print()

def DispSearchAcc():
    try:
        Cmd = "Select * from BANK"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        ch = input(" [ Enter the Account Number To Be Searched ] :> ".center(52))
        print()
        for i in S:
            if i[0] == ch:
                
                F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                print("="*157)
                print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
                print("="*157)
                for j in i:
                    print("%14s" % j, end = '  ')
                print()
                print("="*157)
                break
        else:
            print(" [ Record Not Found ] :> ".center(52))
            print()
    except:
        print(" [ Table dosent EXIST ] :> ".center(52))
        print()


def Update():
    try:
        Cmd = "SELECT * FROM BANK"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        A = input(" [ Enter the account number whose details are to be changed ] :> ")
        print()
        for i in S:
            i = list(i)
            if i[0] == A:
                ch = input(" [ Change Name ( Y / N ) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[1] = input(" [ Enter Name ] :> ".center(52))
                    print()
                    i[1] = i[1].upper()
                    
                ch = input(" [ Change Mobile ( Y / N ) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[2] = input(" [ Enter Mobile ] :> ".center(52))
                    print()
                    
                ch = input(" [ Change Email ( Y / N ) :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[3] = input(" [ Enter Email ] :> ".center(52))
                    print()
                    i[3] = i[3].upper()

                ch = input(" [ Change Addess ( Y / N ) :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[4] = input(" [ Enter Addess ] :> ".center(52))
                    print()
                    i[4] = i[4].upper()

                ch = input(" [ Change City ( Y / N ) :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[5] = input(" [ Enter City ] :> ".center(52))
                    print()
                    i[5] = i[5].upper()

                ch = input(" [ Change Country ( Y / N ) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[6] = input(" [ Enter Country ]      :> ".center(52))
                    print()
                    i[6] = i[6].upper()

                ch = input(" [ Change Balance ( Y / N ) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[7] = float(input(" [ Enter Balance ] :> ".center(52)))
                    print()
                Cmd = "UPDATE BANK SET NAME = %s, MOBILE = %s, EMAIL = %s, ADDRESS = %s, CITY = %s, COUNTRY = %s, BALANCE = %s WHERE ACCNO = %s "
                val = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                mycursor.execute(Cmd,val)
                mydb.commit()
                print(" [ Account Updated ]".center(52))
                print()
                break
        else:
            print(" [ Record Not Found ] ".center(52))
            print()
    except:
        print(" [ No Such Table ] ".center(52))
        print()
                    

                


def Delete():
    try:
        Cmd = "Select * from BANK"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        A = input(" [ Enter the account number whose details are to be changed ] :> ".center(52))
        print()
        for i in S:
            i = list(i)
            if i[0] == A:
                Cmd = "Delete from bank where accno = %s"
                val = (i[0],)
                mycursor.execute(Cmd, val)
                mydb.commit()
                print(" [ Account Deleted ] ".center(52))
                print()
                break
        else:
            print(" [ Record Not Found ] ".center(52))
            print()
    except:
        print(" [ No Such Table EXISTS ] ".center(52))
        print()


def Debit():
    try:
        Cmd = "select * from BANK"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        print(" [ Please Note that the money can only be debited if Min balance of Rs 5000 exists ] ".center(52))
        print()
        acc = input(" [ Enter Note that the account number from which the money is to be debited ] ".center(52))
        print()
        for i in S:
            i = list(i)
            if i[0] == acc:
                Amt = float(input(" [ Enter the amount to be withdrawn ] :> ".center(52)))
                print()
                if i[7] - Amt >= 5000:
                    i[7] -= Amt
                    Cmd = "UPDATE BANK SET BALANCE = %s WHERE ACCNO = %s"
                    val = (i[7], i[0])
                    mycursor.execute(Cmd, val)
                    mydb.commit()
                    print(" [ The Entered Amount Debited ] ".center(52))
                    print()
                    break
                else:
                    print(" [ Sorry Try Again There must be min balance of Rs 5000 ] ".center(52))
                    print()
                    break
        else:
            print(" [ Record not found ] ".center(52))
            print()
    except:
        print(" [ Table Dosent EXIST ] ".center(52))
        print()

def Credit():
    try:
        Cmd = "select * from BANK"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        acc = input(" [ Enter the Account number in which money is to be credited ] :> ".center(52))
        print()
        for i in S:
            i = list(i)
            if i[0] == acc:
                Amt = float(input(" [ Enter the amount to be credited ] :> ".center(52)))
                print()
                i[7] += Amt
                Cmd = "UPDATE BANK SET BALANCE = %s WHERE ACCNO = %s"
                val = (i[7], i[0])
                mycursor.execute(Cmd, val)
                mydb.commit()
                print(" [Amount Credited] ".center(52))
                print()
                break
        else:
            print(" [Record Not FOUND] ".center(52))
            print()
            
    except:
        print(" [Table Dosent EXIST] ".center(52))
        print()


while True:
    Menu()
    print()
    ch = input(" [ Please Enter your Choice] :> ".center(52))
    print()
    if ch == "1":
        Create()
    elif ch == "2":
        while True:
            MenuSort()
            print()
            ch1 = input(" [ Please Enter choice a / b / c / d] :> ".center(52))
            print()
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print(" [Back to the MAIN MENU] ".center(52))
                print()
                break
            else:
                print(" [Invalid choice] ".center(52))
                print()
    elif ch == "3":
        DispSearchAcc()
    elif ch == "4":
        Update()
    elif ch == "5":
        Delete()
    elif ch == "6":
        while True:
            MenuTransaction()
            ch1 = input(" [Enter choice a / b / c] :> ".center(52))
            print()
            if ch1 in ['a','A']:
                Debit()
            elif ch1 in ['b','B']:
                Credit()
            elif ch1 in ['c','C']:
                print(" [Back to the MAIN MENU] ".center(52))
                print()
                break
            else:
                print(" [Invalid choice] ".center(52))
                print()
    elif ch == "7":
        print(" [EXITING......  :) ] ".center(52))
        print()
        break
    else:
        print(" [Wrong Choice Entered] ".center(52))
        print()



def Update():
    try:
        Cmd = "select * from BANK"
        mycursor.execute(Cmd)
        S = mycursor.fetchall()
        A = input(" [ Please Enter the account number whose details to be changed ] :> ".center(52))
        print()
        for i in S:
            i = list(i)
            if i[0] == A:
                ch = input(" [ Change Name (Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[1] = input(" [ Enter Name ] :> ".center(52))
                    print()
                    i[1] = i[1].upper()
                ch = input(" [ Change Mobile(Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[2] = input(" [ Enter Mobile ] :> ".center(52))
                    print()

                ch = input(" [ Change Email (Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[3] = input(" [ Enter Email ] :> ".center(52))
                    print()
                    i[3] = i[3].upper()

                ch = input(" [ Change Address (Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[4] = input(" [ Enter Address ] :> ".center(52))
                    print()
                    i[4] = i[4].upper()

                ch = input(" [ Change City (Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[5] = input(" [ Enter City ] :> ".center(52))
                    print()
                    i[5] = i[5].upper()

                ch = input(" [ Change Country (Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[6] = input(" [ Enter Country ] :>".center(52))
                    print()
                    i[6] = i[6].upper()

                ch = input(" [ Change Balance (Y/N) ] :> ".center(52))
                print()
                if ch == 'y' or ch == 'Y':
                    i[7] = float(input(" [ Enter Balance ] :>"))
                    print()
                Cmd = "UPDATE BANK SET NAME = %s, MOBILE = %s, ADDRESS = %s, CITY = %s, COUNTRY = %s, BALANCE = %s, WHERE ACCNO = %s "
                val = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                mycursor.execute(Cmd, val)
                mydb.commit()
                print(" [ Account Updated ] ".center(52))
                print()
                break
        else:
            print(" [ Record not Found ] ".center(52))
            print()
    except:
        print(" [ No such Table ] ".center(52))
        print()
        
            
                    

                











        
