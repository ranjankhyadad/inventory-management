from tkinter import *

window = Tk()

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

b1 =  Button(window, text = "View Items", width = 12)
b1.grid(row=2, column=3)

b2 =  Button(window, text = "Add Item", width = 12)
b2.grid(row=3, column=3)

b3 =  Button(window, text = "Search Item", width = 12)
b3.grid(row=4, column=3)

b4 =  Button(window, text = "Update Selected", width = 12)
b4.grid(row=5, column=3)

b5 =  Button(window, text = "Delete Selected", width = 12)
b5.grid(row=6, column=3)

b6 =  Button(window, text = "Close", width = 12)
b6.grid(row=7, column=3)

window.mainloop()

