import sqlite3

def create():
    con = sqlite3.connect("inventory.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS storage (id INTEGER PRIMARY KEY, commodity TEXT, quantity INTEGER, price FLOAT, serial INTEGER)")
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("inventory.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM storage")
    rows = cur.fetchall()
    con.close()
    return rows

def insert(commodity,quantity,price,serial):
    con = sqlite3.connect("inventory.db")
    cur = con.cursor()
    cur.execute("INSERT INTO storage VALUES (NULL,?,?,?,?)", (commodity,quantity,price,serial))
    con.commit()
    con.close()

def update(id,commodity,quantity,price,serial):
    con = sqlite3.connect("inventory.db")
    cur = con.cursor()
    cur.execute("UPDATE storage SET commodity= ?, quantity= ?, price= ?, serial= ? WHERE id=?",(commodity,quantity,price,serial,id))
    con.commit()
    con.close()

def search(commodity="",quantity="",price="",serial=""):
    con = sqlite3.connect("inventory.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM storage WHERE commodity= ? OR quantity= ? OR price= ? OR serial= ?", (commodity,quantity,price,serial))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("inventory.db")
    cur = con.cursor()
    cur.execute("DELETE FROM storage WHERE id= ?",(id,))
    con.commit()
    con.close()    

create()
# insert("Book",102,35,985)
# insert("Pen",120,7,575)
# print(search("Pen"))
# update(1,"Book",152,36,985)
# print(view())
