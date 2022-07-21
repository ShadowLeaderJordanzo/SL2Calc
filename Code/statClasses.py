from msilib import init_database
from tkinter import *
from functools import partial
import math
from tkinter.tix import *
class statHandler: # looks pretty ugly
	points = 240
	def __init__(self, stats, parent, pixel):
		if len(stats) > 0:
			self.strength = stats[0].addWidgets(parent=parent,offsetRow=3,offsetColumn=2,pixel=pixel,name="Strength", handler=self)
			self.will = stats[1].addWidgets(parent=parent,offsetRow=4,offsetColumn=2,pixel=pixel,name="Will", handler=self)
			self.skill = stats[2].addWidgets(parent=parent,offsetRow=5,offsetColumn=2,pixel=pixel,name="Skill", handler=self)
			self.celerity = stats[3].addWidgets(parent=parent,offsetRow=6,offsetColumn=2,pixel=pixel,name="Celerity", handler=self)
			self.defense = stats[4].addWidgets(parent=parent,offsetRow=7,offsetColumn=2,pixel=pixel,name="Defense", handler=self)
			self.resistance = stats[5].addWidgets(parent=parent,offsetRow=8,offsetColumn=2,pixel=pixel,name="Resistance", handler=self)
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
			self.strength.handlerRef = self
	def setParents(self):
		self.strength.handlerRef = self
		self.will.handlerRef = self
		self.skill.handlerRef = self
		self.celerity.handlerRef = self
		self.defense.handlerRef = self
		self.resistance.handlerRef = self
		self.vitality.handlerRef = self
		self.faith.handlerRef = self
		self.luck.handlerRef = self
		self.guile.handlerRef = self
		self.sanctity.handlerRef = self
		self.aptitude.handlerRef = self
	def reducePoints(self, num):
		if statHandler.points-num < 0: return 0
		statHandler.points -= num
		return 1
	def adjustAptMods(self, amount):
		amount = int(amount)
		setattr(self.strength, "aptMod", amount)
		setattr(self.will, "aptMod", amount)
		setattr(self.skill, "aptMod", amount)
		setattr(self.celerity, "aptMod", amount)
		setattr(self.defense, "aptMod", amount)
		setattr(self.sanctity, "aptMod", amount)
		setattr(self.guile, "aptMod", amount)
		setattr(self.luck, "aptMod", amount)
		setattr(self.faith, "aptMod", amount)
		setattr(self.vitality, "aptMod", amount)
		setattr(self.resistance, "aptMod", amount)
		self.updateAll()
	def updateAll(self):
		self.strength.updateDisplay()
		self.will.updateDisplay()
		self.skill.updateDisplay()
		self.celerity.updateDisplay()
		self.defense.updateDisplay()
		self.resistance.updateDisplay()
		self.vitality.updateDisplay()
		self.faith.updateDisplay()
		self.luck.updateDisplay()
		self.guile.updateDisplay()
		self.sanctity.updateDisplay()
		

	
