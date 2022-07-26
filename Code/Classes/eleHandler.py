from asyncio.windows_events import NULL
import tkinter
from Classes.statClasses import *


class EleHandler:
	def __init__(self, parent,pixel,person):
		self.eleATK = {"fire":0, "ice":0,"wind":0,"earth":0,"dark":0,"water":0,"light":0,"lightning":0, "acid":0,"sound":0}
		self.eleRES = {"fire":0, "ice":0,"wind":0,"earth":0,"dark":0,"water":0,"light":0,"lightning":0, "acid":0,"sound":0}
		self.eleFrame = ttk.Frame(parent)
		self.eleFrame.grid(row=6,column=1,sticky=W)
		textFrame = ttk.Frame(parent)
		textFrame.grid(row=5,column=1,sticky=W)
		self.text = Label(textFrame, text="ElemATK")
		self.text.grid(row=0,column=0)
		for key, value in self.eleATK.items():
			self.eleATK[key] = eleStat(base=0,name=key)
		for key, value  in self.eleRES.items():
			self.eleRES[key] = eleStat(base=0,name=key)
		index=0
		statIndex=0
		for key, value in self.eleATK.items():
			self.eleATK[key].handlerRef = self
			if index==1:
				blank = Label(self.eleFrame, text="Luminary Element")
				blank.grid(row=index, column=2)
				lumEle = Checkbutton(self.eleFrame)
				lumEle.grid(row=index, column=1)
				self.eleATK[key].addWidgets(parent=self.eleFrame,offsetRow=2,offsetColumn=0)
				self.eleATK[key].addStats(holder=self.eleFrame,offsetRow=2,offsetColumn=0,pixel=pixel,name=key,stat=statHandler.sloppyList[2],handler=self)
				index+=2
			else:
				self.eleATK[key].addWidgets(parent=self.eleFrame,offsetRow=index,offsetColumn=0)
				self.eleATK[key].addStats(holder=self.eleFrame,offsetRow=index,offsetColumn=0,pixel=pixel,name=key,stat=statHandler.sloppyList[index],handler=self)
				index+=1
		blank1 = Label(self.eleFrame, text="")
		blank1.grid(row=11,column=0)
		self.thePlayer = person
	def updateALL(self):
		for key, value in self.eleATK.items():
			self.eleATK[key].updateDisplay()


class eleStat(stat):
	def __init__(self, base, name):
		super().__init__(base, name)
		self.refStat = 0
		self.handlerRef = NULL
	def updateDisplay(self): # new number is the update display one 
		statAtk = int(getattr(self.handlerRef.thePlayer.statHandler, self.refStat).getScaled())
		willBonus = int(getattr(self.handlerRef.thePlayer.statHandler, "will").getScaled()/4)
		setattr(self,"base",statAtk + willBonus + self.baseMod)
		self.display.config(text=f"{self.base+self.customMod}")
	def update_modifiers(self):
		value = int(self.customModValue.get())
		setattr(self, "customMod", value)
		self.updateDisplay()
	def addStats(self, offsetRow, offsetColumn, pixel, name, stat, holder,handler):
		self.Icon = Label(holder, text=name)
		self.Icon.grid(row=offsetRow, column=offsetColumn)
		self.display = Label(holder, text="0",width=4)
		self.display.grid(row=offsetRow,column=offsetColumn+1)
		self.refStat = stat
		print(self.refStat)
	def addWidgets(self, parent, offsetRow, offsetColumn):
		self.customModValue = StringVar(value=0)
		self.customMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f',width=6,wrap=True,justify=LEFT,
                            command=self.update_modifiers,textvariable=self.customModValue,stat="readonly")
		self.customMods.grid(row=offsetRow,column=offsetColumn+2)
		self.customMods.configure(justify=LEFT)
		self.customMods.xview_moveto(1)