import random



class Item:
	pass



class Weapon(Item):

	def __init__(self, name):
		""" """
		self.name = name

	def effect(self, enemy):
		""" """
		if self.name == 'POCKET_SAND.exe':
			self.pocket_sand(enemy)

	def pocket_sand(self, enemy):
		""" """
		enemy.flinchability = 1
		print('{} got (virtual) sand in his eyes! Cheap move!\n'.format(enemy.name))
		return enemy.flinchability



class Potion(Item):

	def __init__(self, attribute=1):
		""" """
		self.attribute = attribute
		self.attribute_name = {
			1: 'Health',
			2: 'STR UP',
			3: 'DEF UP',
			4: 'AGILE UP'
		}

		self.name = '{} potion'.format(self.attribute_name[self.attribute])

	def effect(self, player):
		""" """
		if self.attribute == 1:
			self.healing(player)
		elif self.attribute == 2:
			self.strength_up(player)
		elif self.attribute == 3:
			self.defense_up(player)
		elif self.attribute == 4:
			player.isagile = True
			print('{} drank an AGILE UP potion...'.format(player.name))
			print('Now their heavy attacks won\'t miss!\nWhat an overpowered potion!!!\n')

	def healing(self, player):
		""" """
		player.health += 50
		if player.health > 100:
			player.health = 100
			print('A {} healed {} to the max!\n'.format(self.name, player.name))
		else:
			print('A {} healed {} 50 points!\n'.format(self.name, player.name))

		return player.health

	def strength_up(self, player):
		""" """
		player.strength += 0.25
		print('A {} increased {}\'s strength!\n'.format(self.name, player.name))

		return player.strength

	def defense_up(self, player):
		""" """
		player.defense += 0.25
		print('A {} increased {}\'s defense!\n'.format(self.name, player.name))

		return player.defense




