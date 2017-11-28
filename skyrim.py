#Pyrim: A Python word-based game set in the world of Skyrim
import data.py

class Attributes():	
	lvl = 0
	
	str = 0
	int = 0
	dex = 0
	
	dmg = 0
	armor=0
	
	poison = False
	burn = False
	stun = False 
	slow = False 
	
class Inventory():
	weapon =  ''
	armor = ''
	
	pass

class CharCreation():
	def run(self):
		print "Choose your class"
		print "[1]Warrior, [2]Thief, [3]Mage"
		raw_input
