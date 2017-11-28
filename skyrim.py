#Pyrim: A Python word-based game set in the world of Skyrim


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

class ItemList():
	weapons = {
#	Weapon Name : [Dmg, Weight, Effect, Effect chance] 	
	'Iron Sword' : [7, 9, 'none', 0],
	'Iron Dagger' : [4, 2, 'none', 0],
	'Iron Axe' : [8, 11, 'none', 0],
	'Iron Greatsword' : [15, 16, 'none', 0],
	'Dawnbreaker' : [12, 10, 'burn', 25],
	'Chillrend' : [15, 16, 'slow', 50]
	}
	
	armors = {
#	Armor Name : [Rating, Weight]
	'Fur Armor' : [23, 6],
	'Iron Armor' :[30, 30],
	'Steel Armor' : [40, 37]
	}
	
class Quest():
	pass 

class BanditCave(Quest):
	pass

class Forest(Quest):
	pass
	
class CharCreation():
	def prompt(self):
		choice = raw_input("> ")
		if choice == '1' or choice == 'Warrior':
			print "You have chosen the Warrior class and recieved an Iron Sword"
			Attributes.str = 14
			Attributes.dex = 7
			Attributes.int = 9
			Inventory.weapon = 'Iron Sword'
			Inventory.armors = 'Fur Armor'
		elif choice == '2' or choice == 'Thief':
			print "You have chosen the Thief class and recieved an Iron Dagger"
			Attributes.str = 9
			Attributes.dex = 14
			Attributes.int = 7
			Inventory.weapon = 'Iron Dagger'
			Inventory.armors = 'Fur Armor'	
		elif choice == '3' or choice == 'Mage':
			print "You have chosen the Warrior class and recieved an Iron Axe"
			Attributes.str = 7
			Attributes.dex = 9
			Attributes.int = 14
			Inventory.weapon = 'Iron Axe'
			Inventory.armors = 'Fur Armor'	
		else:
			print "[INVALID INPUT]"
			self.prompt
		
			
	def quest(self):
		choice = raw_input("> ")
		if choice == '1' or choice == 'Bandit Cave':
			print "You proceed East towards the Bandit Cave"
			go = BanditCave()
			go.play
		if choice == '2' or choice == 'Forest':
			print "You proceed West towards the Forest"
			go = Forest()
			go.play
	def run(self):
		print "Choose your class"
		print "[1]Warrior, [2]Thief, [3]Mage"
		self.prompt()
		print "Now choose your first quest"
		print "[1]Bandit Cave, [2]Forest, [3]Sewers" 
		self.quest()
		
Game = CharCreation()			
Game.run()
