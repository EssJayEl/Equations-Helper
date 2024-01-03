#imports
import mysql.connector as conn

#vars
userVar = "root"
pwdVar = "mysql"
connection = True

#funcs
def details(c = True, a = "root",b = "mysql"): #grabbing details
    global userVar, pwdVar, connection, con
    uservar, pwdVar, connection = str(a), str(b), c
    con = conn.connect(host = "localhost", user = userVar, password = pwdVar)
    beginning()

def beginning():    #initialise database and reading
    global con
    op = con.cursor()
    op.execute("drop database if exists project")
    op.execute("create database project")
    op.execute("use project")
    op.execute("create table chemistry(reagent1 varchar(30), reagent2 varchar(30), product varchar(30), extra text)")
    lst1, lst2 = list(), list()
    with open("reactions.txt", "r") as file:
        lst1 = file.readlines()
    for i in lst1:
        lst2.append(i.split(';'))
    query = "insert into chemistry values('{}', '{}', '{}', '{}')"
    for i in lst2:
        op.execute(query.format(*i))    #* so that it uses the values of the list as arguments, instead of the list itself

def getall():
    global con
    lst = []
    op = con.cursor()
    op.execute("select distinct(reagent1) from chemistry")
    lst.append([ str(x[0]) for x in list( op.fetchall() ) ])
    op.execute("select distinct(reagent2) from chemistry")
    lst.append([ str(x[0]) for x in list( op.fetchall() ) ])
    op.execute("select distinct(product) from chemistry")
    lst.append([ str(x[0]) for x in list( op.fetchall() ) ])
    return lst

def getOne(boxNo, value):
    global con
    op = con.cursor()
    if boxNo == 1:
        op.execute("select distinct(reagent2) from chemistry where reagent1 = '{}'".format(value))
        lst1 = [x[0] for x in op.fetchall()]
        op.execute("select distinct(product) from chemistry where reagent1 = '{}'".format(value))
        lst2 = [x[0] for x in op.fetchall()]
    elif boxNo == 2:
        op.execute("select distinct(reagent1) from chemistry where reagent2 = '{}'".format(value))
        lst1 = [x[0] for x in op.fetchall()]
        op.execute("select distinct(product) from chemistry where reagent2 = '{}'".format(value))
        lst2 = [x[0] for x in op.fetchall()]
    elif boxNo == 3:
        op.execute("select distinct(reagent1) from chemistry where product = '{}'".format(value))
        lst1 = [x[0] for x in op.fetchall()]
        op.execute("select distinct(reagent2) from chemistry where product = '{}'".format(value))
        lst2 = [x[0] for x in op.fetchall()]
    return lst1, lst2

def getTwo(firstBoxNo, secondBoxNo, firstValue, secondValue):
    global con
    op = con.cursor()
    if firstBoxNo == 1:
        if secondBoxNo == 2: #1,2
            op.execute("select product from chemistry where reagent1 = '{}' and reagent2 = '{}'".format(firstValue, secondValue))
            ret1 = op.fetchall()[0][0]
            op.execute("select extra from chemistry where reagent1 = '{}' and reagent2 = '{}'".format(firstValue, secondValue))
            ret2 = op.fetchall()[0][0]
        elif secondBoxNo == 3: #1,3
            op.execute("select reagent2 from chemistry where reagent1 = '{}' and product = '{}'".format(firstValue, secondValue))
            ret1 = op.fetchall()[0][0]
            op.execute("select extra from chemistry where reagent1 = '{}' and product = '{}'".format(firstValue, secondValue))
            ret2 = op.fetchall()[0][0]
    elif secondBoxNo == 2:  #2, 3
        op.execute("select reagent1 from chemistry where reagent2 = '{}' and product = '{}'".format(firstValue, secondValue))
        ret1 = op.fetchall()[0][0]
        op.execute("select extra from chemistry where reagent2 = '{}' and product = '{}'".format(firstValue, secondValue))
        ret2 = op.fetchall()[0][0]
    return ret1, ret2
    
