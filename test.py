from tkinter import *
from statClasses import *
import os
currentVersion = "0.1"
root = Tk()
root.grid_columnconfigure(0,weight = 1)
root.title('Sigrogana Legend 2 Calculator')
root.geometry("700x700")
pixel = PhotoImage(width=1, height=1)
currentStats = statHandler( stats = [stat(base=0,name="strength"),stat(base=0,name="will"),stat(base=0,name="skill"),
	stat(base=0,name="celerity"),stat(base=0,name="defense"),stat(base=0,name="resistance"),stat(base=0,name="vitality"),
	stat(base=0,name="faith"),stat(base=0,name="luck"),stat(base=0,name="guile"),stat(base=0,name="sanctity"),stat(base=0,name="aptitude")],
	parent=root, pixel=pixel)
def astroPopUp():
	astro = Tk()
	astro.configure(bg='black')
	astroLabel = Label(astro, text = "Not implemented")
	astroLabel.pack()
	astro.mainloop()

version = Label(root, text="Version " + currentVersion)
Label(root).grid(row=0,column=1, sticky=NSEW)
version.grid(row=0,column=15,sticky=NSEW)

astroPhoto = PhotoImage(file = "astro.png")
myButton = Button(root, text="Click Me!", image = astroPhoto, command = astroPopUp)
myButton.grid(row=0,column=0,sticky='nws',)

root.mainloop()
