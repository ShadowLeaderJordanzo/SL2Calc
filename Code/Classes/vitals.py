from tkinter import NSEW, NW, Label

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
        return round(self.health+self.customHealth,1)
    def getCurrentHealth(self):
        return int(round(self.health+self.customHealth * ( self.percentHealth / 100 ),1))
    def getMaxFocus(self):
        return self.focus+self.customFocus
    def getCurrentFocus(self):
        return int(round(self.focus+self.customFocus * ( self.percentFocus / 100 ),1))
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
    def makeDisplay(self, handler):
        self.healthDisplay = Label(handler, text=f"HP: {self.getCurrentHealth()}/{self.getMaxHealth()}", fg='#FF0000',padx=61,pady=-10) 
        self.focusDisplay = Label(handler, text=f"FP: {self.getCurrentFocus()}/{self.getMaxFocus()}", fg='#0000FF',padx=61,pady=-15) 
        self.healthDisplay.grid(row=0,column=0,sticky=NW)
        self.focusDisplay.grid(row=1,column=0,sticky=NW)