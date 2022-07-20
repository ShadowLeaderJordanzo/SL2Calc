from msilib import init_database
from tkinter import *
from functools import partial
class statHandler:
	points = 240
	def __init__(self, stats, parent, pixel):
		if len(stats) > 0:
			self.strength = stats[0].addWidgets(parent=parent,offsetRow=3,offsetColumn=2,pixel=pixel,name="Strength", handler=self)
			self.will = stats[1].addWidgets(parent=parent,offsetRow=4,offsetColumn=2,pixel=pixel,name="Will", handler=self)
			self.skill = stats[2].addWidgets(parent=parent,offsetRow=5,offsetColumn=2,pixel=pixel,name="Skill", handler=self)
			self.celerity = stats[3].addWidgets(parent=parent,offsetRow=6,offsetColumn=2,pixel=pixel,name="Celerity", handler=self)
			self.defense = stats[4].addWidgets(parent=parent,offsetRow=7,offsetColumn=2,pixel=pixel,name="Defense", handler=self)
			self.reistance = stats[5].addWidgets(parent=parent,offsetRow=8,offsetColumn=2,pixel=pixel,name="Resistance", handler=self)
			self.vitality = stats[6].addWidgets(parent=parent,offsetRow=9,offsetColumn=2,pixel=pixel,name="Vitality", handler=self)
			self.faith = stats[7].addWidgets(parent=parent,offsetRow=10,offsetColumn=2,pixel=pixel,name="Faith", handler=self)
			self.luck = stats[8].addWidgets(parent=parent,offsetRow=11,offsetColumn=2,pixel=pixel,name="Luck", handler=self)
			self.guile = stats[9].addWidgets(parent=parent,offsetRow=12,offsetColumn=2,pixel=pixel,name="Guile", handler=self)
			self.sanctity = stats[10].addWidgets(parent=parent,offsetRow=13,offsetColumn=2,pixel=pixel,name="Sanctity", handler=self)
			self.aptitude = stats[11].addWidgets(parent=parent,offsetRow=14,offsetColumn=2,pixel=pixel,name="Aptitude", handler=self)
			self.pointsRemaining = Label(parent, text=f"{statHandler.points} Points Remaining",)
			self.pointsRemaining.grid(row=1,column=0,sticky='wsn')
			self.modsDisplay = Label(parent, text="Custom Modifiers" + "    " + "Base Modifiers")
			self.modsDisplay.grid(row=1,column=4,sticky=NSEW, columnspan=2)
			self.whoops = Label(parent, width=5)
			self.whoops.grid(row=1,column=7,sticky=NSEW,rowspan=13)
	def reducePoints(self, num):
		if statHandler.points-num < 0: return 0
		statHandler.points -= num
		return 1
	
class stat:
	softCapOffset = 40 # 40+base
	hardCap = 80 # cant go more than this in invested
	def __init__(self, base):
		self.base = base
		self.invested = 0
		self.customMod = 0
		self.baseMod = 0
	def updateDisplay(self):
		self.displayLabel.config(text=f"{self.base+self.invested+self.customMod+self.baseMod}")
	def add(self, choice, num, hardCap,handler):
		currentValue = getattr(self,choice)
		if num == 0: num = 1
		if handler.reducePoints(num=num) == 1:
			if hardCap == 1:
				if currentValue+num > 80: return
			setattr(self, choice, currentValue + num)
			self.updateDisplay()
			handler.pointsRemaining.config(text=f"{statHandler.points} Points Remaining")
	def sub(self, choice, num, handler):
		currentValue = getattr(self,choice)
		if currentValue-num < 0: return
		setattr(self, choice, currentValue-num)
		statHandler.points += num
		self.updateDisplay()
		handler.pointsRemaining.config(text=f"{statHandler.points} Points Remaining")
	def update_modifiers(self):
		print(self.baseMods.get())
		value = int(self.baseModValue.get())
		setattr(self, "baseMod", value)
		value = int(self.customModValue.get())
		setattr(self, "customMod", value)
		self.updateDisplay()
	def addWidgets(self,parent, offsetRow, offsetColumn,pixel,name,handler):
		attr_name = 'invested'
		self.plusButton = Button(parent, text="+",command=partial(self.add,attr_name, 1,1,handler),
			height=10,width=10, image=pixel, compound="c", repeatdelay=50, repeatinterval=50)
		self.minusButton = Button(parent, text="-",command=partial(self.sub, attr_name, 1,handler),
		height=10,width=10, image=pixel, compound="c", repeatdelay=50, repeatinterval=50)
		self.plusButton.grid(row=offsetRow, column=offsetColumn, padx=5,sticky=NSEW)
		self.minusButton.grid(row=offsetRow, column=offsetColumn+1,sticky=NSEW)

		self.nameLabel = Label(parent, text=name, padx=5)
		self.displayLabel = Label(parent, text="0")
		self.nameLabel.grid(row=offsetRow,column=0,sticky='wsn')
		self.displayLabel.grid(row=offsetRow, column=1,sticky='wsn')
		self.customModValue = StringVar(value=0)
		self.customMods = Spinbox(parent, from_=0,to=100,increment=1,format='%10.0f',width=8, command=self.update_modifiers,textvariable=self.customModValue)
		self.customMods.grid(row=offsetRow,column=offsetColumn+2,sticky=E)
		self.baseModValue = StringVar(value=0)
		self.baseMods = Spinbox(parent, from_=0,to=100,increment=1,format='%10.0f',width=8, command=self.update_modifiers,textvariable=self.baseModValue)
		self.baseMods.grid(row=offsetRow,column=offsetColumn+3,sticky=E)