class Player:

	agility = 0
	personality = 0
	sanity = 0
	strenght = 0
	progress = 0


	def __init__(self, name):
		self.name = name

	#functions to add and substract agility		
	def addAgility(self):
		self.agility += 1
		if self.agility > 10:
			self.agility = 10

	def subAgility(self):
		self.agility -= 1
		if self.agility < -10:
			self.agility = -10
			

	#functions to add and subtract personality
	def addPersonality(self):
		self.personality += 1
		if self.personality > 10:
			self.personality = 10

	def subPersonality(self):
		self.personality -= 1
		if self.personality < -10:
			self.personality = -10


	#functions to add and subtract sanity
	def addSanity(self):
		self.sanity += 1
		if self.sanity > 10:
			self.sanity = 10

	def subSanity(self):
		self.sanity -= 1
		if self.sanity < -10:
			self.sanity = -10
			
			
	#functions to add and subtract strength
	def addStrength(self):
		self.strength += 1
		if self.strength > 10:
			self.strength = 10

	def subStrength(self):
		self.strength -= 1
		if self.strength < -10:
			self.strength = -10
	
	
	#Set story progress 
	def setProgress(self, prog):
		self.progress = prog
		
	
	#return current player stats
	def returnPlayerStats(self):
		playerStats = ['Agility = ' + str(self.agility), 
					   'Personality = ' + str(self.personality), 
					   'Sanity = ' + str(self.sanity), 
					   'Strenght = ' + str(self.strenght), 
					   'Progress = ' + str(self.progress)]
		return playerStats
		

		
		
		
		

			


