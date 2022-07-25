from re import S
from tkinter import *
from tkinter import ttk

from Classes.statClasses import statHandler


class Vital:
	def __init__(self, parent):
		self.health = 15
		self.focus = 10
		self.customHealth = 0
		self.customFocus = 0
		self.percentHealth = 100
		self.percentFocus = 100
		self.makeDisplay(handler=parent)
	def getMaxHealth(self):
		return int(round((self.health+self.customHealth) * ( self.percentHealth / 100 ),1))
	def getCurrentHealth(self):
		return round(self.health+self.customHealth,1)
	def getMaxFocus(self):
		return int(round((self.focus+self.customFocus) * ( self.percentFocus / 100 ),1))
	def getCurrentFocus(self):
		return self.focus+self.customFocus
	def addHealth(self, num):
		self.health+=num
	def addFocus(self, num):
		self.focus+=num
	def updateValues(self, stats):
		self.health = 15 + (round(stats.strength.getScaled()) * 3) + (240 - statHandler.points) + (round(stats.vitality.getScaled()) * 10) + (round(stats.sanctity.getScaled()) * 2)
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
		self.updateDisplay() 
	def checkBoxUpdate(self):
		print("update")
	def makeDisplay(self, handler):
		displayFrame = ttk.Frame(handler)
		displayFrame.columnconfigure(0,weight=1)
		displayFrame.grid(row=0,column=0,sticky=W)
  
		self.healthDisplay = Label(displayFrame, text=f"HP: {self.getCurrentHealth()}/{self.getMaxHealth()}", fg='#FF0000') 
		self.focusDisplay = Label(displayFrame, text=f"FP: {self.getCurrentFocus()}/{self.getMaxFocus()}", fg='#0000FF') 
  
		self.healthDisplay.grid(row=0,column=0,sticky=W)
		self.focusDisplay.grid(row=1,column=0,sticky=W)
  
		modFrame = ttk.Frame(handler)
		modFrame = ttk.Frame(handler)
		modFrame.columnconfigure(0,weight=1)
		modFrame.grid(row=0,column=1,sticky=EW)
  
		modLabel1 = Label(modFrame, text="Custom HP:")
		modLabel2 = Label(modFrame, text="Custom FP:")
  
		self.customHealthModValue = StringVar(value=0)
		self.customFocusModValue = StringVar(value=0)
		self.customHealthMod = Spinbox(modFrame, from_=-1000, to=1000, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.customHealthModValue)
		self.customFocusMod = Spinbox(modFrame, from_=-1000, to=1000, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.customFocusModValue)
  
		modLabel1.grid(row=0, column=0, sticky=EW)
		modLabel2.grid(row=1, column=0, sticky=EW)		
		self.customHealthMod.grid(row=0, column=1, sticky=EW)
		self.customFocusMod.grid(row=1, column=1, sticky=EW)
  
		percentFrame = ttk.Frame(handler)	
		percentFrame.columnconfigure(0,weight=1)
		percentFrame.grid(row=0,column=2,sticky=EW)
		self.percentHealthModValue = StringVar(value=100)
		self.percentFocusModValue = StringVar(value=100)		
		percentLabel1 = Label(percentFrame, text="Total HP%:")
		percentLabel2 = Label(percentFrame, text="Total FP%:")
		self.percentHealthMod = Spinbox(percentFrame, from_=0, to=200, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.percentHealthModValue)
		self.percentFocusMod = Spinbox(percentFrame, from_=0, to=200, increment=1, format='%10.0f', width=8,
									   command=self.updateModifiers, textvariable=self.percentFocusModValue)
		self.percentHealthMod.grid(row=0, column=1, sticky=EW)
		self.percentFocusMod.grid(row=1, column=1, sticky=EW)
		percentLabel1.grid(row=0, column=0, sticky=EW)
		percentLabel2.grid(row=1, column=0, sticky=EW)
		# break off into different function and split it up, can really really refactor / optimize all of this
		options = ttk.Frame(handler)
		options.columnconfigure(0,weight=1)
		options.grid(row=0,column=3,sticky=EW)
		giantLabel = Label(options,text="Giant Gene")
		fortLabel = Label(options,text="Fortitude")
		endLabel = Label(options,text="Endurance")
		warLabel = Label(options,text="Warwalk")
		giantLabel.grid(row=0,column=0, sticky=EW)
		fortLabel.grid(row=1,column=0, sticky=EW)
		endLabel.grid(row=0,column=2, sticky=EW)
		warLabel.grid(row=1,column=2, sticky=EW)
		self.giant = Checkbutton(options, command=self.checkBoxUpdate,onvalue='on',offvalue='off')
		self.fortitude = Checkbutton(options, command=self.checkBoxUpdate,onvalue='on',offvalue='off')
		self.endurance = Checkbutton(options, command=self.checkBoxUpdate,onvalue='on',offvalue='off')
		self.warwalk = Checkbutton(options, command=self.checkBoxUpdate,onvalue='on',offvalue='off')
		self.giant.grid(row=0,column=1,sticky=EW)
		self.fortitude.grid(row=1,column=1,sticky=EW)
		self.endurance.grid(row=0,column=3,sticky=EW)
		self.warwalk.grid(row=1,column=3,sticky=EW)
  
  
  
  # make this cleaner later, less repeated code, more functions to handle this all