#main file for text-based game
class Player():
#Class to determine player's name and initialize program
	def __init__(self):
		self.name = input(f"GAME BEGUN.\nWhat is your name?\n").title()
		print(f"{self.name} begins a maybe-not-so-epic quest!\n\n\tREMEMBER: You may always access the Menu by inputting 'Menu'.\n")

inventory = []
BedroomVar = 0
FrontyardVar = 0
DresserVar = 0
MirrorVar = 0


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
			else:
				print(f"\nInput not recognized; try again.")
				Menu()

class Car():
#Class for the primary game objective (fixing and leaving through car)
	def __init__(self):
		print("Car!")

def Iti(word):
#function to italicize words (words that are interactable or grabbable)
	italics = '\033[3m'
	end = '\033[0m'
	word = (italics + word + end)
	return word

###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---

def Bedroom():
#starting location
	global BedroomVar
	global DresserVar
	dresser = Iti("dresser")
	ui = ""
	if BedroomVar == 0:
		print(f"Screams of the distance awaken you from your short lived slumber, and thus your stay here.\n\tYou sit up and out of the creaking bed, grab your rifle off the {dresser}, begin to head to the garage.")
	else:
		print(f"You re-enter the master bedroom; not much is here besides a {dresser} and bedframe.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'West', 'South', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Bedroom()
		elif ui == "South":
			BedroomVar = 1
			KidsRoom()
		elif ui == "East":
			BedroomVar = 1
			UpHall()
		elif ui == "West":
			BedroomVar = 1
			Bathroom()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Dresser":
				if DresserVar == 0:
					print(f"\nYou open the dresser and find an old flashlight, but upon clicking it you find it has no batteries.\n")
					print(f"+ Flashlight!\n")
					inventory.append("Dead Flashlight")
					DresserVar = 1
					if "Batteries" in inventory:
						print(f"You place your batteries from the toolbox into the flashlight; making them useful once more.\n")
						print(f"+ Charged Flashlight!\n- Dead Flashlight!\n- Batteries!\n")
						inventory.append(f"Charged Flashlight")
						inventory.remove(f"Dead Flashlight")
						inventory.remove(f"Batteries")
				else:
					print(f"\nYou open the dresser again and find nothing.\n")
			else:
				print(f"\nInput either not recognized or not valid right now.\n")
				Bedroom()
		else:
			print(f"\nInput not recognized; try again.\n")
			Bedroom()

def Bathroom():
	ui = ""
	global MirrorVar
	mirror = Iti("mirror")
	print(f"You enter the master bedroom's bathroom. In it, cracked {mirror} and stained walls.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Bathroom()
		elif ui == "East":
			Bedroom()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Mirror":
				if MirrorVar == 0:
					print(f"\nYou open the damaged mirror and pull out a few bobby pins.\n")
					print(f"+ Bobby Pins\n")
					inventory.append(f"Bobby Pins")
					MirrorVar = 1
				else:
					print(f"\nYou re-open the bathroom mirror but find only forgotten medicine bottles.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
				Bathroom()
		else:
			print(f"\nInput not recognized; try again.\n")
			Bathroom()

def KidsRoom():
	ui = ""
	print(f"Seeing strewn toys and clothing about; you must be in the room that was once for the children of this home.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'East' ///\n").title()
		if ui == "Menu":
			Menu()
			KidsRoom()
		elif ui == "North":
			Bedroom()
		elif ui == "East":
			UpHall()
		else:
			print(f"\nInput not recognized; try again.\n")
			KidsRoom()

def UpHall():
	ui = ""
	print(f"You enter the hallway connecting two bedrooms and a staircase. You see a wanning crescent glisten through the dilapidated roof.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'West', 'Down' ///\n").title()
		if ui == "Menu":
			Menu()
			UpHall()
		elif ui == "West":
			Bedroom()
		elif ui == "Down":
			LivingRoom()
		else:
			print(f"\nInput not recognized; try again.\n")
			UpHall()

def LivingRoom():
	ui = ""
	print(f"Your movement silently rocks a thin wooden chair in front of an old television set. The rug of this living room is moldy in wet.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'West', 'Up', 'Down' ///\n").title()
		if ui == "Menu":
			Menu()
			LivingRoom()
		elif ui == "West":
			DiningRoom()
		elif ui == "East":
			Garage()
		elif ui == "Up":
			UpHall()
		elif ui == "Down":
			Cellar()
		else:
			print(f"\nInput not recognized; try again.\n")
			LivingRoom()

def DiningRoom():
	ui = ""
	print(f"A low light lamp lights the family table. China and cutlery are littered on the floor.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'East', 'South' ///\n").title()
		if ui == "Menu":
			Menu()
			DiningRoom()
		elif ui == "North":
			ui = input(f"\nWould you like to enter the 'Kitchen' or 'Hallway'?\n").title()
			if ui == "Kitchen":
				Kitchen()
			elif ui == "Hallway":
				DownHall()
		elif ui == "East":
			LivingRoom()
		elif ui == "South":
			Frontyard()
		else:
			print(f"\nInput not recognized; try again.\n")
			DiningRoom()

def Kitchen():
	ui = ""
	print(f"Walking on the checkboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'South' ///\n").title()
		if ui == "'Menu":
			Menu()
			Kitchen()
		elif ui == "East":
			DownHall()
		elif ui == "South":
			DiningRoom()
		else:
			print(f"\nInput not recognized; try again.\n")
			Kitchen()

def DownHall():
	ui = ""
	print(f"You pass by frames of photos of bygone children; through the home's backdoor you see the moon-lit yard")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'West', 'South' ///\n").title()
		if ui == "Menu":
			Menu()
			DownHall()
		elif ui == "North":
			Backyard()
		elif ui == "West":
			Kitchen()
		elif ui == "South":
			DiningRoom()
		else:
			print(f"\nInput not recognized; try again.\n")
			DownHall()

def Garage():
	ui = ""
	print(f"Perhaps the only room that appears like its pre-war self; the garage is where your nearly handmade 'car' is dimly light by a single bulb.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'West', 'Car' ///\n").title()
		if ui == "Menu":
			Menu()
			Garage()
		elif ui == "West":
			LivingRoom()
		elif ui == "Car":
			Car()
			Garage()
		else:
			print(f"\nInput not recognized; try again.\n")
			Garage()

def Cellar():
	ui = ""
	print(f"You walk down into the cellar; all is silent but the cyclic dripping from somewhere.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'Up' ///\n").title()
		if ui == "Menu":
			Menu()
			Cellar()
		elif ui == "East":
			DeepCellar()
		elif ui == "Up":
			LivingRoom()
		else:
			print(f"\nInput not recognized; try again.\n")
			Cellar()

def DeepCellar():
	ui = ""
	if " Charged Flashlight" in inventory:
		print(f"Now able to see with your flashlight, you can see.")
		while ui != "Menu":
			ui = input(f"/// Inputs: 'West' ///\n").title()
			if ui == "Menu":
				Menu()
				DeepCellar()
			elif ui == "West":
				Cellar()
			else:
				print(f"\nInput not recognized; try again.\n")
				DeepCellar()
	else:
		print(f"\nThis part of the cellar is so far from the staircase that visibility is naught, you need some sort of tool to aid your eyes to proceed.")
		print(f"Returning east to the lit part of the cellar.\n")
		Cellar()

def Backyard():
	ui= ""
	print(f"Exiting the house you feel the early morning dew brush against your boots.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'South' ///\n").title()
		if ui == "Menu":
			Menu()
			Backyard()
		elif ui == "South":
			DownHall()
		else:
			print(f"\nInput not recognized; try again.\n")
			Backyard()

def Frontyard():
	global FrontyardVar
	ui = ""
	if FrontyardVar == 0:
		print(f"As you open the front door, leaving the home, a faraway explosion is heard followed by more screams.\n\tYou should leave soon.")
	else:
		print(f"You walk by the gray picket fences in front of the house")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'East', 'West' ///\n").title()
		if ui == "Menu":
			Menu()
			Frontyard()
		elif ui == "North":
			FrontyardVar = 1
			DiningRoom()
		elif ui == "East":
			FrontyardVar = 1
			FrontyardEast()
		elif ui == "West":
			FrontyardVar = 1
			FrontyardWest()
		else:
			print(f"\nInput not recognized; try again.\n")
			Frontyard()

def FrontyardEast():
	ui = ""
	print(f"You walk farther east from the house, any more distance would be dangerous.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'West' ///\n").title()
		if ui == "Menu":
			Menu()
			FrontyardEast()
		elif ui == "West":
			Frontyard()
		else:
			print(f"\nInput not recognized; try again.\n")
			FrontyardEast()

def FrontyardWest():

	ui = ""
	print(f"You walk farther west from the house, any more distance would be dangerous.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East' ///\n").title()
		if ui == "Menu":
			Menu()
			FrontyardWest()
		elif ui == "East":
			Frontyard()
		else:
			print(f"\nInput not recpgnized; try again.\n")
			FrontyardWest()

Player()
Bedroom()