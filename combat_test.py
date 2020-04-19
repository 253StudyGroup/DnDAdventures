#Combat Test File
#This allows us to test the classes from the enemy.py file. 

from enemy import *

random_enemy = Enemy(10, 25, 3)

print(random_enemy.ArmorClass)
print(random_enemy.Speed)
print(random_enemy.ChallengeRating)

gobbo = Goblin(15, 30, '1/4')

print(gobbo.ArmorClass)
print(gobbo.Speed)
print(gobbo.ChallengeRating)

print(gobbo.HitPoints)
print(gobbo.StatList)

gobbo.set_hp()
gobbo.set_stats()

print(gobbo.HitPoints)
print(gobbo.StatList)

gobbo2 = gobbo = Goblin(15, 30, '1/4')

gobbo2.set_hp()
gobbo2.set_stats()

print(gobbo2.HitPoints)
print(gobbo2.StatList)