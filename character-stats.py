#TODO Import the stats generation script. 

#TODO Decide how the stats are slotted into attribute scores. 

#TODO Apply Racial bonuses to attribute scores. 

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


#Input Variables


Stats Values from generator script

#TODO Generate Hit Points based off the designation of attribute scores 

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
	
def variable_level_hp(class_input, dwarfTough, CONBonus, StartLevel):

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
