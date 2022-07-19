from tkinter import *
import os
currentVersion = "0.1"
root = Tk()
root.title('Sigrogana Legend 2 Calculator')
root.geometry("400x600")
pixel = PhotoImage(width=1, height=1)
# god i really want to clean this up somehow

def statAdd():
	return 
def statMinus():
	return 
# ref stat?
def addStatLabels():
	statList = ["Strength","Will","Skill","Celerity","Defense","Resistance","Vitality","Faith","Luck","Guile","Sanctity", "Aptitude"]
	offset=3
	pointsRemaining = Label(root, text="0 Points Remaining", padx=15)
	pointsRemaining.grid(row=2,column=1)
	for x in range(len(statList)):
		theStat = Label(root, text=statList[x],padx=5)
		statValue = Label(root, text="0")
		theStat.grid(row=offset+x,column=0)
		statValue.grid(row=offset+x, column=1)
def addStatButtons():
	offsetRow = 3
	offsetColumn = 2
	for x in range(12):
		theButton = Button(root, text="+",command=statAdd,height=10,width=10, image=pixel, compound="c")
		otherButton = Button(root, text="-",command=statMinus,height=10,width=10, image=pixel, compound="c")
		theButton.grid(row=offsetRow+x,column=offsetColumn,padx=5)
		otherButton.grid(row=offsetRow+x,column=offsetColumn+1)
	return
# ref stat? 

def astroPopUp():
	astro = Tk()
	astro.configure(bg='black')
	astroLabel = Label(astro, text = "Not implemented")
	astroLabel.pack()

	astro.mainloop()

# god i really want to clean this up somehow

version = Label(root, text="Version " + currentVersion, width=15,)
version.grid(row=0,column=1, columnspan=3)
addStatButtons()
addStatLabels()
astroPhoto = PhotoImage(file = "astro.png")
myButton = Button(root, text="Click Me!", image = astroPhoto, command = astroPopUp)
myButton.grid(row=0,column=0)
root.mainloop()
