from tkinter import *

from Classes.classesClass import *
from Classes.personClass import *
from Classes.statClasses import *

from databaseInfo import *
test = 1
Data = Database()
root = Tk()
root.title('Sigrogana Legend 2 Calculator')
root.geometry("1200x600")
pixel = PhotoImage(width=1, height=1)
player = Person(root=root,pixel=pixel,dataBase=Data)
player.statHandler.setParents()
for columns in range(root.grid_size()[0]):
    root.grid_columnconfigure(columns,weight = 1)
root.mainloop()
