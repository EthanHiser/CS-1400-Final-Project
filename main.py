#main file for text-based game

class Player():
#Class to determine player's name and initialize program
	def __init__(self):
		self.name = input(f"GAME BEGUN.\nWhat is your name?\n").title()
		print(f"{self.name} begins a maybe-not-so-epic quest!\n")

inventory = []

class Menu(Player):
#Class that will be called multiple times to allow player many commands
	def __init__(self):
		ui = ""
		while ui != "R":
			ui = input(f"\nThis is the menu, here you may:\nI - View Inventory\nS - Save Game\nL - Load Game\nR - Return to Game\nQ - Quit Game\n").title()
			if ui == "I":
				print(f"\nInventory: {inventory}")
			elif ui == "S":
				print(f"\nGame Saved!")
			elif ui == "L":
				print(f"\nGame Loaded!")
			elif ui == "R":
				print()
			elif ui == "Q":
				print(f"\nQuitting the game will NOT save; therefore, you may want to save before quitting.")
				ui = ""
				ui = input("Would you like to 'quit' game or 'return' to menu to save?\n")
				if ui == "quit":
					print(f"\nThanks for playing, goodbye.\n")
					exit()
				elif ui == "return":
					print()
				else:
					print(f"\nInput was not recognized, returning to menu.")
					print()

class Game(Player):
	def Bedroom(self):
		print(f"Bedroom")
	def __init__(self):
		ui = None
		while ui != "Menu":
			ui = input(f"What would you like to do?\nAccess 'Menu'\n'Grab' item\n").title()
			if ui == "Menu":
				Menu()
				Game()
			elif ui == "Grab":
				print(f"HI")
				print(f"{inventory}")
				inventory.append("Rock")
			elif ui == "Q":
				print(f"QQQ")
def Bedroom():
	ui = ""
	while ui != "Menu":
		ui = input(f"You hear...").title()
		if ui == "Menu":
			Menu()
			Bedroom()
		elif ui == "grab":
			inventory.append("Rock")
Player()
Bedroom()