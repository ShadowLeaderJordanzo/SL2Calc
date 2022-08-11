from asyncio.windows_events import NULL
from msilib import init_database
from tkinter import *
from functools import partial
import math
from tkinter import ttk
from tkinter.tix import *
class statHandler: # looks pretty ugly
	points = 240
	sloppyList = ["strength","will","skill","celerity","defense","resistance","vitality","faith","luck","guile","sanctity","aptitude"]
	def __init__(self, stats, parent, pixel, person,root):
		if len(stats) > 0:
			self.strength = stats[0]
			self.will = stats[1]
			self.skill = stats[2]
			self.celerity = stats[3]
			self.defense = stats[4]
			self.resistance = stats[5]
			self.vitality = stats[6]
			self.faith = stats[7]
			self.luck = stats[8]
			self.guile = stats[9]
			self.sanctity = stats[10]
			self.aptitude = stats[11]
			# maybe just like a frame function, no matter what i do i seem to bloat code with the frame - > label -> grid movement and it makes a function look ugly
			textFrame = ttk.Frame(root)
			textFrame.grid(row=5,column=0,sticky=W)
			self.pointsRemaining = Label(textFrame, text=f"{statHandler.points} Points Remaining",)
			self.pointsRemaining.grid(row=0,column=0,sticky=W)
			displayRand = Label(textFrame, text="",padx=13)
			displayRand.grid(row=0,column=1)
			self.modsDisplay1 = Label(textFrame, text="Custom Mod",padx=5)
			self.modsDisplay1.grid(row=0,column=2,sticky=W)
			self.modsDisplay2 = Label(textFrame, text="Base Mod",padx=0)
			self.modsDisplay2.grid(row=0,column=3,sticky=W)
			for columns in range(textFrame.grid_size()[0]):
				textFrame.columnconfigure(columns,weight=1)
			self.statFrame = ttk.Frame(parent)
			self.statFrame.grid(row=0,column=0,sticky=W)
			index = 5
			for arg in vars(self):
				if arg in statHandler.sloppyList:
					index+=1
					namesake = arg[:1].upper()
					namesake = namesake + arg[1:]
					getattr(self, arg).addStats(offsetRow=index, offsetColumn=0, pixel=pixel, name=namesake,handler=self,holder=self.statFrame)
					getattr(self, arg).addWidgets(parent=self.statFrame, offsetRow=index, offsetColumn=0)
					getattr(self, arg).handlerRef = self
			for columns in range(self.statFrame.grid_size()[0]):
				self.statFrame.columnconfigure(columns,weight=1)
		self.player = person
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
	def assignClassStats(self, results,columns, main):
		index=0
		for name in columns:
			if name == "name":
				index+=1
				continue
			increase = results[0][index]
			if increase == None: increase = 0
			increase = int(increase)
			currentVar = setattr(getattr(self, name),main, increase)
			index += 1
		self.updateAll()
	def assignClassBonus(self, results, columns, main):
		increase = results[0][1]
		index=2
		if main == 1:
			varName = "max"
		else: varName = "subMax"
		for name in columns:
			if name == "name" or name == "max":
				continue
			if results[0][index] == None:
				index+=1
				continue
			setattr(getattr(self,name),varName,increase)
			index+=1
		self.updateAll()
	def assignRaceStats(self, results, columns):
		index=0
		for name in columns:
			if name =="names":
				index+=1
				continue
			increase = results[0][index]
			increase = int(increase)
			currentVar = setattr(getattr(self,name), "base",increase)
			index += 1
		self.updateAll()
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
		self.mainClass = 0
		self.mClassBonus = 0
		self.sClassBonus = 0
		self.max = 0
		self.subMax = 0
		self.handlerRef = NULL
	def updateDisplay(self):
		totalStat = self.getTotal()
		totalSoftCap = self.getTotalSoftCap()
		if totalSoftCap >= totalStat:
			self.displayLabel.config(text=f"{totalStat}")
		else:
			self.displayLabel.config(text=f"{totalStat}({self.getScaled()})")
		self.checkAdptitude(handler=self.handlerRef)
		self.handlerRef.player.vitals.updateValues(stats=self.handlerRef)
		if self.name == "sanctity":
			self.handlerRef.player.eleHandler.updateValue(stat=self)
		self.handlerRef.player.updateAll()
	def getTotalNoMods(self):
		return self.base+self.invested+self.baseMod
	def getTotal(self):
			return self.base+self.invested+self.customMod+self.baseMod+self.mClassBonus+self.sClassBonus+self.aptMod+self.mainClass
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
		if totalStat > 0:
			while totalStat > 3:
				totalStat-=3
				currentStat += 3 * mod
				mod -= .08
				if mod < 0.1: mod =0.1
			currentStat += totalStat * mod
			return round(currentStat,2)
		else: return self.getTotal()
	def checkAdptitude(self,handler):
		if self.name == "aptitude":
			totalStat = self.getTotal()
			totalSoftCap = self.getTotalSoftCap()
			if totalSoftCap >= totalStat:
				if totalStat == 0: return
				if totalStat%6 == 0:
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
				if self.invested+num > 80: return
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
	# def adjustBalloonMsg(self,e):
	# 	self.nameBalloon.bind_widget(self.nameLabel, balloonmsg=self.getToolTip())
	def addStats(self, offsetRow, offsetColumn, pixel, name,handler,holder):
		attr_name = 'invested'
		self.plusButton = Button(holder, text="+",command=partial(self.add,attr_name, 1,1,handler),
			height=10,width=10, image=pixel, compound="c", repeatdelay=100, repeatinterval=100)
		self.minusButton = Button(holder, text="-",command=partial(self.sub, attr_name, 1,handler),
		height=10,width=10, image=pixel, compound="c", repeatdelay=100, repeatinterval=100)
		#+ and - buttons
		self.plusButton.grid(row=offsetRow, column=offsetColumn+2,sticky=W)
		self.minusButton.grid(row=offsetRow, column=offsetColumn+3,sticky=W)
		#stat name / values
		# iconHolder.grid(row=offsetRow, column=offsetColumn+6)
		self.nameLabel = Label(holder, text=name)
		self.displayLabel = Label(holder, text="0",width=7)
		self.nameLabel.grid(row=offsetRow,column=offsetColumn,sticky=W,pady=5)
		self.displayLabel.grid(row=offsetRow, column=offsetColumn+1,sticky=W)
		# self.nameBalloon = Balloon(holder)
		# self.nameLabel.bind("<Enter>", self.adjustBalloonMsg)
		# self.nameBalloon.bind_widget(self.nameLabel, balloonmsg=self.getToolTip())
	def addWidgets(self,parent, offsetRow, offsetColumn):
		#Mod names
		self.customModValue = StringVar(value=0)
		self.customMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f',width=6,wrap=True, command=self.update_modifiers,textvariable=self.customModValue)
		self.customMods.grid(row=offsetRow,column=offsetColumn+4,sticky=W,padx=15)
		self.customMods.xview_moveto(1)

		self.baseModValue = StringVar(value=0)
		self.baseMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f',width=6,wrap=True, command=self.update_modifiers,textvariable=self.baseModValue)
		self.baseMods.grid(row=offsetRow,column=offsetColumn+5,sticky=W,padx=5)
		self.baseMods.xview_moveto(1)

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