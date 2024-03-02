import flask
import sqlite3
import random,string

app = flask.Flask("__name__")

con = sqlite3.connect("CapcordApi.db")
cur = con.cursor()

def GenerateUserId():
    chars = string.digits + string.ascii_lowercase

    return "".join(random.choice(chars) for i in range(len(chars)-1))

@app.route("/",methods=["Get"])
def Home():
    return "Home page"

@app.route("/CreateAccount",methods=["Get"])
def CreateAccount(Username,Password):
    NewId = GenerateUserId()
    
    cur.execute(f"""INSERT INTO Login VALUES
                ({Username},{Password},{NewId})
                """)
    
@app.route("/GetAccountInfo",methods=["Get"])
def GetAccountInfo():
    User = cur.execute("SELECT Username FROM Login")
    Pass = cur.execute("SELECT Password FROM Login")
    Id = cur.execute("SELECT UserId FROM Login")
    
    return User.fetchall(),Pass.fetchall(),Id.fetchall()

cur.close()
