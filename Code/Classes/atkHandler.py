from tkinter import *
from tkinter import ttk
from Classes.tkentrycomplete import *
from Classes.classesClass import *
from Classes.vitals import *
from Classes.eleHandler import *
from databaseInfo import *
from Classes.statClasses import *

class AtkHandler:
    def __init__(self, parent,pixel,person,root):
        self.hit = trackerStat(0, "Hit")
        self.flanking = trackerStat(0, "Flanking")
        self.crit = trackerStat(0, "Crit")
        self.statusInflict = trackerStat(0, "Status Inflict")
        statList = ["hit","crit","flanking","statusInflict"]
        self.personRef = person
        for x in range(len(statList)):
            getattr(self, statList[x]).addStats(offsetRow=x,offsetColumn=0,holder=parent, name = statList[x],handler=NULL,pixel=NULL)
            getattr(self, statList[x]).addWidgets(offsetRow=x,offsetColumn=0,parent=parent)
            getattr(self, statList[x]).handlerRef = self
        self.stats = person.statHandler
    def critCalc(self):
        return f"{int((self.stats.skill.getScaled()/2) + self.stats.luck.getScaled() + self.crit.customMod)}%"
    def hitCalc(self):
        return (self.stats.skill.getScaled()*2) + self.hit.customMod
    def flankCalc(self):
        return int(10 + self.stats.guile.getScaled())
    def statusInf(self):
        return f"{int(self.stats.skill.getScaled()*2 + self.stats.will.getScaled())}%"
    def updateAll(self):
        self.crit.display.config(text=self.critCalc())
        self.hit.display.config(text=self.hitCalc())
        self.flanking.display.config(text=self.flankCalc())
        self.statusInflict.display.config(text=self.statusInf())
class trackerStat(stat):
    def __init__(self, base, name):
        super().__init__(base, name)
    def update_modifiers(self):
        value = int(self.customModValue.get())
        setattr(self, "customMod", value)
        self.handlerRef.updateAll() 
    def updateDisplay(self):
        self.handlerRef.updateAll()
    def addRes(self, offsetRow, offsetColumn, holder, stat):
        self.display = Label(holder, text="0%", width=4,anchor=W)
        self.refStat = stat
        self.display.grid(row=offsetRow,column=offsetColumn,sticky=E)
    def addStats(self, offsetRow, offsetColumn, pixel, name, handler, holder):
        self.nameLabel = Label(holder, text=self.name,width=10,anchor=W)
        self.nameLabel.grid(row=offsetRow,column=offsetColumn,sticky=W)
        textToUse = "0"
        if name in ["hit","crit","statusInflict","statusResist","phyRes","magRes"]: textToUse = "0%"
        self.display = Label(holder, text=textToUse, width=4)
        self.refStat = stat
        self.display.grid(row=offsetRow,column=offsetColumn+1,sticky=E)
    def addWidgets(self, parent, offsetRow, offsetColumn):
        self.customModValue = StringVar(value=0)
        if self.name == "Evade":
            self.armorModValue = StringVar(value=0)
            self.armorMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f', width=6, wrap=True
                                     , justify=LEFT,command=self.update_modifiers,textvariable=self.armorModValue)
            self.customMods = Spinbox(parent, from_=-100,to=50,increment=1,format='%10.0f', width=6, wrap=True
                                     , justify=LEFT,command=self.update_modifiers,textvariable=self.customModValue)
            self.customMods.grid(row=offsetRow,column=offsetColumn+2,sticky=E)
            self.armorMods.grid(row=offsetRow,column=offsetColumn+3,sticky=E)
        else:
            self.customMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f', width=6, wrap=True
                , justify=LEFT,command=self.update_modifiers,textvariable=self.customModValue)
            self.customMods.grid(row=offsetRow,column=offsetColumn+2,sticky=E)
        
        
# if self.name == "evade":
  #          self.armorModValue = StringVar(value=0)
   #         self.armorMods = Spinbox(parent, from_=-100,to=100,increment=1,format='%10.0f', width=6, wrap=True
    #                                 , justify=LEFT,command=self.update_modifiers,textvariable=self.armorModValue,stat="readonly")
     #       self.customMods = Spinbox(parent, from_=-100,to=50,increment=1,format='%10.0f', width=6, wrap=True
      #                               , justify=LEFT,command=self.update_modifiers,textvariable=self.customModValue,stat="readonly")
       #     self.customMods.grid(row=offsetRow,column=offsetColumn+3)
        #    self.armorMods.grid(row=offsetRow,column=offsetColumn+2)