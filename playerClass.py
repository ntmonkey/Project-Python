"""
Our Player class that tracks the information of our player
"""
import json

class Player:
	"""
	Player class that tracks agility, personality, sanity, strenght, and progress.
	"""

	def __init__(self, name):
		"""The constructor"""
		self.name = name	
		self.agility = 0
		self.personality = 0
		self.sanity = 0
		self.strength = 0
		self.progress = 0

		
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
		function to add personality
		"""
		self.personality += 1
		if self.personality > 10:
			self.personality = 10

	def subPersonality(self):
		"""
		function to subtract personality
		"""
		self.personality -= 1
		if self.personality < -10:
			self.personality = -10 


	def addSanity(self):
		"""
		function to add sanity
		"""
		self.sanity += 1
		if self.sanity > 10:
			self.sanity = 10

	def subSanity(self):
		"""
		function to subtract sanity
		"""
		self.sanity -= 1
		if self.sanity < -10:
			self.sanity = -10
			
			
	def addStrength(self):
		"""
		function to add strength
		"""
		self.strength += 1
		if self.strength > 10:
			self.strength = 10

	def subStrength(self):
		"""
		function to subtract strength
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
		playerStats = [self.name, 
					   self.agility, 
					   self.personality, 
					   self.sanity, 
					   self.strength, 
					   self.progress]
		return playerStats		
	
	
	def printPlayerStats(self):
		"""
		return current player stats in a list
		"""
		playerStats = ['Name = ' + self.name, 
					   'Agility = ' + str(self.agility), 
					   'Personality = ' + str(self.personality), 
					   'Sanity = ' + str(self.sanity), 
					   'Strength = ' + str(self.strength), 
					   'Progress = ' + str(self.progress)]
		print playerStats
		
		
	def savePlayerStats(self):
		file = open(self.name + 'SaveGame', 'w')
		x = self.returnPlayerStats()
		json.dump(x, file)
		file.close()
		

		



