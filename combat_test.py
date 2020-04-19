#Combat Test File
#This allows us to test the classes from the enemy.py file. 

#This is required to bring in the classes and methods we described in another file.
from enemy import *

#We are creating an instance of the standard 'Enemy' Template by calling it's class
random_enemy = Enemy(10, 25, 3)

#Here we show that there are values assigned to the attributes. 
print(random_enemy.ArmorClass)
print(random_enemy.Speed)
print(random_enemy.ChallengeRating)

#Now we create a second instance, this time with the child Class that uses some of Enemy class attributes
gobbo = Goblin(15, 30, '1/4')

print(gobbo.ArmorClass)
print(gobbo.Speed)
print(gobbo.ChallengeRating)

#Here we print the Goblin default attributes
print(gobbo.HitPoints)
print(gobbo.StatList)

#both methods adjust the default attributes we printed a moment ago. 
gobbo.set_hp()
gobbo.set_stats()

#We've now printed the updated attributes after the methods have interacted with them
print(gobbo.HitPoints)
print(gobbo.StatList)

#Now we repeat with a second instance of the same child class. 
gobbo2 = gobbo = Goblin(15, 30, '1/4')

gobbo2.set_hp()
gobbo2.set_stats()

#Note that while we have the same value of StatList, it's treated as a seperate variable. 
#HitPoints will likely be different as well. 
print(gobbo2.HitPoints)
print(gobbo2.StatList)