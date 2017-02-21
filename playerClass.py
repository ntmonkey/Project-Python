"""
Our Player class that tracks the information of our player
"""

class Player:
	"""Player class that tracks agility, personality, sanity, strenght, and progress"""

	agility = 0
	personality = 0
	sanity = 0
	strenght = 0
	progress = 0


	def __init__(self, name):
		"""The constructor"""
		self.name = name

		
	def addAgility(self):
		"""
		function to add agility
		"""	
		self.agility += 1
		if self.agility > 10:
			self.agility = 10

	def subAgility(self):
		"""
		function to subtract agility
		"""
		self.agility -= 1
		if self.agility < -10:
			self.agility = -10
			

	def addPersonality(self):
		"""
		functions to add personality
		"""
		self.personality += 1
		if self.personality > 10:
			self.personality = 10

	def subPersonality(self):
		"""
		functions to subtract personality
		"""
		self.personality -= 1
		if self.personality < -10:
			self.personality = -10 


	def addSanity(self):
		"""
		functions to add sanity
		"""
		self.sanity += 1
		if self.sanity > 10:
			self.sanity = 10

	def subSanity(self):
		"""
		functions to subtract sanity
		"""
		self.sanity -= 1
		if self.sanity < -10:
			self.sanity = -10
			
			
	def addStrength(self):
		"""
		functions to add strength
		"""
		self.strength += 1
		if self.strength > 10:
			self.strength = 10

	def subStrength(self):
		"""
		functions to subtract strength
		"""
		self.strength -= 1
		if self.strength < -10:
			self.strength = -10
	
	
	def setProgress(self, prog):
		"""
		set story progress as an integer
		"""
		self.progress = prog
		
	
	def returnPlayerStats(self):
		"""
		return current player stats in a list
		"""
		playerStats = ['Agility = ' + str(self.agility), 
					   'Personality = ' + str(self.personality), 
					   'Sanity = ' + str(self.sanity), 
					   'Strenght = ' + str(self.strenght), 
					   'Progress = ' + str(self.progress)]
		return playerStats
		



