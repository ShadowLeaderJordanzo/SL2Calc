from tkinter import *
from tkinter import tix

from Classes.classesClass import *
from Classes.personClass import *
from Classes.statClasses import *

from databaseInfo import *
test = 1
currentVersion = "0.1"
Data = Database()
root = tix.Tk()
classTest = ClassBonuses(name="Soldier",dataBase=Data)
root.title('Sigrogana Legend 2 Calculator')
root.geometry("900x600")
pixel = PhotoImage(width=1, height=1)
player = Person(root=root,pixel=pixel,dataBase=Data)
player.statHandler.setParents()
version = Label(root, text="Version " + currentVersion)
# Label(root).grid(row=0,column=1, sticky=NSEW)
version.grid(row=0,column=15,sticky=NSEW)
astroPhoto = PhotoImage(file = "Images/NoSign.png")
myButton = Button(root, image = astroPhoto, command = astroPopUp)
myButton.grid(row=0,column=16,rowspan=2,sticky=W,)
for columns in range(root.grid_size()[0]):
    root.grid_columnconfigure(columns,weight = 1)
root.mainloop()