
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