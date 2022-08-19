from asyncio.windows_events import NULL
import tkinter
from Classes.statClasses import *
from tkinter import *  
from PIL import Image,ImageTk

from Classes.atkHandler import trackerStat
from databaseInfo import *

class EleHandler:
	def __init__(self, parent,pixel,person,root):
		self.eleATK = {"fire":0, "ice":0,"wind":0,"earth":0,"dark":0,"water":0,"light":0,"lightning":0, "acid":0,"sound":0}
		self.eleRES = {"fire":0, "ice":0,"wind":0,"earth":0,"dark":0,"water":0,"light":0,"lightning":0, "acid":0,"sound":0}
		self.eleFrame = ttk.Frame(parent)
		self.eleFrame.grid(row=0,column=1,sticky=W)
		self.text = Label(person.statHandler.textFrame, text="EleATK")
		self.text.grid(row=0,column=4,sticky=W)
		for key, value in self.eleATK.items():
			self.eleATK[key] = eleStat(base=0,name=key)
		for key, value  in self.eleRES.items():
			self.eleRES[key] = trackerStat(base=0,name=key)
		Label(self.eleFrame, text="",image=pixel,height=26).grid(row=11,column=0,sticky=W)
		self.generateEleAtks(pixel = pixel)
		self.generateEleDefs(pixel=pixel)
		self.thePlayer = person
		for columns in range(self.eleFrame.grid_size()[0]):
			self.eleFrame.columnconfigure(columns,weight=1)
	def getBonus(self, element):
		stats = self.thePlayer.statHandler
		if self.lumEleValue != 1: # we will handle the handling of lum ele later
			match element:
				case "fire":
					return stats.strength.getScaled()
				case "ice":
					return stats.skill.getScaled()
				case "wind":
					return stats.celerity.getScaled()
				case "earth":
					return stats.defense.getScaled()
				case "dark":
					return stats.resistance.getScaled()
				case "water":
					return stats.vitality.getScaled()
				case "light":
					return stats.faith.getScaled()
				case "lightning":
					return stats.luck.getScaled()
				case "acid":
					return stats.guile.getScaled()
				case "sound":
					return stats.sanctity.getScaled()
	def updateAll(self):
		bonus = 0
		for key, value in self.eleATK.items():
			bonus = self.getBonus(element = key)
			self.eleATK[key].updateDisplay(eleBonus=bonus)
		for key, value  in self.eleRES.items():
			self.eleRES[key].display.config(text=f"{self.eleRES[key].base}%")
	def updateValue(self, stat):
		bonus = int(stat.getScaled()/6)
		for key, value  in self.eleRES.items():
			self.eleRES[key].base = bonus
	def generateEleAtks(self, pixel):
		index = 0 
		for key, value in self.eleATK.items():
			self.eleATK[key].handlerRef = self
			if index==1:
				blank = Label(self.eleFrame, text="Luminary Element")
				blank.grid(row=index, column=2,sticky=W)
				self.lumEleValue = IntVar(value=0)
				self.lumEle = Checkbutton(self.eleFrame,variable=self.lumEleValue)
				self.lumEle.grid(row=index, column=1,sticky=W)
				Label(self.eleFrame, image=pixel,height=26).grid(row=index,column=0,sticky=W)
				self.eleATK[key].addWidgets(parent=self.eleFrame,offsetRow=2,offsetColumn=0)
				self.eleATK[key].addStats(holder=self.eleFrame,offsetRow=2,offsetColumn=0,pixel=pixel,name=key,stat=statHandler.sloppyList[2],handler=self)
				index+=2
			else:
				self.eleATK[key].addWidgets(parent=self.eleFrame,offsetRow=index,offsetColumn=0)
				self.eleATK[key].addStats(holder=self.eleFrame,offsetRow=index,offsetColumn=0,pixel=pixel,name=key,stat=statHandler.sloppyList[index],handler=self)
				index+=1
		Label(self.eleFrame, text="",image=pixel,height=26).grid(row=11,column=0,sticky=W)

	def generateEleDefs(self,pixel):
		index=0
		for key, value  in self.eleRES.items():
			if index==1:
				blank = Label(self.eleFrame, text=" ")
				blank.grid(row=index, column=3,sticky=W)
				self.eleRES[key].addRes(holder=self.eleFrame,offsetRow=index+1,offsetColumn=3,stat = self.eleRES[key])
				self.eleRES[key].addWidgets(parent=self.eleFrame, offsetRow=index+1,offsetColumn=3)
				index+=2

			else:
				self.eleRES[key].name = ""
				self.eleRES[key].addRes(holder=self.eleFrame,offsetRow=index,offsetColumn=3,stat = self.eleRES[key])
				self.eleRES[key].addWidgets(parent=self.eleFrame, offsetRow=index,offsetColumn=3)
				index+=1


class eleStat(stat):
	def __init__(self, base, name):
		super().__init__(base, name)
		self.refStat = 0
		self.handlerRef = NULL
	def updateDisplay(self, eleBonus): # new number is the update display one 
		statAtk = int(getattr(self.handlerRef.thePlayer.statHandler, self.refStat).getScaled())
		willBonus = int(getattr(self.handlerRef.thePlayer.statHandler, "will").getScaled()/4)
		setattr(self,"base",statAtk + willBonus + self.baseMod)
		self.display.config(text=f"{self.base+self.customMod}")
	def update_modifiers(self):
		value = int(self.customModValue.get())
		setattr(self, "customMod", value)
		self.updateDisplay()
	def addStats(self, offsetRow, offsetColumn, pixel, name, stat, holder,handler):
		imagePath = f"Images\\{name}.png"
		imagePath = fileName(imagePath)
		self.theIcon = ImageTk.PhotoImage(Image.open(imagePath))
		self.Icon = Label(holder, image=self.theIcon,height=26)
		self.Icon.grid(row=offsetRow, column=offsetColumn,sticky=W)
		self.display = Label(holder, text="0",width=4)
		self.display.grid(row=offsetRow,column=offsetColumn+1,sticky=W)
		self.refStat = stat

	def addWidgets(self, parent, offsetRow, offsetColumn):
		self.customModValue = StringVar(value=0)
		self.customMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f',width=6,wrap=True,justify=LEFT,
                            command=self.update_modifiers,textvariable=self.customModValue)
		self.customMods.grid(row=offsetRow,column=offsetColumn+2,sticky=W)
		self.customMods.configure(justify=LEFT)
		self.customMods.xview_moveto(1)