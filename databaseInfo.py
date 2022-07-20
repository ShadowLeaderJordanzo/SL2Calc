from asyncio.windows_events import NULL
import sqlite3

class Database:

	def __init__(self):
		self.con = sqlite3.connect('database.db')
		self.cur = self.con.cursor()


		# con.commit()
		# con.close()



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