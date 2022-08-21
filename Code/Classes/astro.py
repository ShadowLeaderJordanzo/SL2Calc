from tkinter import *
from tkinter import ttk
from databaseInfo import *

class AstroHandler:
	def __init__(self,root):
		self.previousChoice = "None"
		self.currentChoice = "None"
	def astroPopUp(self):
		self.astro = Toplevel()
		self.astro.configure(bg='black')
		self.astro.resizable=(0,0)
		self.astro.wm_maxsize(width=307,height=313)
		self.astro.wm_minsize(width=307,height=313)
		self.starSign = PhotoImage(file = fileName('Images\\Starsign.png'))
		self.astroCanvas = Canvas(self.astro, width=307,height=313)
		self.astroCanvas.pack(fill="both",expand= TRUE)
		self.astroCanvas.create_text(100,100, text="hm")
		self.astroCanvas.create_image(0,0,image=self.starSign, anchor="nw")
		self.makeLabels()
		self.astro.mainloop()
	def makeLabels(self):
		self.neptuneImage = PhotoImage(file=fileName(f"Images\\Neptune.png"))
		self.neptune = AstroButtons(root=self.astro, name="Neptune",function="+1 VIT +2 Water ATK",imageneeded=self.neptuneImage)
		self.astroCanvas.create_window(4,130, anchor="nw", window = self.neptune)
  
		self.jupiterImage = PhotoImage(file=fileName(f"Images\\Jupiter.png"))
		self.jupiter = AstroButtons(root=self.astro, name="Jupiter",function="+1 VIT +2 Water ATK",imageneeded=self.jupiterImage)
		self.astroCanvas.create_window(252,130, anchor="nw", window = self.jupiter)
  
		self.mercuryImage = PhotoImage(file=fileName(f"Images\\Mercury.png"))
		self.mercury = AstroButtons(root=self.astro, name="Mercury",function="+1 VIT +2 Water ATK",imageneeded=self.mercuryImage)
		self.astroCanvas.create_window(66,196, anchor="nw", window = self.mercury)
class AstroButtons(Button):
	def __new__(cls,root,name,function,imageneeded):
		return Button(root,text=f"{name} {function}",image=imageneeded,borderwidth=0)