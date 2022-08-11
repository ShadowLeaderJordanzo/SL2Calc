from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from Classes.tkentrycomplete import *
from Classes.classesClass import *
from Classes.vitals import Vital
from Classes.eleHandler import EleHandler
from Classes.atkHandler import AtkHandler
from Classes.defHandler import DefHandler
from Classes.otherHandler import OtherHandler
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
		dataBase.cur.execute('SELECT * FROM classbonus WHERE name=?', (name,))
		data = dataBase.cur.fetchall()
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
		self.superFrame = ttk.Frame(root)
		self.superFrame.grid(row=6,column=0,sticky=W,columnspan=12)
		self.superFrame.columnconfigure(0,weight=1)
		self.superFrame.columnconfigure(1,weight=1)
		self.infoFrame = ttk.Frame(root)
		self.infoFrame.grid(row=6,column=14,sticky=W)
		self.Data = dataBase
		self.statHandler = statHandler( stats = [stat(base=0,name="strength"),stat(base=0,name="will"),stat(base=0,name="skill"),
			stat(base=0,name="celerity"),stat(base=0,name="defense"),stat(base=0,name="resistance"),stat(base=0,name="vitality"),
			stat(base=0,name="faith"),stat(base=0,name="luck"),stat(base=0,name="guile"),stat(base=0,name="sanctity"),stat(base=0,name="aptitude")],
			parent=self.superFrame, pixel=pixel, person=self,root=root) # stats
		self.vitals = Vital(parent=root,person=self)
		self.eleHandler = EleHandler(parent=self.superFrame,pixel=pixel,person=self,root=root) # ELE ATKS / ELE DEF
		self.atkHandler = AtkHandler(parent=self.infoFrame,pixel=pixel,person=self,root=root) # hit/crit/status infliction/flanking 
		self.defHandler = DefHandler(parent=self.infoFrame,pixel=pixel,person=self,root=root) # Phys% Mag Def % Evade crit evade Status Resist
		self.othersHandler = OtherHandler(parent=self.infoFrame,pixel=pixel,person=self,root=root) # youkai cap, skill pool, init, bw / encumbrance
		self.modHandler = NULL # stamps/LE, additonal things like check boxes etc
		textFrame = ttk.Frame(root)
		textFrame.grid(row=5,column=14,sticky=W)
		Label(textFrame, text=" ",width=8).grid(row=0,column=0)
		Label(textFrame, text=" ",width=4).grid(row=0,column=1)
		Label(textFrame, text="Mods",width=8).grid(row=0,column=2)
		Label(textFrame, text="Torso").grid(row=0,column=3)
		self.trait = "None"
		self.race = "None"
		self.mainClass = "None"
		self.subClass = "None"
		self.statHandler.setParents()
		self.makeDisplay(root=root,dataBase=dataBase)
	def updateAll(self):
		self.eleHandler.updateAll()
		self.atkHandler.updateAll()
		self.othersHandler.updateAll()
		self.defHandler.updateAll()
	def getFoodNames(self):
		with sqlite3.connect(fileName("Code\\database.db")) as db:
			cur = db.cursor()
			cur.execute('SELECT * FROM food')
			result = []
			records = cur.fetchall()
			for row in records:
				result.append(row[0])
			return result
	def foodTest(self, event):
		print("Do we get here?")
		with sqlite3.connect(fileName("Code\\database.db")) as db:
			cur = db.cursor()
			hm = cur.execute('SELECT * FROM food WHERE name=?', (self.currentFood.get(),))
			records = cur.fetchall()
			colName = [tuple[0] for tuple in hm.description]
			self.statHandler.assignFoodBonus(results=records,columns=colName)
	def getClassNames(self, Data):
		Data.cur.execute('SELECT * FROM classes')
		result = []
		records = Data.cur.fetchall()
		for row in records:
			result.append(row[0])
		return result
	def getClassBonusList(self,main):
		if main: varName = self.mainClass.get()
		else: varName = self.subClass.get()
		hm1 = self.Data.cur.execute('SELECT * FROM classbonus WHERE name=?', (varName,))
		records1 = self.Data.cur.fetchall()
		if len(records1)==0:
			return []
		else:
			colName1 = [tuple[0] for tuple in hm1.description]
		# records = values, colname = cols
		results = [records1[0][1]]
		index=2
		for name in colName1:
			if name == "name" or name == "max":
				continue
			if records1[0][index] == None:
				index+=1
				continue
			results.append(name)
			index+=1
		return results
	def getRaceNames(self, Data):
		result =[]		
		with sqlite3.connect(fileName("Code\\database.db")) as db:
			cur = db.cursor()
			cur.execute('SELECT * FROM races')
			records = cur.fetchall()
			for row in records:
				result.append(row[0])
		return result
	def changeRace(self,event):
		hm = self.Data.cur.execute('SELECT * FROM races WHERE names=?', (self.currentRace.get(),))
		records = self.Data.cur.fetchall()
		colName = [tuple[0] for tuple in hm.description]
		self.statHandler.assignRaceStats(results=records, columns=colName)
	def changeClass(self,event, main):
		if main==1: varName = "mainClass"
		else: varName = "subClass"
		with sqlite3.connect(fileName("Code\\database.db")) as db:
			if main == 1:
				hm = db.cur.execute('SELECT * FROM classes WHERE name=?', (self.mainClass.get(),))
				records = self.Data.cur.fetchall()
				colName = [tuple[0] for tuple in hm.description]
				self.statHandler.assignClassStats(results=records,columns=colName,main=varName)
				hm1 = db.cur.execute('SELECT * FROM classbonus WHERE name=?', (self.mainClass.get(),))
				records1 = db.cur.fetchall()
				if len(records1)==0:
					self.mClassBonusValue = StringVar(value=0)
					self.mainClassBonus.configure(to=0,from_=0,textvariable=self.mClassBonusValue)
					return
				else:
					colName1 = [tuple[0] for tuple in hm1.description]
					self.statHandler.assignClassBonus(results=records1, columns=colName1,main=main)
					self.updateClassBonuses()
			else:
				hm1 = db.cur.execute('SELECT * FROM classbonus WHERE name=?', (self.subClass.get(),))
				records1 = db.cur.fetchall()
				if len(records1)==0:
					self.sClassBonusValue = StringVar(value=0)
					self.subClassBonus.configure(to=0,from_=0,textvariable=self.sClassBonusValue)
					return
				else:
					colName1 = [tuple[0] for tuple in hm1.description]
					self.statHandler.assignClassBonus(results=records1, columns=colName1,main=main)
					self.updateClassBonuses()
	def updateClassBonuses(self):
		value = int(self.mClassBonusValue.get())
		classBonuses = self.getClassBonusList(main=1)
		if len(classBonuses) > 0:
			self.mainClassBonus.configure(to=classBonuses[0])
			for name in classBonuses[1:]:
				setattr(getattr(self.statHandler, name), "mClassBonus", value)
		if self.subClass.get() == self.mainClass.get():
			self.subClassBonus.configure(to=0,from_=0)
		else:
			value = int(self.sClassBonusValue.get())
			classBonuses = self.getClassBonusList(main=0)
			if len(classBonuses) > 0:
				self.subClassBonus.configure(to=classBonuses[0])
				for name in classBonuses[1:]:
					setattr(getattr(self.statHandler, name), "sClassBonus", value)
		self.statHandler.updateAll()
	def makeDisplay(self,root,dataBase):
		infoFrame = Frame(root)
		infoFrame.grid(row=3,column=0,sticky=W,columnspan=4)
		infoFrame.columnconfigure(0,weight=1)
		infoFrame.columnconfigure(1,weight=1)
		infoFrame.columnconfigure(2,weight=1)
		infoFrame.columnconfigure(3,weight=1)
		raceLabel = Label(infoFrame, text="Race:")
		raceLabel.grid(row=0,column=0,sticky=W)
		records1 = self.getRaceNames(Data=dataBase)
		self.currentRace = StringVar(value='Pick a Race')
		self.raceComboBox = AutocompleteCombobox(infoFrame, textvariable=self.currentRace,values=records1,width=15)
		self.raceComboBox.set_completion_list(records1)
		self.raceComboBox.grid(row=0,column=1,sticky=W)
		self.raceComboBox.bind('<<ComboboxSelected>>', self.changeRace)
		foodLabel = Label(infoFrame, text="Food:")
		foodLabel.grid(row=1,column=0,sticky=W)
		records2 = self.getFoodNames()
		self.currentFood = StringVar(value='Pick a Food')
		self.foodComboBox = AutocompleteCombobox(infoFrame, textvariable=self.currentFood,values=records2,width=15)
		self.foodComboBox.set_completion_list(records2)
		self.foodComboBox.grid(row=1,column=1,sticky=W)
		self.foodComboBox.bind('<<ComboboxSelected>>', self.foodTest)
  
		mClassLabel = Label(infoFrame, text="Main Class:")
		mClassLabel.grid(row=0,column=2,sticky=W)
		self.mainClass = StringVar(value='Pick a Class')
		records = self.getClassNames(Data=dataBase)
  
		self.mainClassComboBox = AutocompleteCombobox(infoFrame, textvariable=self.mainClass,values=records,width=18)
		self.mainClassComboBox.set_completion_list(records)
		self.mainClassComboBox.grid(row=0,column=3,sticky=W)  
		self.mainClassComboBox.bind('<<ComboboxSelected>>', partial(self.changeClass, main=1))
  
		self.mClassBonusValue = StringVar(value=0)
		self.mainClassBonus = Spinbox(infoFrame, from_=0,to=0,increment=1,format='%10.0f',width=6, command=self.updateClassBonuses,textvariable=self.mClassBonusValue)
		Label(infoFrame, text="Passives: ").grid(row=0,column=4,sticky=W)
		self.mainClassBonus.grid(row=0,column=5,sticky=W)
  
		sClassLabel = Label(infoFrame, text="Sub Class:")
		sClassLabel.grid(row=1,column=2,sticky=W)
		self.subClass = StringVar(value='Pick a Sub Class')
  
		self.subClassComboBox = AutocompleteCombobox(infoFrame, textvariable=self.subClass,values=records,width=18)
		self.subClassComboBox.set_completion_list(records)
		self.subClassComboBox.grid(row=1,column=3,sticky=W)
		self.subClassComboBox.bind('<<ComboboxSelected>>', partial(self.changeClass, main=0))
		Label(infoFrame, text="Passives: ").grid(row=1,column=4,sticky=W)
		self.sClassBonusValue = StringVar(value=0)
		self.subClassBonus = Spinbox(infoFrame, from_=0,to=0,increment=1,format='%10.0f',width=6, command=self.updateClassBonuses,textvariable=self.sClassBonusValue)
		self.subClassBonus.grid(row=1,column=5,sticky=W)
