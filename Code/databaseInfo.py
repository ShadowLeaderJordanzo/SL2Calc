from asyncio.windows_events import NULL
import sqlite3
import os
import sys
import os

def fileName(text):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		basePath = sys._MEIPASS
	except Exception:
		basePath = os.path.abspath(".")
	return os.path.join(basePath, text)
class Database:

	def __init__(self):
		print("hm")		
		with sqlite3.connect(fileName("Code\\database.db")) as db:
			self.con = db
			self.cur = db.cursor()
			# self.con.close()

	def parseTxt(self, file):
		with open(file) as file:
			currentString = "INSERT INTO classbonus (name, "
			valueString = "VALUES ('"
			for line in file:
				if line.strip() == "break;":
					valueString = valueString[:-1]
					currentString = currentString[:-1]
					valueString+= ")"
					currentString+= ")"
					print(currentString + " " + valueString)
					self.cur.execute(currentString + " " + valueString)
					self.con.commit()
					currentString = "INSERT INTO classbonus (name, "
					valueString = "VALUES ('"
					continue
				if line.strip()[-1:] == ";":
				# next will be the stats, but how do we get them to be the same on the database as here
					valueString+="'" + line.strip()[-2:-1]+ "'," # the 
					currentString+=line.strip().lower()[0:-5] + ","
				else:
					valueString+=line.strip() + "'," # should be class name


#### Code for parsing classes ####

#    def parseTxt(self, file):
#        with open(file) as file:
#            currentString = "INSERT INTO classes (name, "
#            valueString = "VALUES ('"
#            for line in file:
#                if line.strip() == "break;":
#					valueString = valueString[:-1]
#					currentString = currentString[:-1]
#					valueString+= ")"
#					currentString+= ")"
#					print(currentString + " " + valueString)
#					self.cur.execute(currentString + " " + valueString)
#					self.con.commit()
#					currentString = "INSERT INTO classes (name, "
#					valueString = "VALUES ('"
#					continue
#				if line.strip()[-1:] == ";":
#				# next will be the stats, but how do we get them to be the same on the database as here
#					valueString+="'" + line.strip()[-2:-1]+ "'," # the 
#					currentString+=line.strip().lower()[0:-5] + ","
#				else:
#					valueString+=line.strip() + "'," # should be class name