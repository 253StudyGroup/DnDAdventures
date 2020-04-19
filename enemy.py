#This is the start of the enemies Class library. The idea is to have each enemy be an
#instance of the Enemy Class, and all the behavior/attributes to be handled by the Class. 

from random import randint

class Enemy():
	
	def __init__(self, ArmorClass, Speed, ChallengeRating):
		self.ArmorClass = ArmorClass
		self.Speed = Speed
		self.ChallengeRating = ChallengeRating
		
		
		
class Goblin(Enemy):

	def __init__(self, ArmorClass, Speed, ChallengeRating):
		super().__init__(ArmorClass, Speed, ChallengeRating)
		self.HitPoints = 0 
		self.StatList = []
		self.EnemySkills = {}
		self.EnemyAbilities = []
		self.Equipment = {}
		
	def set_hp(self):
			
		two_dice = []
		
		for i in range (1,3):
			dice_num = randint(1, 6)
			two_dice.append(dice_num)
			
		self.HitPoints = sum(two_dice)
		
	def set_stats(self):
		stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
		values = [8, 14, 10, 10, 8, 8]
		self.StatList = dict(zip(stats, values))
	
	