from tkinter import *
from tkinter import ttk
from databaseInfo import *

class AstroHandler:
	values = {"neptune":["vitality","water"],
			"jupiter":["luck","lightning"],
			"mars":["strength","fire"],
			"pluto":["resistance","dark"],
			"venus":["defense","earth"],
			"uranus":["faith","light"],
			"saturn":["celerity","wind"],
			"mercury":["skill","ice"],
           }
	def __init__(self,root, parent):
		self.previousChoice = "noSign"
		self.currentChoice = "noSign"
		self.person = parent
	def astroPopUp(self):
		self.astro = Toplevel()
		self.astro.configure(bg='black')
		self.astro.resizable=(0,0)
		self.astro.wm_maxsize(width=307,height=313)
		self.astro.wm_minsize(width=307,height=313)
		self.starSign = PhotoImage(file = fileName('Images\\Starsign.png'))
		self.astroCanvas = Canvas(self.astro, width=307,height=313)
		self.astroCanvas.pack(fill="both",expand= TRUE)
		self.astroCanvas.create_text(100,100, text="hm")
		self.astroCanvas.create_image(0,0,image=self.starSign, anchor="nw")
		self.makeLabels()
		self.astro.mainloop()
	def submitChange(self, newchoice):
		toChange = ""
		stats = self.person.statHandler
		elements = self.person.eleHandler
		if self.previousChoice != "noSign":
			toChange = self.getChanges(name=self.previousChoice) # this should match
			stat = getattr(stats, toChange[0])
			if getattr(stat, "hiddenMod") != 0:
				setattr(stat, "hiddenMod", getattr(stat, "hiddenMod") - 1)
				element = getattr(elements, "eleATK")[toChange[1]]
				setattr(element, "baseMod", getattr(element, "baseMod") - 2)
		if newchoice != "noSign":
			currentChanges = self.getChanges(name=newchoice)
			stat = getattr(stats, currentChanges[0])
			setattr(stat, "hiddenMod", getattr(stat, "hiddenMod") + 1)
			element = getattr(elements, "eleATK")[currentChanges[1]]
			setattr(element, "baseMod", getattr(element, "baseMod") + 2)
		self.previousChoice = newchoice
		stats.updateAll()
		elements.updateAll()
		namesake =f"{newchoice}Image"
		self.person.astroButton.configure(image=getattr(self, namesake))
	def getChanges(self, name):
		return AstroHandler.values[name]
	def makeLabels(self):
		self.neptuneImage = PhotoImage(file=fileName(f"Images\\Neptune.png"))
		self.neptune = AstroButtons(root=self.astro, name="Neptune",function="+1 VIT +2 Water ATK",imageneeded=self.neptuneImage, cmd=lambda:self.submitChange("neptune"))
		self.astroCanvas.create_window(4,130, anchor="nw", window = self.neptune)
  
		self.jupiterImage = PhotoImage(file=fileName(f"Images\\Jupiter.png"))
		self.jupiter = AstroButtons(root=self.astro, name="Jupiter",function="+1 LUK +2 Lightning ATK",imageneeded=self.jupiterImage, cmd=lambda:self.submitChange("jupiter"))
		self.astroCanvas.create_window(252,130, anchor="nw", window = self.jupiter)
  
		self.marsImage = PhotoImage(file=fileName(f"Images\\Mars.png"))
		self.mars = AstroButtons(root=self.astro, name="Mars",function="+1 STR +2 Fire ATK",imageneeded=self.marsImage, cmd=lambda:self.submitChange("mars"))
		self.astroCanvas.create_window(193,196, anchor="nw", window = self.mars)
  
		self.plutoImage = PhotoImage(file=fileName(f"Images\\Pluto.png"))
		self.pluto = AstroButtons(root=self.astro, name="Pluto",function="+1 RES +2 Dark ATK",imageneeded=self.plutoImage, cmd=lambda:self.submitChange("pluto"))
		self.astroCanvas.create_window(129,257 , anchor="nw", window = self.pluto)
  
		self.venusImage = PhotoImage(file=fileName(f"Images\\Venus.png"))
		self.venus = AstroButtons(root=self.astro, name="Venus",function="+1 DEF +2 Earth ATK",imageneeded=self.venusImage, cmd=lambda:self.submitChange("venus"))
		self.astroCanvas.create_window(66,67 , anchor="nw", window = self.venus)
  
		self.uranusImage = PhotoImage(file=fileName(f"Images\\Uranus.png"))
		self.uranus = AstroButtons(root=self.astro, name="Uranus",function="+1 FAI +2 Light ATK",imageneeded=self.uranusImage, cmd=lambda:self.submitChange("uranus"))
		self.astroCanvas.create_window(129,4 , anchor="nw", window = self.uranus)

		self.saturnImage = PhotoImage(file=fileName(f"Images\\Saturn.png"))
		self.saturn = AstroButtons(root=self.astro, name="Saturn",function="+1 CEL +2 Wind ATK",imageneeded=self.saturnImage, cmd=lambda:self.submitChange("saturn"))
		self.astroCanvas.create_window(193,67 , anchor="nw", window = self.saturn)
  
		self.mercuryImage = PhotoImage(file=fileName(f"Images\\Mercury.png"))
		self.mercury = AstroButtons(root=self.astro, name="Mercury",function="+1 VIT +2 Water ATK",imageneeded=self.mercuryImage, cmd=lambda:self.submitChange("mercury"))
		self.astroCanvas.create_window(66,196, anchor="nw", window = self.mercury)

		self.noSignImage = PhotoImage(file=fileName(f"Images\\NoSign.png"))
		self.noSign = AstroButtons(root=self.astro, name="NoSign",function="",imageneeded=NULL, cmd=lambda:self.submitChange("noSign"))
		pixel = PhotoImage(width=1, height=1)
		self.noSign.configure(width=90,height=34,compound="left",image=self.noSignImage,text="No sign")
		self.astroCanvas.create_window(4,272, anchor="nw", window = self.noSign)
class AstroButtons(Button):
	def __new__(cls,root,name,function,imageneeded,cmd):
		if imageneeded != NULL:
			return Button(root,text=f"{name} {function}",image=imageneeded,borderwidth=0,command=cmd)
		else:
			return Button(root,text=f"{name} {function}",borderwidth=0,command=cmd)
		