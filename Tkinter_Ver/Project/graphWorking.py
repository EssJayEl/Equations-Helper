#imports
import numpy as np
import matplotlib.pyplot as plot
#inits
Y = np.linspace(-50, 50, 1000)
#funcs
def graph():
    plot.clf()
    global Y
    X = np.linspace(-50, 50, 1000)
    plot.plot(X, Y)
    plot.savefig("graphImg.png")

def update(inp):
    global Y
    if inp == "clear":
        Y = np.linspace(-50, 50, 1000)
    elif inp == "sin":
        Y = np.sin(Y)
    elif inp == "cos":
        Y = np.cos(Y)
    elif inp == "tan":
        Y = np.tan(Y)
    elif inp == "arcsin":
        Y = np.arcsin(Y)
    elif inp == "arccos":
        Y = np.arccos(Y)
    elif inp == "arctan":
        Y = np.arctan(Y)
    elif inp == "e^":
        Y = np.exp(Y)
    elif inp == "2^":
        Y = np.exp2(Y)
    elif inp == "ln":
        Y = np.log(Y)
    elif inp == "log":
        Y = np.log10(Y)
    elif inp == "log2":
        Y = np.log2(Y)
    elif inp == "1/":
        Y = np.reciprocal(Y)
    elif inp == "mod":
        Y = np.mod(Y)
    graph()
