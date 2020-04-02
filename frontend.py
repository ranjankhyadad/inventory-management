from tkinter import *
import backend

def view_items():
    listbox.delete(0,END)
    for row in backend.view():
        listbox.insert(END,row)

def add_item():
    backend.insert(commodity.get(), quantity.get(), price.get(), serial.get())
    listbox.delete(0,END)
    listbox.insert(commodity.get(), quantity.get(), price.get(), serial.get())

def update_item():
    backend.update(selected_tuple[0], commodity.get(), quantity.get(), price.get(), serial.get())

def search_item():
    listbox.delete(0,END)
    for row in backend.search(commodity.get(), quantity.get(), price.get(), serial.get()):
    # x.get method converts StringVar to string
        listbox.insert(END,row)

def delete_item():
    backend.delete(selected_tuple[0])

def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0] #get index of the tuple in the list
        selected_tuple = listbox.get(index) #get tuple
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass
    
window = Tk()

window.title("Inventory")

l1 = Label(window, text = "Commodity :")
l1.grid(row=0, column=0)

l2 = Label(window, text = "Quantity :")
l2.grid(row=0, column=2)

l3 = Label(window, text = "Price :")
l3.grid(row=1, column=0)

l4 = Label(window, text = "Serial No :")
l4.grid(row=1, column=2)

commodity = StringVar()
e1 = Entry(window,textvariable= commodity)
e1.grid(row=0, column=1)

quantity = StringVar()
e2 = Entry(window,textvariable= quantity)
e2.grid(row=0, column=3)

price = StringVar()
e3= Entry(window,textvariable= price)
e3.grid(row=1, column=1)

serial = StringVar()
e4 = Entry(window,textvariable= serial)
e4.grid(row=1, column=3)

listbox = Listbox(window, height=6,width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand = sb.set) #y-axis scrollbar
sb.configure(command = listbox.yview) 

listbox.bind('<<ListboxSelect>>', get_selected_row)
#Bind method

b1 =  Button(window, text = "View Items", width = 12, command = view_items)
b1.grid(row=2, column=3)

b2 =  Button(window, text = "Add Item", width = 12, command= add_item)
b2.grid(row=3, column=3)

b3 =  Button(window, text = "Search Item", width = 12, command = search_item)
b3.grid(row=4, column=3)

b4 =  Button(window, text = "Update Selected", width = 12, command = update_item)
b4.grid(row=5, column=3)

b5 =  Button(window, text = "Delete Selected", width = 12, command = delete_item)
b5.grid(row=6, column=3)

b6 =  Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row=7, column=3)

window.mainloop()

