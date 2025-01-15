import random

from items import Weapon, Potion



class Player:

	def __init__(self, name):
		""" """
		self.name = name
		self.health = 100
		self.inventory = [Weapon('POCKET_SAND.exe')]

		self.strength = 1
		self.defense = 1
		self.flinchability = 0

		self.isagile = False # turn on w/ AGILE UP potion

		self.inputs = {
			1: self.basic_attack,
			2: self.heavy_attack,
			3: self.heal_self,
			4: self.check_inventory,
		}

	def __str__(self):
		""" """
		return self.name

	def print_menu(self):
		""" """
		print('1. Use basic attack.')
		print('2. Use heavy attack.')
		print('3. Heal!')
		print('4. Check your "holoDict".{}'.format(' (empty)' if len(self.inventory) == 0 else ''))

	def fight(self, enemy):
		""" """
		self.turn_over = False

		self.maybeflinch()

		while not self.turn_over:
			print('{}\'s turn:'.format(self.name))
			self.print_menu()
			selection = input('Choice: '.format(self.name))
			
			try:
				action = self.inputs.get(int(selection), None)
			except ValueError:
				# print('\n{} isn\'t even a number!!'.format(selection))
				action = 10 # allows janky passage through next ifelse

			if action in self.inputs.values():
				if action == self.heal_self:
					action(enemy)
				else:
					action(enemy)
				self.turn_over = True
			else:
				print('You have to do something!!')
				print('')

		return enemy
				
	def basic_attack(self, enemy):
		""" a guarenteed moderate damage attack. """
		damage = (random.randint(18, 25) * self.strength) / enemy.defense
		enemy.health -= damage
		print('{}\'s basic attack did {} damage!\n'.format(self.name, damage))

		return round(enemy.health, 2)

	def heavy_attack(self, enemy):
		""" high damage attack, but with a chance to miss! """
		damage = (random.randint(5, 50) * self.strength) / enemy.defense

		if damage / self.strength > 18 or self.isagile:
			enemy.health -= damage
			print('{}\'s heavy attack did {} damage!\n'.format(self.name, damage))
		elif damage / self.strength >= 45:
			enemy.health = 0
			print('{}\'s heavy attack was a critical hit! KO!!!'.format(self.name))
		else:
			enemy.health = enemy.health
			print('{}\'s heavy attack missed!!\n'.format(self.name))

		return round(enemy.health, 2)

	def heal_self(self, enemy):
		""" a moderate healing spell """
		healage = random.randint(18, 25)
		self.health += healage

		if self.health > 100:
			self.health = 100
			print('{} healed to 100!\n'.format(self.name))

		else:
			print('{} healed {} points!\n'.format(self.name, healage))

		return self.health

	def check_inventory(self, enemy):
		""" """
		self.lookin_at_inventory = True

		while self.lookin_at_inventory:
			if len(self.inventory) > 0:
				pocketview = {k+1: item.name for k, item in enumerate(self.inventory)}
				print('\nIt seems to contain some executables..\n'.format(self.name), '{}\n'.format(pocketview))

				goback = (list(pocketview.keys())[-1] + 1)
				print(f"{goback}. Maybe i\'ll save th{'is' if len(self.inventory) == 1 else 'ese'} for later...")

				try:
					choice = int(input('Use something? (exit={}): '.format(goback)))
					print('')
				except ValueError:
					choice = goback # allows passage through next ifelse

				if int(choice) in pocketview:
					self.lookin_at_inventory = False
					item = self.inventory[int(choice)-1]
					if isinstance(item, Potion):
						item.effect(self)
						self.inventory.remove(item)
					if isinstance(item, Weapon):
						item.effect(enemy)
						self.inventory.remove(item)

				elif int(choice) == goback:
					self.lookin_at_inventory = False
					self.fight(enemy)

				else:
					print('{} used nothing!'.format(self.name))
					self.lookin_at_inventory = False

			else:
				print('You got nothin\'!')
				self.lookin_at_inventory = False

	def maybeflinch(self):
		""" """
		if self.flinchability > 0:
			ohfuckchance = random.randint(1,5)
			if ohfuckchance > 3:
				self.turn_over = True
				self.flinchability -= ohfuckchance * 0.1 # lowers chance of flinching each flinch
				print('Oh snap, that pocket sand got {} flinching!'.format(self.name))
				print('He must be upset!\n')
			else:
				self.flinchability = 0  # get lucky and have clean eyes!
				print('{} shook off the pocket sand!\n'.format(self.name))

		return self.flinchability



class LivePlayer(Player):
	pass



class CompPlayer(Player):

	def __init__(self):
		""" """
		super().__init__(self)

		self.name = random.choice(['Earl', 'Jimmy', 'Wendyl', 'Dirk', 'Sphen'])
		self.inputs.update({4: self.use_item})

	def use_item(self, enemy):
		""" """
		if len(self.inventory) > 0:
			item = random.choice(self.inventory)
			if isinstance(item, Potion):
				print('{} used {}!'.format(self.name, item.name))
				item.effect(self)
				self.inventory.remove(item)
			if isinstance(item, Weapon):
				print('{} used {}!'.format(self.name, item.name))
				item.effect(enemy)
				self.inventory.remove(item)
		else:
			print('{} got caught lookin\' through an empty "holoDeck"!\n'.format(self.name))
			
	def fight(self, enemy):
		""" """
		self.turn_over = False
		self.maybeflinch()

		while not self.turn_over:
			if self.health > 80:
				action = self.inputs.get(random.choice([1,2,4]))
			else:
				action = self.inputs.get(random.randint(1,4))

			print('{}\'s turn!\n'.format(self.name))
			return action(enemy)



class Monster(CompPlayer):
	pass





