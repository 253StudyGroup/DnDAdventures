########################
#File Name:character-stats.py
#Date Started: 4/19/2020
#Date Finished: 
#Author: Mark Bell
#***********************
#General Purpose: To define the library for characters stats, how they're 
#generated, assigned, and edited.
#Imported to:character-creation.py
#Misc. Notes
######################## 

from random import randint

def stat_gen_method():
	print("Welcome to the DnD Stats Generator!")
	print("Here are the methods of generating stats in DnD.")
	print("1. Manual Dice Roll")
	print("2. Point Buy")
	print("3. Standard Template")
	method_choice = input("Please select the number to generate Stats.\n")
	return method_choice
	
def dm_comment(choice):

	if choice == "evil":
		print("Ok, we'll have some tough rolls up ahead. Hold on!")
	elif choice == "fair":
		print("Remember that whatever happens...fair is fair.")
	elif choice == "lenient": 
		print("Ok, we'll have some forgiveness baked in.")
		
def stat_roll(type):

	score_results = []
	
	for j in range(0,6):
			
		four_dice = []
		
		for i in range (1,5):
			if type == "evil":
				dice_num = randint(1, 6)
			elif type == "fair":
				dice_num = randint(2, 6)
			elif type == "lenient":
				dice_num = randint(3, 6)
			
			four_dice.append(dice_num)
					
		four_dice.sort()
		four_dice.pop(0)
		value = sum(four_dice)
		score_results.append(value)
		
	return score_results
	
def method_output(choice):

	if choice == '1':

		char_stats = ''
		print("You've selected the Manual method for stats.")
		dm_style = input("Is the DM evil, fair, or lenient? Please describe.")
		dm_comment(dm_style)
		char_stats = stat_roll(dm_style)	
		return char_stats
	
	elif choice == '2':
		print("You've selected the Point Buy method for stats.")
		print("You have 27 points to spend on abilities. See chart below.")
		print("Ability Score Point Cost")
		print("Score			Cost")
		print("  8			  0 ")
		print("  9			  1 ")
		print("  10			  2 ")
		print("  11			  3 ")
		print("  12			  4 ")
		print("  13			  5 ")
		print("  14			  7 ")
		print("  15			  9 ")
		print("\n\nWe hope you choose wisely!")
		
	elif choice == '3':
		print("You've selected the Standard Template method for stats.")
		print("Use the numbers 8, 10, 12, 13, 14,15 how you see fit.")
		char_stats = [8, 10, 12, 13, 14,15]
		return char_stats

	else:
		print("Oops! You entered an incorrect choice.")
		stat_choice = input("Please select the number to generate Stats.")
	

stat_results = ''

stat_results = stat_gen_method()
attribute_scores = method_output(stat_results)
print(attribute_scores)
print("Well...I hope you liked your results. Those are yours for keeps!")

#TODO Decide how the attribute scores are assigned. 

#DONE Apply Racial bonuses to attribute scores. To be tested

print("Welcome to the stat-generation Test Machine!")
print("Today, we are testing the racial modification of our classes.")
race_input = input("What is the race for your character?")

char_stats = [8, 10, 12, 13, 14,15]


	def racial_add(stat_list, race_input):
		if race_input = 'hill dwarf':
			stat_list['CON'] += 2
			stat_list['WIS'] += 1
			dwarfTough = TRUE
		elif race_input = 'mountain dwarf'"
			stat_list['CON'] += 2
			stat_list['STR'] += 2
		elif race_input = 'human':
			for j in range(1, len(stat_list):
				stat_list[j] += 1
		elif race_input = 'high elf':
			stat_list['DEX'] += 2
			stat_list['INT'] += 1
		elif race_input = 'wood elf':
			stat_list['DEX'] += 2
			stat_list['WIS'] += 1
		elif race_input = 'dark elf':
			stat_list['DEX'] += 2
			stat_list['CHA'] += 1
		
#TODO Convert the attribute scores into bonuses



#DONE Generate Hit Points based off the designation of attribute scores. To be tested

def start_hp(class_input, dwarfTough, CONBonus):
	HitPoints = 0
	if class_input = 'Fighter':
		HitPoints = sum(10, CONBonus)
	elif class_input = 'Rogue':
		HitPoints = sum(8, CONBonus)
	elif class_input = 'Wizard':
		HitPoints = sum(6, CONBonus)
		
	if dwarfTough == TRUE:
		HitPoints += 1
		
	return HitPoints
	
#def variable_level_hp(class_input, dwarfTough, CONBonus, StartLevel):

def start_hp(class_input, dwarfTough, CONBonus):
	
	HitPoints = 0
	Health_Rolls = []
	if class_input = 'Fighter':
		for i in range(1, StartLevel)
			HitRoll = randint(1,10) + CONBonus
			Health_Rolls.append(HitRoll)
			
	elif class_input = 'Rogue':
		for i in range(1, StartLevel)
			HitRoll = randint(1,8) + CONBonus
			Health_Rolls.append(HitRoll)
			
	elif class_input = 'Wizard':
		for i in range(1, StartLevel)
			HitRoll = randint(1,6) + CONBonus
			Health_Rolls.append(HitRoll)
		
	if dwarfTough == TRUE:
		ExtraHealth += (1 * StartLevel)
		Health_Rolls.append(ExtraHealth)
		
	HitPoints = sum(Health_Rolls)	
	return HitPoints
	
