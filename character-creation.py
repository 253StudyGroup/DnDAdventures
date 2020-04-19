import pygame

###### VARIABLE CREATION CENTER ##### -CP 04/18/2020 @ 4:30pm on a Saturday
HitPoints = 0
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
	ClassOfChar = input("Create your Class:")

	return ClassOfChar
####END OF choose_char_class METHOD####

def choose_char_race():
	print("What Race would you like to be?")
	print("You could be flexible like a human, agile like an elf, or hearty as a dwarf!")
	print("Pick the race which you would prefer to play in this realm.")
	RaceOfChar = input("Choose your Race:")
	return RaceOfChar

#TODO Take the user choice and code in what would result from this choice. Include racial bonuses, features, and any other
# impact to their character


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
