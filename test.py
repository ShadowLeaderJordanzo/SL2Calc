from tkinter import *
from statClasses import *
import os
currentVersion = "0.1"
root = Tk()
root.grid_columnconfigure(0,weight = 1)
root.title('Sigrogana Legend 2 Calculator')
root.geometry("700x700")
pixel = PhotoImage(width=1, height=1)
# god i really want to clean this up somehow


# make this a class with these inside it
currentStats = statHandler( stats = [stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0),stat(base=0)],
	parent=root, pixel=pixel)
# 	root=root)
# end
def statAdd():
	return 
def statMinus():
	return 
# ref stat?
# ref stat? 

def astroPopUp():
	astro = Tk()
	astro.configure(bg='black')
	astroLabel = Label(astro, text = "Not implemented")
	astroLabel.pack()

	astro.mainloop()

# god i really want to clean this up somehow

version = Label(root, text="Version " + currentVersion)
Label(root).grid(row=0,column=1, sticky=NSEW)
version.grid(row=0,column=15,sticky=NSEW)
# addStatButtons()
# addStatLabels()
astroPhoto = PhotoImage(file = "astro.png")
myButton = Button(root, text="Click Me!", image = astroPhoto, command = astroPopUp)
myButton.grid(row=0,column=0,sticky='nws',)
root.mainloop()
