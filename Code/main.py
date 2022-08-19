from tkinter import *

from Classes.classesClass import *
from Classes.personClass import *
from Classes.statClasses import *

from databaseInfo import *
test = 1
currentVersion = "0.1c"
Data = Database()
root = Tk()
root.title('Sigrogana Legend 2 Calculator')
root.geometry("1200x600")
pixel = PhotoImage(width=1, height=1)
player = Person(root=root,pixel=pixel,dataBase=Data)
player.statHandler.setParents()
versionFrame = ttk.Frame(root)
versionFrame.grid(row=0,column=15,sticky=NSEW,columnspan=3,rowspan=2)
version = Label(versionFrame, text="Version " + currentVersion)
# Label(root).grid(row=0,column=1, sticky=NSEW)
version.grid(row=0,column=0,sticky=NSEW)
image = fileName('Images\\NoSign.png')
astroPhoto = PhotoImage(file = image)
myButton = Button(versionFrame, image = astroPhoto, command = astroPopUp)
myButton.grid(row=0,column=1,rowspan=2,sticky=W,)
for columns in range(root.grid_size()[0]):
    root.grid_columnconfigure(columns,weight = 1)
root.mainloop()
