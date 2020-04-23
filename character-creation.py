########################
#File Name:character-creation.py
#Date Started: 4/11/2020
#Date Finished: 
#Author(s): Mark Bell, Connor Porter
#***********************
#General Purpose:To introduce and create a character according to the rule
#-set of DnD 5th edition. 
#Imported to:None
#Misc. Notes: 
########################





import pygame

###### VARIABLE CREATION CENTER ##### -CP 04/18/2020 @ 4:30pm on a Saturday
HitPoints = 0
InitScore = 0
CharSpeed = 0
RaceOfChar = 'NONE'
ClassOfChar = 'NONE'
StrengthOfChar = 0
CharismaOfChar = 0
WisdomOfChar = 0
IntellectOfChar = 0
DexterityOfChar = 0
ConstitutionOfChar = 0
StatPair = 
CharSkills = {:}
CharSkillsStat = []
SavingThrowCheckArray = []
ProficiencyArray = []
ProficiencyBonus = 0
###########################################################################
	print("Greetings Soul! You've spent a long time in the nether.")
	print("It has become your time to enter a world of mystery and adventure.")

def choose_char_class():
	print("The role that your character will play in the world will be important!")
	print("Will you choose the Figher, Rogue, or Wizard?")
	print(" 1. Fighter (Experienced in Hand to Hand Combat)")
	print(" 2. Rogue (Experienced in Stealth and Subtlety)")
	print(" 3. Wizard (Experienced in Knowledge and Spells)")
	ClassOfChar = input("Create your Class: ")
	while ClassOfChar != "fighter" or "rogue" or "wizzard" or "Fighter" or "Rogue" or "Wizard":
		print("Sorry soul... That class is not available for you at this time.")
		print("Please choose from the following options: Fighter, Rogue, Wizard.")
		ClassOfChar = input("Choose your Class: ")
		
	return ClassOfChar
####END OF choose_char_class METHOD####

def choose_char_race():
	print("What Race would you like to be?")
	print("You could be flexible like a human, agile like an elf, or hearty as a dwarf!")
	print("Pick the race which you would prefer to play in this realm.")
	RaceOfChar = input("Choose your Race: ")
	while RaceOfChar != "dwarf" or "elf" or "human" or "Dwarf" or "Elf" or "Human":
	print("I apologize, but that race is not available for this adventure.")
	print("Please choose from the following options: Dwarf, Elf, or Human.")
	RaceOfChar = input("Choose your Race: ")

	return RaceOfChar

#####END OF choose_char_race METHOD###


#TODO Take the user choice and code in what would result from this choice. Include racial bonuses, features, and any other
# impact to their character








#### BEGIN RACE IMPACT CHANGERATOR ####
def dwarf():
	print ("You have chosen to be a dwarf!")
	print ("Your constitution score increases by 2!")
	ConstitutionOfChar = ConstitutionOfChar+2
	print ("Your speed is set to 25 feet per turn!")
	CharSpeed = 25
	print ("You have advantage on saving throws against poison!")
	SavingThrowCheckArray.append("poison")
	print ("As a dwarf, you have proficiency with the following weapons:\nBattleaxe\nHandaxe\nLight Hammer\nWarhammer")
	ProfiencyArray.append("Battlexe","Handaxe","Light Hammer","Warhammer")
	print ("You also get the opportunity now to choose a tool you would like to be proficient with. \nDo you choose Smith's Tools, Brwer's Supplies, or Mason's Tools?")
	ToolProficiency = input("(Smith, Brewer, Mason?): ")
		def dwarfToolProficiencyCheck(ToolProficiency):
		if ToolProficiency == "Smith":
			print("You have chosen the way of the Blacksmith!")
			ProfiencyArray.append("Smith's Tools")
		elif ToolProficiency == "Brewer":
			print("You have chosen the way of the Brewer! \nMmm... Beer.")
			ProficiencyArray.append("Brewer's Tools")
		elif ToolProficiency == "Mason":
			print("You have chosen the way of the Stonemason!")
			ProfiencyArray.append("Mason's Tools")
		else:
			print("Hmm... I don't recognize what that choice means. Please be sure to speak clearly, and enunciate.")
			ToolProficiency = input("(Smith, Brewer, Mason?): ")
			ToolProficiency = dwarfToolProficiencyCheck(ToolProficiency)
	print("")


def elf():
	print ("You have chosen to be a elf!")

def human():
	print ("You have chosen to be a human!")
########################################

#### BEGIN CLASS IMPACT CHANGERATOR ####



print("Excellent. Now we will roll your attribute scores. These will affect how well your character operates in this world.")

#TODO Import the stats generation script. Also, depending on the CLASS chosen, give the user a choice between the "preferred" option
# or to go their own path. 

#TODO Designate the points from generation into attribute scores along with the racial bonuses. 
#VARIABLES MODIFIED HERE: Str, Chr, Wis, Int, Dex, Con

#TODO Generate Hit Points based off the designation of attribute scores 
#VARIABLES MODIFIED HERE: Hit Points

#TODO Generate Initial Skill Scores. As a bonus, incorporate proficency bonus
#

#VARIABLES USED: STR, DEX, CON, INT, WIS, CHA, ProficencyBonus

# STR Skills: Athletics
# DEX Skills: Acrobatics, Sleight of Hand, Stealth
# INT Skills: Arcana, History, Investigation, Nature, Religion
# WIS Skills: Animal Handling, Insight, Medicine, Perception, Survival
# CHA Skills: Deception, Intimdation, Performance, Persuasion

#Flow should read in stats, and then assign the sum of stat and proficiency bonus to the skill.
skill_names = ['Athletics', 'Acrobatics', 'Sleight of Hand', 'Stealth', \
                'Arcana', 'History', 'Investigation', 'Nature', 'Religion', \
                'Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival' \
                'Deception', 'Intimdation', 'Performance', 'Persuasion' ]

def skill_list_gen(skill):
	skill_list = []

	
	#This will assemble the pairing
	for i in range(0,len(skill)):
		skill_pair = {skill[i]:0}
		skill_list.append(skill_pair)
	print(skill_list)
	
skill_list_gen(skill_keys)

   # def char_skill_gen(stat):
            #skill_list = []
            
            
        #if stat == 'STR':
                
        #elif stat == 'DEX':
       # elif stat == 'INT':
        #elif stat == 'WIS':
       # elif stat == 'CHA':
        #else:
                #continue
        
                
                    
        


#TODO Make the user selec character details like faith, physical descriptors, height/weight/etc. 

#TODO Make the user select a background FROM Entertainer, Hermit, Urchin. 

#TODO Make the user craft the equipment choices for the initial character based off the 5th edition layout. 

#TODO Write the charachter choices to a file for permenance. 

#
