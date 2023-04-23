#main file for text-based game
class Menu():
	def __init__(self):
		ui = ""
		while ui != "R":
			ui = input(f"\nThis is the menu, here you may:\nI - View Inventory\nS - Save Game\nL - Load Game\nR - Return to Game\nQ - Quit Game\n").title()
			if ui == "I":
				print(f"{inventory}")
			elif ui == "S":
				print(f"Game Saved!\n")
			elif ui == "L":
				print(f"Game Loaded!\n")
			elif ui == "R":
				print()
			elif ui == "Q":
				print(f"Thanks for playing, goodbye.")
				exit()
			else:
				print(f"Input not recognized, try again.\n")

class Player():
	def __init__(self):
		self.name = input(f"GAME BEGUN.\nWhat is your name?\n").title()
		self.inventory = []
		print(f"{self.name} begins a maybe-not-so-epic quest!\n")
	def get_invetory(self):
		return self.inventory

class Game(Player):
	def __init__(self):
		ui = None
		while ui != "Menu":
			ui = input(f"What would you like to do?\nAccess 'Menu'\n'Grab' item\n")
			if ui == "Menu":
				Menu()
				Game()
			elif ui == "grab":
				print(f"HI")
				print(f"{self.inventory}")
			elif ui == "Q":
				print(f"QQQQQQQQQQ")
Player()
Game()
