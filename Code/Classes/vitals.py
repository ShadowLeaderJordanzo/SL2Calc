from asyncio.windows_events import NULL
from functools import partial
from tkinter import *
from tkinter import ttk
from Classes.statClasses import statHandler


class Vital:
	def __init__(self, parent,person):
		self.stats = person.statHandler
		self.health = 10
		self.focus = 10
		self.customHealth = 0
		self.customFocus = 0
		self.hiddenMods = 0
		self.hiddenFMods = 0 
		self.giantMod = 0
		self.hexerMod = 0
		self.percentHealth = 100
		self.percentFocus = 100
		self.hpShards = 0
		self.focusShards = 0
		self.afflictedSpectre = 0
		self.makeDisplay(handler=parent)
	def getMaxHealth(self):
		return int(self.getCurrentHealth() * ( self.percentHealth / 100 ))
	def getBaseHealth(self):
		return round(self.health+self.customHealth+self.hpShards+self.hiddenMods,1)
	def getCurrentHealth(self):
		health = self.getBaseHealth()
		health = health + int(health * 0.1) if self.giantMod else health
		health = health + int(health * 0.1) if self.hexerMod else health
		health = health + int(health * (0.05 * self.afflictedSpectre)) if self.afflictedSpectre>0 else health
		return int(health)
	def getGiantMod(self):
		if self.giantMod:
			return int((self.health+self.customHealth+self.hpShards+self.hiddenMods) * 0.1)
		else: return 0
	def getMaxFocus(self):
		return int(self.getCurrentFocus() * ( self.percentFocus / 100 ))
	def getCurrentFocus(self):
		return self.focus+self.customFocus+self.focusShards+self.hiddenFMods
	def addHealth(self, num):
		self.health+=num
	def addFocus(self, num):
		self.focus+=num
	def painTolerance(self, prevnum, nextnum):
		self.hiddenMods-=prevnum
		self.hiddenMods+=nextnum
		self.updateDisplay()
	def updateCapacity(self, num):
		self.hiddenFMods-=self.capacityFormerValue
		self.hiddenFMods+=num
		self.capacityFormerValue = num
		self.updateDisplay()
	def updateValues(self, stats):
		self.health = 12 + (round(stats.strength.invested) * 3) + (240 - statHandler.points) + (round(stats.vitality.getScaled()) * 10) + (round(stats.sanctity.getScaled()) * 2)
		self.focus = 10 + (round(stats.will.getScaled()) * 5) + (round(stats.faith.getScaled()) * 3) + (round(stats.sanctity.getScaled()) * 2)
		self.updateDisplay()
	def updateDisplay(self):
		self.healthDisplay.config(text=f"HP: {self.getCurrentHealth()}/{self.getMaxHealth()}")
		self.focusDisplay.config(text=f"FP: {self.getCurrentFocus()}/{self.getMaxFocus()}") 
	def updateModifiers(self):
		value = int(self.customHealthMod.get())
		setattr(self, "customHealth", value)
		value = int(self.customFocusMod.get())
		setattr(self, "customFocus", value)
		value = int(self.percentHealthMod.get())
		setattr(self, "percentHealth", value)
		value = int(self.percentFocusMod.get())
		setattr(self, "percentFocus", value)
		value = int(self.hpShardMod.get())
		setattr(self, "hpShards", value)
		value = int(self.focusShardMod.get())
		setattr(self, "focusShards", value)
		self.updateDisplay() 
	def checkBoxUpdate(self, modifier, name, giant,endurance):
		Var = getattr(self, name)
		if Var.get(): Var = 1
		else: Var = 0
		if giant:
			if Var: self.giantMod = 1
			else: self.giantMod = 0 
		else:
			if endurance:
				if Var: self.hexerMod = 1
				else: self.hexerMod = 0 
			if Var:
				self.hiddenMods += modifier
				if name == "warValue": self.hiddenFMods += modifier
			else:
				if name == "warValue": self.hiddenFMods -= modifier
				self.hiddenMods -=modifier
		self.updateDisplay()
	def makeDisplay(self, handler):
		displayFrame = ttk.Frame(handler) 
		displayFrame.grid(row=0,column=0,sticky=W,columnspan=9)
  
		self.healthDisplay = Label(displayFrame, text=f"HP: {self.getCurrentHealth()}/{self.getMaxHealth()}", fg='#FF0000') 
		self.focusDisplay = Label(displayFrame, text=f"FP: {self.getCurrentFocus()}/{self.getMaxFocus()}", fg='#0000FF') 
  
		self.healthDisplay.grid(row=0,column=0,sticky=W)
		self.focusDisplay.grid(row=1,column=0,sticky=W)
  
		modFrame = ttk.Frame(handler)
		modFrame = ttk.Frame(handler)
		modFrame.columnconfigure(0,weight=1)
		modFrame.grid(row=0,column=1,sticky=EW)
  
		modLabel1 = Label(displayFrame, text="Custom HP:")
		modLabel2 = Label(displayFrame, text="Custom FP:")
  
		self.customHealthModValue = StringVar(value=0)
		self.customFocusModValue = StringVar(value=0)
		self.customHealthMod = Spinbox(displayFrame, from_=-1000, to=1000, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.customHealthModValue)
		self.customFocusMod = Spinbox(displayFrame, from_=-1000, to=1000, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.customFocusModValue)
  
		modLabel1.grid(row=0, column=1, sticky=EW)
		modLabel2.grid(row=1, column=1, sticky=EW)		
		self.customHealthMod.grid(row=0, column=2, sticky=EW)
		self.customFocusMod.grid(row=1, column=2, sticky=EW)
  
		self.percentHealthModValue = StringVar(value=100)
		self.percentFocusModValue = StringVar(value=100)		
		percentLabel1 = Label(displayFrame, text="Total HP%:")
		percentLabel2 = Label(displayFrame, text="Total FP%:")
		self.percentHealthMod = Spinbox(displayFrame, from_=0, to=200, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.percentHealthModValue)
		self.percentFocusMod = Spinbox(displayFrame, from_=0, to=200, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.percentFocusModValue)
		self.percentHealthMod.grid(row=0, column=4, sticky=EW)
		self.percentFocusMod.grid(row=1, column=4, sticky=EW)
		percentLabel1.grid(row=0, column=3, sticky=EW)
		percentLabel2.grid(row=1, column=3, sticky=EW)
  
  
		self.hpShardValue = StringVar(value=0)
		self.focusShardValue = StringVar(value=0)
		shardLabel1 = Label(displayFrame,text="HPShard:")
		shardLabel2 = Label(displayFrame,text="FPShard:")
		self.hpShardMod = Spinbox(displayFrame, from_=0, to=45, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.hpShardValue)
		self.focusShardMod = Spinbox(displayFrame, from_=0, to=45, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.focusShardValue)
		shardLabel1.grid(row=0,column=9)
		shardLabel2.grid(row=1,column=9)
		self.hpShardMod.grid(row=0, column=10)
		self.focusShardMod.grid(row=1, column=10)
  
		Label(displayFrame,text="Capacity: " ).grid(row=1,column=11,sticky=W)
		self.capacityValue = IntVar(value=0)
		self.capacityFormerValue = 0 
		self.capacity = Spinbox(displayFrame, from_=0, to=25, increment=5,format='%10.0f',width=6, command=lambda:self.updateCapacity(self.capacityValue.get()),textvariable=self.capacityValue, wrap=False)
		self.capacity.grid(row=1,column=12,sticky=W)
  
		# break off into different function and split it up, can really really refactor / optimize all of this
		Label(displayFrame,text="Giant Gene").grid(row=0,column=5, sticky=EW)
		Label(displayFrame,text="Fortitude").grid(row=1,column=5, sticky=EW)
		Label(displayFrame,text="Endurance").grid(row=0,column=7, sticky=EW)
		Label(displayFrame,text="Warwalk").grid(row=1,column=7, sticky=EW)
		self.giantValue =  IntVar(value=0)
		self.giant = Checkbutton(displayFrame, variable=self.giantValue,command=partial(self.checkBoxUpdate, 0,"giantValue",1, 0),onvalue=1,offvalue=0)
		self.fortValue = IntVar(value=0)
		self.fortitude = Checkbutton(displayFrame, variable=self.fortValue, command=partial(self.checkBoxUpdate, 75, "fortValue", 0,0),onvalue=1,offvalue=0)
		self.endValue = IntVar(value=0)
		self.endurance = Checkbutton(displayFrame, variable=self.endValue, command=partial(self.checkBoxUpdate, 0, "endValue", 0,1),onvalue=1,offvalue=0)
		self.warValue = IntVar(value=0)
		self.warwalk = Checkbutton(displayFrame, variable=self.warValue, command=partial(self.checkBoxUpdate, 20, "warValue", 0,0),onvalue=1,offvalue=0)
		self.giant.grid(row=0,column=6,sticky=EW)
		self.fortitude.grid(row=1,column=6,sticky=EW)
		self.endurance.grid(row=0,column=8,sticky=EW)
		self.warwalk.grid(row=1,column=8,sticky=EW)
		for columns in range(displayFrame.grid_size()[0]):
			displayFrame.columnconfigure(columns,weight=1)
  
  
  # make this cleaner later, less repeated code, more functions to handle this all