from asyncio.windows_events import NULL
import sqlite3
from tkinter import E, W, Button, IntVar, Label, PhotoImage, StringVar
from Classes.tkentrycomplete import AutocompleteCombobox
from databaseInfo import fileName

class LegendExtend():
	def __init__(self,root, name, relatedstat, row, column, modHandler):
		self.previousValue = 0
		self.statToChange = relatedstat
		self.leName = name
		self.generateButton(root=root,name=name, row=row,column=column)
		self.parent = modHandler
	def generateButton(self, root, name, row, column):
		namesake = f"Images\\{name}"
		self.offImage = PhotoImage(file = fileName(f"{namesake}Off.png"))
		self.onImage = PhotoImage(file = fileName(f"{namesake}On.png"))
		self.currentValue = IntVar(value=0)
		self.button = Button(root, image=self.offImage, command=lambda:self.updateDisplay(self.currentValue.get()),borderwidth=0,anchor=W)
		self.button.grid(row=row,column=column,sticky=W)
	def updateDisplay(self, active):
		stats = self.parent.person.statHandler
		self.changeValue(active)
		if self.leName == "All":
			self.parent.tickAll(toggle=active)
		if active:
			self.changeMod(num=-1)
		else:
			self.changeMod(num=1)
		stats.updateAll()
		self.parent.person.updateAll()
		self.previousValue = active
	def changeValue(self, active):
		if active:
			self.currentValue.set(0)
			self.button.configure(image=self.offImage)
		else:
			self.currentValue.set(1)
			self.button.configure(image=self.onImage)
	def changeMod(self, num):
		if self.leName!="All":
			stats = self.parent.person.statHandler
			stat = getattr(stats, self.statToChange)
			setattr(stat, "hiddenBase", (getattr(stat, "hiddenBase") + num))
class ModHandler:
	list1 = ["AxysAl",
		"BldiIa",
		"ChoirEr",
		"GrenUt",
		"HolyMr",
		"KagiJi",
		"KashIc",
		"RabeUr",
		"ZeroGy",
		"LunaCu",
		"AkurZo",
		"All"]
	list2 = {"AxysAl":"strength",
		"BldiIa":"vitality",
		"ChoirEr":"resistance",
		"GrenUt":"defense",
		"HolyMr":"faith",
		"KagiJi":"luck",
		"KashIc":"will",
		"RabeUr":"celerity",
		"ZeroGy":"skill",
		"LunaCu":"sanctity",
		"AkurZo":"guile",
		"All":"none"
	}
	def __init__(self,root, char):
		self.person = char
		self.AxysAl = NULL
		self.Blidila = NULL
		self.ChoirEr = NULL
		self.GrenUt = NULL
		self.HolyMr = NULL
		self.KagiJi = NULL
		self.Kashlc = NULL
		self.RabeUr = NULL
		self.ZeroGy = NULL
		self.LunaCu = NULL
		self.AkurZo = NULL
		self.All = NULL
		self.currentTalent = NULL
		currentRow = 0
		currentCol = 0
		for num, name in enumerate(ModHandler.list1):
			if(num < 3):
				currentCol = num
			else:
				currentCol = num%3
			if num%3 == 0 and num != 0:
				currentCol = num%3
				currentRow += 1
			setattr(self, name, LegendExtend(root=root, name=name, relatedstat=ModHandler.list2[name],row = currentRow,column=currentCol,modHandler=self))
	def tickAll(self, toggle):
		number = -1 if toggle else 1
		for num, name in enumerate(ModHandler.list1):
			if name == "All": continue
			getattr(self, name).changeValue(active=toggle)
			getattr(self, name).changeMod(num=number)
		self.person.statHandler.updateAll()
		self.person.updateAll()


	