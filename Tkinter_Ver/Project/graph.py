#imports
import tkinter as tk
import graphWorking as g

#funcs
def mainmenu():
    root.destroy()
    import MainScreen.py

def update():   #updates text box and graph
    global graph
    global photo
    photo = tk.PhotoImage(file = "graphImg.png")
    graph = tk.Label(root, width = 640, height = 480, relief = "raised", bd = 5, image = photo)
    graph.grid(column = 8, row = 0, rowspan = 5, padx = 2, pady = 2)

def parse(inp):    #takes in parameter based on which button is clicked; sends message to other module to update Y array    
    if inp == "clear":
        text1.set("X")
    elif inp in ["sin", "cos", "tan", "arcsin", "arccos", "arctan", "e^", "2^", "ln", "log", "log2", "1/", "mod"]:
        text1.set(inp+"("+text1.get()+")")
    g.update(inp)
    update()

def operate(op):
    global Working
    if op == "clear":
        text2.set("")
        Working = False
        disabler(Working)
    elif op in ["+", "-", "*", "/", "**"]:
        text2.set(text2.get()+" "+op)
        if Working == False:
            Working = True
            disabler(Working)

def disabler(w):
    if w == False:
        BtnClr2["state"] = "disabled"
        BtnClr["state"] = "normal"
        BtnSin["state"] = "normal"
        BtnCos["state"] = "normal"
        BtnTan["state"] = "normal"
        BtnArcsin["state"] = "normal"
        BtnArccos["state"] = "normal"
        BtnArctan["state"] = "normal"
        BtnExp["state"] = "normal"
        BtnExp2["state"] = "normal"
        BtnLog["state"] = "normal"
        BtnLog2["state"] = "normal"
        BtnLog10["state"] = "normal"
        BtnInverse["state"] = "normal"
        BtnMod["state"] = "normal"
    else:
        BtnClr2["state"] = "normal"
        BtnClr["state"] = "disabled"
        BtnSin["state"] = "disabled"
        BtnCos["state"] = "disabled"
        BtnTan["state"] = "disabled"
        BtnArcsin["state"] = "disabled"
        BtnArccos["state"] = "disabled"
        BtnArctan["state"] = "disabled"
        BtnExp["state"] = "disabled"
        BtnExp2["state"] = "disabled"
        BtnLog["state"] = "disabled"
        BtnLog2["state"] = "disabled"
        BtnLog10["state"] = "disabled"
        BtnInverse["state"] = "disabled"
        BtnMod["state"] = "disabled"

#main
root = tk.Tk()
root.title("Graph")
root.geometry("1280x525")
#root.resizable(False, False)

Frame1 = tk.Frame(root, bd = 5, relief = "raised")
Frame1.grid(column = 0, row = 0, columnspan = 7, rowspan = 4, padx = 2, pady = 2)
Frame2 = tk.Frame(root, bd = 5, relief = "raised")
Frame2.grid(column = 1, row = 4, columnspan = 7, rowspan = 3, padx = 2, pady = 2)

g.graph()
photo = tk.PhotoImage(file = "graphImg.png")
graph = tk.Label(root, width = 640, height = 480, relief = "raised", bd = 5, image = photo)
graph.grid(column = 8, row = 0, rowspan = 7, padx = 2, pady = 2)


MainMenu = tk.Button(root, text = "Main Menu", fg = "black", bg = "white", font = ("Calibri", 10), width = 10, command = mainmenu)
MainMenu.grid(column = 6, row = 7, padx = 2, pady = 2)

text1 = tk.StringVar()
text1.set("X")
Label = tk.Label(Frame1, textvariable = text1, fg = "black", bg = "white", font = ("Calibri", 10), width = 75, height = 5, anchor = "nw", justify = "left")
Label.grid(column = 0, row = 0, columnspan = 6, padx = 2, pady = 2)

BtnClr = tk.Button(Frame1, text = "clear", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("clear"))
BtnClr.grid(column = 10, row = 0, padx = 2, pady = 2)

BtnSin = tk.Button(Frame1, text = "sin(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("sin"))
BtnSin.grid(column = 0, row = 1, padx = 2, pady = 2)

BtnCos = tk.Button(Frame1, text = "cos(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("cos"))
BtnCos.grid(column = 1, row = 1, padx = 2, pady = 2)

BtnTan = tk.Button(Frame1, text = "tan(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("tan"))
BtnTan.grid(column = 2, row = 1, padx = 2, pady = 2)

BtnArcsin = tk.Button(Frame1, text = "Arcsin(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("arcsin"))
BtnArcsin.grid(column = 3, row = 1, padx = 2, pady = 2)

BtnArccos = tk.Button(Frame1, text = "Arccos(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("arccos"))
BtnArccos.grid(column = 4, row = 1, padx = 2, pady = 2)

BtnArctan = tk.Button(Frame1, text = "Arctan(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("arctan"))
BtnArctan.grid(column = 5, row = 1, padx = 2, pady = 2)

BtnExp = tk.Button(Frame1, text = "e^x", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("e^"))
BtnExp.grid(column = 0, row = 2, padx = 2, pady = 2)

BtnExp2 = tk.Button(Frame1, text = "2^x", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("2^"))
BtnExp2.grid(column = 1, row = 2, padx = 2, pady = 2)

BtnLog = tk.Button(Frame1, text = "Ln(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("ln"))
BtnLog.grid(column = 2, row = 2, padx = 2, pady = 2)

BtnLog10 = tk.Button(Frame1, text = "Log(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("log"))
BtnLog10.grid(column = 3, row = 2, padx = 2, pady = 2)

BtnLog2 = tk.Button(Frame1, text = "Log2(x)", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("log2"))
BtnLog2.grid(column = 4, row = 2, padx = 2, pady = 2)

BtnInverse = tk.Button(Frame1, text = "1/x", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("1/"))
BtnInverse.grid(column = 5, row = 2, padx = 2, pady = 2)

BtnMod = tk.Button(Frame1, text = "|x|", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:parse("mod"))
BtnMod.grid(column = 0, row = 3, padx = 2, pady = 2)

text2 = tk.StringVar()
text2.set("")
Working = False
Label2 = tk.Label(Frame2, textvariable = text2, fg = "black", bg = "white", font = ("Calibri", 10), width = 75, height = 5, anchor = "nw", justify = "left")
Label2.grid(column = 0, row = 0, columnspan = 5, padx = 2, pady = 2)

BtnClr2 = tk.Button(Frame2, text = "clear", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:operate("clear"), state = "disabled")
BtnClr2.grid(column = 6, row = 0, padx = 2, pady = 2)

BtnPlus = tk.Button(Frame2, text = "+", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:operate("+"))
BtnPlus.grid(column = 0, row = 1, padx = 2, pady = 2)

BtnMinus = tk.Button(Frame2, text = "-", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:operate("-"))
BtnMinus.grid(column = 1, row = 1, padx = 2, pady = 2)

BtnStar = tk.Button(Frame2, text = "*", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:operate("*"))
BtnStar.grid(column = 2, row = 1, padx = 2, pady = 2)

BtnSlash = tk.Button(Frame2, text = "/", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:operate("/"))
BtnSlash.grid(column = 3, row = 1, padx = 2, pady = 2)

BtnUp = tk.Button(Frame2, text = "^", fg = "black", bg = "white", font = ("Calibri", 10), width = 7, command = lambda:operate("**"))
BtnUp.grid(column = 4, row = 1, padx = 2, pady = 2)

##+
##-
##*
##/
##^
##0-9
##1/x
##pi

