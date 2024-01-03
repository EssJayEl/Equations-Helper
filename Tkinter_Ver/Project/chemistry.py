#imports
import tkinter as tk

#funcs
def organic():
    root.destroy()  
    import organic

##def physical():
##    root.destroy()
##    import physical()

def mainmenu():
    root.destroy()
    import MainScreen

#main
root = tk.Tk()
root.title("Chemistry")
root.geometry("500x500")
root.resizable(False, False)

BtnOrganic = tk.Button(root, text = "Organic", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = organic)
BtnOrganic.place(relx=0.4, rely=0.4, bordermode = "inside")

##BtnPhysical = tk.Button(root, text = "Physical", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = physical)
##BtnPhysical.place(relx=0.4, rely=0.5, bordermode = "inside")

MainMenu = tk.Button(root, text = "Main Menu", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = mainmenu)
MainMenu.place(relx = 0.4, rely = 0.8, bordermode = "inside")

root.mainloop()
        
