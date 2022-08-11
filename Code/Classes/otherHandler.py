from tkinter import *
from Classes.tkentrycomplete import *
from Classes.classesClass import *
from Classes.atkHandler import trackerStat
from databaseInfo import *
from Classes.statClasses import *

class OtherHandler:
    def __init__(self, parent,pixel,person,root):
        self.youkaiCap = trackerStat(0, "Youkai Cap ")
        self.skillPool = trackerStat(0, "Skill Pool")
        self.initative = trackerStat(0, "Initative")
        self.bodyWeight = trackerStat(0, "BW")
        self.encumbrance = trackerStat(0, "Encumbrance")
        statList = ["youkaiCap", "skillPool","initative","bodyWeight","encumbrance"]
        placeholder = Label(parent, text=" ")
        placeholder.grid(row=10,column=0,columnspan=3)
        for x in range(len(statList)):
            getattr(self, statList[x]).addStats(offsetRow=x+11,offsetColumn=0,holder=parent, name = statList[x],handler=NULL,pixel=NULL)
            getattr(self, statList[x]).addWidgets(offsetRow=x+11,offsetColumn=0,parent=parent)
            getattr(self, statList[x]).handlerRef = self
        self.stats = person.statHandler
        self.updateAll()
    def calcBW(self):
        return int(5 + self.stats.strength.getScaled()+ self.bodyWeight.customMod)
    def calcSP(self):
        return int(5 + int(self.stats.will.getScaled()/10) + int(self.stats.skill.getScaled()/5) + int(self.stats.guile.getScaled()/5) + self.skillPool.customMod)
    def calcYoukaiCap(self):
        return int(5 + (self.stats.faith.getScaled()/5) + self.youkaiCap.customMod)
    def calcEnc(self):
        return int(5 + self.stats.strength.getScaled() + self.stats.vitality.getScaled() + self.encumbrance.customMod)
    def calcInit(self):
        return int(self.stats.celerity.getTotalNoMods() + self.initative.customMod)
    def updateAll(self):
        self.skillPool.display.config(text=self.calcSP())
        self.youkaiCap.display.config(text=self.calcYoukaiCap())
        self.bodyWeight.display.config(text=self.calcBW())
        self.encumbrance.display.config(text=self.calcEnc())
        self.initative.display.config(text=self.calcInit())