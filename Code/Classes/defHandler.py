from tkinter import *
from tkinter import ttk
from Classes.tkentrycomplete import *
from Classes.classesClass import *
from Classes.vitals import Vital
from Classes.eleHandler import EleHandler
from Classes.atkHandler import trackerStat
from databaseInfo import *
from Classes.statClasses import *

class DefHandler:
    def __init__(self, parent,pixel,person,root):
        self.phyRes = trackerStat(0, "Phys. ")
        self.magRes = trackerStat(0, "Mag. Def")
        self.evade = trackerStat(0, "Evade")
        self.critEvade = trackerStat(0, "Crit Evade")
        self.statusResist = trackerStat(0, "Status Resist")
        statList = ["statusResist", "phyRes","magRes","evade","critEvade"]
        self.personRef = person
        for x in range(len(statList)):
            getattr(self, statList[x]).addStats(offsetRow=x+4,offsetColumn=0,holder=parent, name = statList[x],handler=NULL,pixel=NULL)
            getattr(self, statList[x]).addWidgets(offsetRow=x+4,offsetColumn=0,parent=parent)
            getattr(self, statList[x]).handlerRef = self
        self.stats = person.statHandler
    def physCalc(self):
        return f"{int((self.stats.defense.getScaled() * 0.9)  + self.phyRes.customMod)}%"
    def resCalc(self):
        return f"{int((self.stats.resistance.getScaled() * 0.9) + self.magRes.customMod)}%"
    def evadeCalc(self):
        return int(self.stats.celerity.getScaled()*2 + int(self.evade.armorModValue.get()) + self.evade.customMod)
    def critEvadeCalc(self):
        return int(self.stats.luck.getScaled() + self.stats.faith.getScaled() + self.critEvade.customMod)
    def statusResistCalc(self):
        return f"{int(self.stats.faith.getScaled())}%"
    def updateAll(self):
        self.phyRes.display.config(text=self.physCalc())
        self.magRes.display.config(text=self.resCalc())
        self.evade.display.config(text=self.evadeCalc())
        self.critEvade.display.config(text=self.critEvadeCalc())
        self.statusResist.display.config(text=self.statusResistCalc())