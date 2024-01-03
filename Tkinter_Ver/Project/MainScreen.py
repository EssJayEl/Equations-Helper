import tkinter as tk
from tkinter import messagebox
import sqlWorking as sql

import mysql.connector as conn

def submit(a, b):
    MySqlDetails = list((a, b))     #tuple for storing user, pwd
    ##give MySqlDetails to working module
    try:
        con = conn.connect(host = "localhost", user = MySqlDetails[0], password = MySqlDetails[1])
        if con.is_connected():  #checking if connection is made
            messagebox.showinfo("Success!", "Connection Successfull!")
            sql.details(True, MySqlDetails[0], MySqlDetails[1])   #giving details to module to be used later
    except:
        messagebox.showwarning("Connection Error","Python could not connect to mysql. Please check mysql, python, and mysql connector installation, as well as entered credentials")
        sql.details(False)
    top.withdraw()


def chemistry():
    root.destroy()
    import chemistry

def math():
    root.destroy()
    import mathModule

#main window
root = tk.Tk()
root.title("Menu")
root.geometry("500x500")
root.resizable(False, False)

BtnChem = tk.Button(root, text = "Chemistry", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = chemistry)
BtnChem.place(relx=0.4, rely=0.4, bordermode = "inside")

BtnMath = tk.Button(root, text = "Math", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = math)
BtnMath.place(relx=0.4, rely=0.5, bordermode = "inside")

BtnSql = tk.Button(root, text = "Use MySql", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = lambda:top.deiconify() )
BtnSql.place(relx = 0.4, rely = 0.8, bordermode = "inside")

#Sql window
top = tk.Toplevel(height = 300, width = 200)
top.withdraw()
top.resizable(False, False)
top.title("SQL")

Label = tk.Label(top, anchor = "center", bg = "white", fg = "black", text = "Enter MySQL database\ndetails to be used\nin the program", font = ("Calibri", 10), width = 20, height = 3)
Label.place(relx = 0.15, bordermode = "inside", rely = 0.01)

UserText = tk.StringVar()
UserText.set("Enter username")
User = tk.Entry(top, bg = "white", fg = "black", font = ("Calibri", 10), textvariable = UserText, width = 20)
User.place(relx = 0.15, bordermode = "inside", rely = 0.2)

PwdText = tk.StringVar()
PwdText.set("Enter password")
Pwd = tk.Entry(top, bg = "white", fg = "black", font = ("Calibri", 10), textvariable = PwdText, width = 20)
Pwd.place(relx = 0.15, bordermode = "inside", rely = 0.3)

Submit = tk.Button(top, text = "Submit", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = lambda: submit( User.get(), Pwd.get() ) )
Submit.place(relx=0.3, bordermode = "inside", rely = 0.4)

Close = tk.Button(top, text = "Close", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = lambda: top.withdraw())
Close.place(relx = 0.3, bordermode = "inside", rely = 0.5)

root.mainloop()
