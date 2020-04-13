from tkinter import *
from backend import DB

db = DB("inventory.db")

class my_window:
    def __init__(self,window):
        
        self.window = window

        self.window.title("Inventory")

        l1 = Label(self.window, text = "Commodity :")
        l1.grid(row=0, column=0)

        l2 = Label(self.window, text = "Quantity :")
        l2.grid(row=0, column=2)

        l3 = Label(self.window, text = "Price :")
        l3.grid(row=1, column=0)

        l4 = Label(self.window, text = "Serial No :")
        l4.grid(row=1, column=2)

        self.commodity = StringVar()
        self.e1 = Entry(self.window,textvariable= self.commodity)
        self.e1.grid(row=0, column=1)

        self.quantity = StringVar()
        self.e2 = Entry(self.window,textvariable= self.quantity)
        self.e2.grid(row=0, column=3)

        self.price = StringVar()
        self.e3= Entry(self.window,textvariable= self.price)
        self.e3.grid(row=1, column=1)

        self.serial = StringVar()
        self.e4 = Entry(self.window,textvariable= self.serial)
        self.e4.grid(row=1, column=3)

        self.listbox = Listbox(self.window, height=6,width=35)
        self.listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb = Scrollbar(self.window)
        sb.grid(row=2, column=2, rowspan=6)

        self.listbox.configure(yscrollcommand = sb.set) #y-axis scrollbar
        sb.configure(command = self.listbox.yview) 

        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)
        #Bind method

        b1 =  Button(self.window, text = "View Items", width = 12, command = self.view_items)
        b1.grid(row=2, column=3)

        b2 =  Button(self.window, text = "Add Item", width = 12, command= self.add_item)
        b2.grid(row=3, column=3)

        b3 =  Button(self.window, text = "Search Item", width = 12, command = self.search_item)
        b3.grid(row=4, column=3)

        b4 =  Button(self.window, text = "Update Selected", width = 12, command = self.update_item)
        b4.grid(row=5, column=3)

        b5 =  Button(self.window, text = "Delete Selected", width = 12, command = self.delete_item)
        b5.grid(row=6, column=3)

        b6 =  Button(self.window, text = "Close", width = 12, command = self.window.destroy)
        b6.grid(row=7, column=3)
    
    def view_items(self):
        self.listbox.delete(0,END)
        for row in db.view():
            self.listbox.insert(END,row)

    def add_item(self):
        db.insert(self.commodity.get(), self.quantity.get(), self.price.get(), self.serial.get())
        self.listbox.delete(0,END)
        self.listbox.insert(END,(self.commodity.get(), self.quantity.get(), self.price.get(), self.serial.get()))

    def update_item(self):
        db.update(selected_tuple[0], self.commodity.get(), self.quantity.get(), self.price.get(), self.serial.get())

    def search_item(self):
        self.listbox.delete(0,END)
        for row in db.search(self.commodity.get(), self.quantity.get(), self.price.get(), self.serial.get()):
        # x.get method converts StringVar to string
            self.listbox.insert(END,row)

    def delete_item(self):
        db.delete(selected_tuple[0])

    def get_selected_row(self,event):
        try:
            global selected_tuple
            index = self.listbox.curselection()[0] #get index of the tuple in the list
            selected_tuple = self.listbox.get(index) #get tuple
            self.e1.delete(0,END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

window = Tk()
my_window(window)
window.mainloop()