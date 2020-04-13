import sqlite3

class DB:
    def __init__(self,db):
        self.con = sqlite3.connect("inventory.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS storage (id INTEGER PRIMARY KEY, commodity TEXT, quantity INTEGER, price FLOAT, serial INTEGER)")
        self.con.commit()

    def view(self):
        self.cur.execute("SELECT * FROM storage")
        rows = self.cur.fetchall()
        return rows

    def insert(self,commodity,quantity,price,serial):
        self.cur.execute("INSERT INTO storage VALUES (NULL,?,?,?,?)", (commodity,quantity,price,serial))
        self.con.commit()

    def update(self, id,commodity,quantity,price,serial):
        self.cur.execute("UPDATE storage SET commodity= ?, quantity= ?, price= ?, serial= ? WHERE id=?",(commodity,quantity,price,serial,id))
        self.con.commit()

    def search(self, commodity="",quantity="",price="",serial=""):
        self.cur.execute("SELECT * FROM storage WHERE commodity= ? OR quantity= ? OR price= ? OR serial= ?", (commodity,quantity,price,serial))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM storage WHERE id= ?",(id,))
        self.con.commit()
        
# insert("Book",102,35,985)
# insert("Pen",120,7,575)
# print(search("Pen"))
# update(1,"Book",152,36,985)
# print(view())
