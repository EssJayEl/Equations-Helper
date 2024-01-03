#imports
import tkinter as tk

#funcs
def graph():
    root.destroy()
    import graph

##def calc():
##    root.destroy()
##    import calc

def mainmenu():
    root.destroy()
    import MainScreen

#main
root = tk.Tk()
root.title("Math")
root.geometry("500x500")
root.resizable(False, False)

BtnGraph = tk.Button(root, text = "Graph", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = graph)
BtnGraph.place(relx=0.4, rely=0.4, bordermode = "inside")

##BtnCalc = tk.Button(root, text = "Calculator", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = calculator)
##BtnCalc.place(relx=0.4, rely=0.5, bordermode = "inside")

MainMenu = tk.Button(root, text = "Main Menu", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = mainmenu)
MainMenu.place(relx = 0.4, rely = 0.8, bordermode = "inside")

root.mainloop()
