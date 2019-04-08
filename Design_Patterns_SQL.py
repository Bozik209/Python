import mysql.connector
from mysql.connector import (connection)
#-----------------SQL------------------------
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    db = "mysql"
)

#print(mydb)  #<mysql.connector.connection.MySQLConnection object at 0x03480F70>
mycursor = mydb.cursor()
mycursor.execute("USE `northwind`;")
mycursor.execute("SELECT first_name FROM customers")

myresult = mycursor.fetchall()

# for x in myresult:
#     #'write (str, x) 
#     print("".join(x))


print("------------------------------------------")
#---------------------class--------------------
class User():
    def getinfo(self):
        pass

class Admin(User):
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def getinfo(self):
        User.getinfo(self)
        return "I am an Admin"
    @classmethod
    def isValid(self,name,password):
            for x in myresult:
                if "".join(x)=="Admin":
                    return "".join(x)
            return None
        #return name=="Admin" and  password=="1234"

class Cashier (User):
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def getinfo(self):
        #User.getinfo(self)
        return "I am Cashier"
    @classmethod
    def isValid(self,name,password):
        for x in myresult:
            if "".join(x)=="Cashier":
                return "".join(x)
        return None
        #return name=="Cashier" and  password=="1234"

class Client(User):
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def getinfo(self):
        User.getinfo(self)
        return "I am Client"
    @classmethod
    def isValid(self,name,password):
        for x in myresult:
            if "".join(x)=="Client":
                return "".join(x)
        return None
        #return name=="Client" and  password=="1234"   

class UserFactory(object):
    @classmethod
    def login(self,name,password):
        #Admin
        if Admin.isValid(name,password):
            return Admin(name,password)
        #Cashier
        if Cashier.isValid(name,password):
            return Cashier(name,password)
        #Client
        if Client.isValid(name,password):
            return Client(name,password)
        return None



#---------------------Main--------------------
Names=["Admin","Cashier", "bob", "Client", "Admin"]

for name in Names:
    user = UserFactory.login(name,"1234")
    if user is None:
        print (name+" is not valid")
    else:
        print (name+" "+user.getinfo())


