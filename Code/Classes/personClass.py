from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk

from Classes.classesClass import *
from Classes.vitals import Vital
from Classes.eleHandler import EleHandler
from databaseInfo import *
from Classes.statClasses import *


def astroPopUp():
	astro = Toplevel()
	astro.configure(bg='black')
	astro.resizable=(0,0)
	astro.wm_maxsize(width=307,height=313)
	astro.wm_minsize(width=307,height=313)
	starSign = PhotoImage(file = "Images/Starsign.png")
	astroCanvas = Canvas(astro, width=307,height=313)
	astroCanvas.pack(fill="both",expand= TRUE)
	astroCanvas.create_image(0,0,image=starSign, anchor="nw")
	astro.mainloop()
class ClassBonuses:
	def __init__(self, name, dataBase): # probably sql to handle database of info 
		dataBase.cur.execute('SELECT * FROM classes WHERE name=?', (name,))
		data = dataBase.cur.fetchone()
		self.strength = data[1]
		self.will = data[2]
		self.skill = data[3]
		self.celerity = data[4]
		self.defense = data[5]
		self.resistance = data[6]
		self.vitality = data[7]
		self.faith = data[8]
		self.luck = data[9]
		self.guile = data[10]
		self.sanctity = data[11]

class Person:
	# so if its class variable its essentially shared across all classes, but more like it exists as its own instance shared?? 
	def __init__(self, root, pixel,dataBase):
		self.vitals = Vital(parent=root)
		self.eleHandler = EleHandler(parent=root,pixel=pixel,person=self) # ELE ATKS / ELE DEF
		self.atkHandler = NULL # hit/crit/status infliction/flanking 
		self.defHandler = NULL # Phys% Mag Def % Evade crit evade Status Resist
		self.othersHandler = NULL # youkai cap, skill pool, init, bw / encumbrance
		self.statHandler = statHandler( stats = [stat(base=0,name="strength"),stat(base=0,name="will"),stat(base=0,name="skill"),
			stat(base=0,name="celerity"),stat(base=0,name="defense"),stat(base=0,name="resistance"),stat(base=0,name="vitality"),
			stat(base=0,name="faith"),stat(base=0,name="luck"),stat(base=0,name="guile"),stat(base=0,name="sanctity"),stat(base=0,name="aptitude")],
			parent=root, pixel=pixel, person=self) # stats
		self.modHandler = NULL # stamps/LE, additonal things like check boxes etc
		self.trait = "None"
		self.race = "None"
		self.mainClass = "None"
		self.subClass = "None"
		self.statHandler.setParents()
		self.makeDisplay(root=root,dataBase=dataBase)
	def getClassNames(self, Data):
		Data.cur.execute('SELECT * FROM classes')
		result = []
		records = Data.cur.fetchall()
		for row in records:
			result.append(row[0])
		return result
	def makeDisplay(self,root,dataBase):
		infoFrame = Frame(root)
		infoFrame.grid(row=3,column=0,sticky=W,columnspan=4)
		infoFrame.columnconfigure(0,weight=1)
		infoFrame.columnconfigure(1,weight=1)
		infoFrame.columnconfigure(2,weight=1)
		infoFrame.columnconfigure(3,weight=1)
		raceLabel = Label(infoFrame, text="Race:")
		raceLabel.grid(row=0,column=0,sticky=W)
		self.currentRace = StringVar(value='_HUMANS_')
		self.raceComboBox = ttk.Combobox(infoFrame, textvariable=self.currentRace,values=['Onigan','Glykin'],width=12)
		self.raceComboBox.grid(row=0,column=1,sticky=W)
		self.raceComboBox['state'] = 'readonly'
  
		foodLabel = Label(infoFrame, text="Food:")
		foodLabel.grid(row=1,column=0,sticky=W)
		self.currentFood = StringVar(value='_STR_')
		self.foodComboBox = ttk.Combobox(infoFrame, textvariable=self.currentFood,values=['Salad','Fugu'],width=12)
		self.foodComboBox.grid(row=1,column=1,sticky=W)
		self.foodComboBox['state'] = 'readonly'
  
		mClassLabel = Label(infoFrame, text="Main Class:")
		mClassLabel.grid(row=0,column=2,sticky=W)
		self.mainClass = StringVar(value=' ')
		records = self.getClassNames(Data=dataBase)
		self.mainClassComboBox = ttk.Combobox(infoFrame, textvariable=self.mainClass,values=records,width=18)
		self.mainClassComboBox.grid(row=0,column=3,sticky=W)
		self.mainClassComboBox['state'] = 'readonly'
  
		sClassLabel = Label(infoFrame, text="Sub Class:")
		sClassLabel.grid(row=1,column=2,sticky=W)
		self.subClass = StringVar(value=' ')
		self.subClassComboBox = ttk.Combobox(infoFrame, textvariable=self.subClass,values=records,width=18)
		self.subClassComboBox.grid(row=1,column=3,sticky=W)
		self.subClassComboBox['state'] = 'readonly'
