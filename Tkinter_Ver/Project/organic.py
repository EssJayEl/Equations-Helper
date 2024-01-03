#imports
import tkinter as tk
import tkinter.ttk as tk2
import sqlWorking as sql
#inits
selected = 0    #which boxes are selected: 0-none; 1-first; 2-2nd; 3-3rd


#testcall
sql.details()


#funcs
def mainmenu():
    root.destroy()
    import MainScreen.py

def reset():
    global selected, var1, var2, var3, Reagent1, Reagent2, Reagent3
    selected = 0
    Reagent1['state'] = Reagent2['state'] = Reagent3['state'] = "readonly"

    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")

    values = sql.getall()
    Reagent1['values'] = values[0]
    Reagent2['values'] = values[1]
    Reagent3['values'] = values[2]
    

def bindFunc(boxNo):
    global selected, var1, var2, var3, var4
    if selected == 0:
        if boxNo == 1:
            Reagent2['values'], Reagent3['values'] = sql.getOne(1, var1.get())
            Reagent1['state'] = "disabled"
            selected = 1
            
        elif boxNo == 2:
            Reagent1['values'], Reagent3['values'] = sql.getOne(2, var2.get())
            Reagent2['state'] = "disabled"
            selected = 2
            
        elif boxNo == 3:
            Reagent1['values'], Reagent2['values'] = sql.getOne(3, var3.get())
            Reagent3['state'] = "disabled"
            selected = 3
            
    elif selected == 1:
        if boxNo == 2:
            tup = sql.getTwo(1, 2, var1.get(), var2.get())
            var3.set(tup[0])
            var4.set(tup[1])
        elif boxNo == 3:
            tup = sql.getTwo(1, 3, var1.get(), var3.get())
            var2.set(tup[0])
            var4.set(tup[1])
        Reagent2['state'] = Reagent3['state'] = 'disabled'
        
    elif selected == 2:
        if boxNo == 1:
            tup = sql.getTwo(1, 2, var1.get(), var2.get())
            var3.set(tup[0])
            var4.set(tup[1])
        elif boxNo == 3:
            tup = sql.getTwo(2, 3, var2.get(), var3.get())
            var1.set(tup[0])
            var4.set(tup[1])
        Reagent1['state'] = Reagent3['state'] = 'disabled'

    elif selected == 3:
        if boxNo == 1:
            tup = sql.getTwo(1, 3, var1.get(), var3.get())
            var2.set(tup[0])
            var4.set(tup[1])
        elif boxNo == 2:
            tup = sql.getTwo(2, 3, var2.get(), var3.get())
            var1.set(tup[0])
            var4.set(tup[1])
        Reagent1['state'] = Reagent2['state'] = 'disabled'

                        
#main
root = tk.Tk()
root.title("Chemistry")
root.geometry("1280x500")
root.resizable(False, False)

MainMenu = tk.Button(root, text = "Main Menu", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = mainmenu)
MainMenu.place(relx = 0.5, rely = 0.8)

var1 = tk.StringVar()  ## Reagent A
var2 = tk.StringVar() ## Reagent B
var3 = tk.StringVar() ## Product
var4 = tk.StringVar() ## Extra stuffs on arrow
values = sql.getall()

Label1 = tk.Label(root, text = "First Reagent", width = 30, fg = "black", bg = "white")
Label1.place(relx = 0.1, rely = 0.2)
Reagent1 = tk2.Combobox(root, state = "readonly", textvariable = var1, width = 30, values = values[0])
Reagent1.place(relx = 0.1, rely = 0.25)
Reagent1.bind("<<ComboboxSelected>>", lambda _ :bindFunc(1))

Label2 = tk.Label(root, text = "Second Reagent", width = 30, fg = "black", bg = "white")
Label2.place(relx = 0.3, rely = 0.2)
Reagent2 = tk2.Combobox(root, state = "readonly", textvariable = var2, width = 30, values = values[1])
Reagent2.place(relx = 0.3, rely = 0.25)
Reagent2.bind("<<ComboboxSelected>>", lambda _ :bindFunc(2))

Label3 = tk.Label(root, text = "Product", width = 30, fg = "black", bg = "white")
Label3.place(relx = 0.5, rely = 0.2)
Reagent3 = tk2.Combobox(root, state = "readonly", textvariable = var3, width = 30, values = values[2])
Reagent3.place(relx = 0.5, rely = 0.25)
Reagent3.bind("<<ComboboxSelected>>", lambda _ :bindFunc(3))

Label5 = tk.Label(root, text = "Extra Information", width = 30, fg = "black", bg = "white")
Label5.place(relx = 0.7, rely = 0.2)
Label4 = tk.Label(root, textvariable = var4, width = 30)
Label4.place(relx = 0.7, rely = 0.25)

BtnReset = tk.Button(root, text = "Reset", fg = "black", bg = "white", font = ("Calibri", 10), command = reset)
BtnReset.place(relx = 0.47, rely = 0.4)

root.mainloop()