class stat:
	softCapOffset = 40 # 40+base
	hardCap = 80 # cant go more than this in invested
	def __init__(self, base, name,):
		self.name = name
		self.base = base
		self.invested = 0
		self.customMod = 0
		self.baseMod = 0
		self.aptMod = 0
		self.additonalMod = 0 #classes
	def updateDisplay(self):
		realStat = self.base+self.invested+self.customMod+self.baseMod+self.additonalMod+self.aptMod
		totalStat = self.getTotal()
		totalSoftCap = self.getTotalSoftCap()
		if totalSoftCap >= totalStat:
			self.displayLabel.config(text=f"{totalStat}")
		else:
			self.displayLabel.config(text=f"{realStat}({self.getScaled()})")
		self.checkAdptitude(handler=self.handlerRef)
	def getTotal(self):
			return self.base+self.invested+self.customMod+self.baseMod+self.additonalMod+self.aptMod
	def getTotalSoftCap(self):
			return stat.softCapOffset + self.base + self.baseMod
	def getBaseInvested(self):
			return self.base+self.baseMod + self.invested
	def getToolTip(self):
			return f"{self.base+self.baseMod} + {self.invested}"
	def getScaled(self):
		totalStat = self.getTotal()
		totalSoftCap = self.getTotalSoftCap()
		currentStat = totalSoftCap
		totalStat-=totalSoftCap
		mod = 0.9
		while totalStat > 3:
			totalStat-=3
			currentStat += 3 * mod
			mod -= .08
			if mod < 0.1: mod =0.1
		currentStat += totalStat * mod
		return round(currentStat,2)

	def checkAdptitude(self,handler):
		if self.name == "aptitude":
			totalStat = self.getTotal()
			totalSoftCap = self.getTotalSoftCap()
			if totalSoftCap >= totalStat:
				if totalStat == 0: return
				if totalStat%6 == 0:
					print(totalStat%6)
					handler.adjustAptMods(amount=totalStat/6)
				else:
					if (totalStat/6)-int(totalStat/6)==0:
						handler.adjustAptMods(amount=totalStat/6)
					else:
						handler.adjustAptMods(amount=int(totalStat)/6)
			else:
				if self.getScaled()%6 < 1:
					handler.adjustAptMods(amount=round(int(self.getScaled()/6)))
					# handler.updateAll()
				else:
					handler.adjustAptMods(amount=round(int(self.getScaled()/6)))
	def add(self, choice, num, hardCap,handler):
		currentValue = self.getBaseInvested()
		if num == 0: num = 1
		if handler.reducePoints(num=num) == 1:
			if hardCap == 1:
				if currentValue+num > 80: return
			setattr(self, choice, self.invested + num)
			self.updateDisplay()
			handler.pointsRemaining.config(text=f"{statHandler.points} Points Remaining")
	def sub(self, choice, num, handler):
		currentValue = getattr(self,choice)
		if currentValue-num < 0: return
		self.updateDisplay()
		setattr(self, choice, currentValue-num)
		statHandler.points += num
		self.updateDisplay()
		handler.pointsRemaining.config(text=f"{statHandler.points} Points Remaining")
	def update_modifiers(self):
		value = int(self.baseModValue.get())
		setattr(self, "baseMod", value)
		value = int(self.customModValue.get())
		setattr(self, "customMod", value)
		self.updateDisplay()
		# self.handlerRef.updateAll(self=self.handlerRef)
	def adjustBalloonMsg(self,e):
		self.nameBalloon.bind_widget(self.nameLabel, balloonmsg=self.getToolTip())
	def addWidgets(self,parent, offsetRow, offsetColumn,pixel,name,handler):
		attr_name = 'invested'
		self.plusButton = Button(parent, text="+",command=partial(self.add,attr_name, 1,1,handler),
			height=10,width=10, image=pixel, compound="c", repeatdelay=100, repeatinterval=100)
		self.minusButton = Button(parent, text="-",command=partial(self.sub, attr_name, 1,handler),
		height=10,width=10, image=pixel, compound="c", repeatdelay=100, repeatinterval=100)
		#+ and - buttons
		self.plusButton.grid(row=offsetRow, column=offsetColumn, padx=5,sticky=NSEW)
		self.minusButton.grid(row=offsetRow, column=offsetColumn+1,sticky=NSEW)
		#stat name / values
		self.nameLabel = Label(parent, text=name, padx=5)
		self.displayLabel = Label(parent, text="0")
		self.nameLabel.grid(row=offsetRow,column=0,sticky='wsn')
		self.displayLabel.grid(row=offsetRow, column=1,sticky='wsn')
		self.nameBalloon = Balloon(parent)
		self.nameLabel.bind("<Enter>", self.adjustBalloonMsg)
		self.nameBalloon.bind_widget(self.nameLabel, balloonmsg=self.getToolTip())
		#Mod names
		self.customModValue = StringVar(value=0)
		self.customMods = Spinbox(parent, from_=0,to=100,increment=1,format='%10.0f',width=8, command=self.update_modifiers,textvariable=self.customModValue)
		self.customMods.grid(row=offsetRow,column=offsetColumn+2,sticky=E)

		self.baseModValue = StringVar(value=0)
		self.baseMods = Spinbox(parent, from_=0,to=100,increment=1,format='%10.0f',width=8, command=self.update_modifiers,textvariable=self.baseModValue)
		self.baseMods.grid(row=offsetRow,column=offsetColumn+3,sticky=E)
		return self

# trid to reverse the equation
#
#	equation = 1.08**(math.floor((totalStat-totalSoftCap)/4))  # essentially the modifier, while > 3 = 0.08
#		self.displayLabel.config(text=f"{totalStat}")
#		if totalStat > stat.softCapOffset + self.base +self.baseMod:
#			if totalStat - totalSoftCap < 4:
#				self.displayLabel.config(text=f"{totalStat}({totalSoftCap+(totalStat-totalSoftCap) * 0.9})")
#			else:
#				effectiveStat = totalSoftCap+((43-totalSoftCap) * 0.9)
#				equation = 0.9-(equation-1)
#				equation = math.ceil(equation*100.0)/100.0
#				shownStat = (effectiveStat + (totalStat-(totalSoftCap+3)) * equation)
#	self.displayLabel.config(text=f"{totalStat}([{equation}]{round(shownStat, 2)})")