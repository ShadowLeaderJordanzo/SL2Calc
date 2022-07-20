from tkinter import *
def astroPopUp():
	astro = Tk()
	astro.configure(bg='black')
	astroLabel = Label(astro, text = "Not implemented")
	astroLabel.pack()
	astro.mainloop()
class ClassBonuses:
	def __init__(self, name, dataBase): # probably sql to handle database of info 
		dataBase.cur.execute('SELECT * FROM classes WHERE name=?', (name,))
		data = dataBase.cur.fetchone()
		print(data)
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
	def __init__(self):
		self.race = "None"
		self.mainClass = "None"
		self.subClass = "None"