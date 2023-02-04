# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter
# Importing tkinter

from PIL import Image
im = (Image.open("ybusimage2.png"))
im.show()
import ybus

from tkinter import *
# Importing ttk from tkinter

from tkinter import ttk
# Creating app window

app = Tk()
# Defining title of the app
app.geometry("600x600")
app.title("GUI application of YBUS")
# Defining label of the app and calling a geometry
# management method i.e, pack in order to organize
# widgets in form of blocks before locating them
# in the parent widget
ttk.Label(app, text ="Y-Bus admittance").pack()

# Creating treeview window
treeview = ttk.Treeview(app)

# Calling pack method on the treeview
treeview.pack()

# Inserting items to the treeview
# Inserting parent
treeview.insert('', '0', 'item1',
				text ='Y-bus')

# Inserting child
treeview.insert('', '1', 'item2',
				text ='ROW 1')
treeview.insert('', '2', 'item3',
				text ='ROW 2')
treeview.insert('', 'end', 'item4',
				text ='ROW 3')

# Inserting more than one attribute of an item
treeview.insert('item2', 'end', 'Y11=1.5-4.47j',
		text ='Y11=1.5-4.47j')
treeview.insert('item2', 'end','Y12=-1.02+3j',
                text ='Y12=-1.02+3j')
treeview.insert('item2', 'end','Y13=-0.5+1.5j',
                text ='Y13=-0.5+1.5j')
treeview.insert('item3', 'end', 'Y21=-1.02+3j',  
				text ='Y21=-1.02+3j')
treeview.insert('item3', 'end','Y22=1.5-4.8j',
                text ='Y22=1.5-4.8j')
treeview.insert('item3', 'end','Y23=-0.55+1.83j',
                text ='Y23=-0.55+1.83j')
treeview.insert('item4', 'end', 'Y31= -0.500+1.5j', 
				text ='Y31= -0.500+1.5j')
treeview.insert('item4', 'end','Y32=-0.55+1.8j',
                text ='Y32=-0.55+1.8j')
treeview.insert('item4', 'end','Y33= 1.050-3.314j',
                text ='Y33= 1.050-3.314j')
# Placing each child items in parent widget
treeview.move('item2', 'item1', 'end')
treeview.move('item3', 'item1', 'end')
treeview.move('item4', 'item1', 'end')

# Calling main()
app.mainloop()



