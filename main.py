import pickle
#main file for text-based game
class Player():
#Class to determine player's name and initialize program
	def __init__(self):
		self.name = input(f"GAME BEGUN.\nWhat is your name?\n").title()
		print(f"{self.name} begins a maybe-not-so-epic quest!\n\n\tREMEMBER: You may always access the Menu by inputting 'Menu'.\n")

#multiple variables that will be called, saved, and loaded.
CarObjevInven = ["Cooling Fan", "Hose", "Air Filter", "Exhaust Pipe", "Light Bulb"]
inventory = []
BedroomVar = 0
FrontyardVar = 0
DresserVar = 0
MirrorVar = 0
ToolboxVar = 0
CarVar = 0
ChairVar = 0
LightbulbVar = 0
HoseVar = 0
PipeVar = 0
StickVar = 0
BladeVar = 0
FanVar = 0
UnitVar = 0
FanShellVar = 0
GooseVar = 0

class Menu(Player):
#Class that will be called multiple times to allow player many commands
	def __init__(self):
		ui = ""
		while ui != "R":
			ui = input(f"\nThis is the menu, here you may:\nI - View Inventory\nS - Save Game\nL - Load Game\nR - Return to Game\nQ - Quit Game\n").title()
			if ui == "I":
				print(f"\nInventory: {inventory}")
			elif ui == "S":
				Save()
				print(f"\nGame Saved!")
			elif ui == "L":
				Load()
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

class Save():
#Class for saving all of the variables of the player/map
	with open("game.dat", "wb") as f:
		pickle.dump(CarObjevInven, f)
		pickle.dump(inventory, f)
		pickle.dump(Player, f)
		pickle.dump(BedroomVar, f)
		pickle.dump(FrontyardVar, f)
		pickle.dump(DresserVar, f)
		pickle.dump(MirrorVar, f)
		pickle.dump(ToolboxVar, f)
		pickle.dump(CarVar, f)
		pickle.dump(ChairVar, f)
		pickle.dump(LightbulbVar, f)
		pickle.dump(HoseVar, f)
		pickle.dump(PipeVar, f)
		pickle.dump(BladeVar, f)
		pickle.dump(FanVar, f)
		pickle.dump(UnitVar, f)
		pickle.dump(FanShellVar, f)
		pickle.dump(GooseVar, f)

class Load():
	def __init__(self):
		global Player
		global inventory
		global CarObjevInven
		global BedroomVar
		global FrontyardVar
		global DresserVar
		global MirrorVar
		global ToolboxVar
		global CarVar
		global ChairVar
		global LightbulbVar
		global HoseVar
		global PipeVar
		global StickVar
		global BladeVar
		global FanVar
		global UnitVar
		global FanShellVar
		global GooseVar
		try:
			with open("game.dat", "rb") as f:
				CarObjevInven = pickle.load(f)
				inventory = pickle.load(f)
				Player = pickle.load(f)
				BedroomVar = pickle.load(f)
				FrontyardVar = pickle.load(f)
				DresserVar = pickle.load(f)
				MirrorVar = pickle.load(f)
				ToolboxVar = pickle.load(f)
				CarVar = pickle.load(f)
				ChairVar = pickle.load(f)
				LightbulbVar = pickle.load(f)
				HoseVar = pickle.load(f)
				PipeVar = pickle.load(f)
				BladeVar = pickle.load(f)
				FanVar = pickle.load(f)
				UnitVar = pickle.load(f)
				FanShellVar = pickle.load(f)
				GooseVar = pickle.load(f)
		except FileNotFoundError:
			print(f"\nFile not found!")


class Car():
#Class for the primary game objective (fixing and leaving through car)
	def __init__(self):
		global CarVar
		ui = ""
		CarObjevInven = []
		if CarObjevInven == []:
			print(f"\n ||| Now, with all the required car parts, you are able to successfully start the engine of your vehicle.\n\tDriving out of the garage you see an illuminated sign that indicates an upcoming offshoot. ||| \n")
			while ui != "Main":
				ui = input(f"\t/// Do you take the 'main' path or the 'offshoot'? ///\n").title()
				if ui == "Main":
					print(f"\nDriving continuouly down the main path, you are able to leave the home's property a final time.\n\tHopefuly this world has intentions in your favor...\n\n ||| Thanks for playing! Goodbye. |||\n")
					quit()
				elif ui == "Offshoot":
					print(f"\nLeaving the main path, and taking the offshoot, you drive down an unpaved road until you see a small shack.\n\tUpon entering you see nothing but a large, metal door and a keypad.\n")
					while ui != "1218":
						ui = input(f"/// What is the code? ///\n").title()
						if ui == "1218":
							print(f"\nThe metal door loudly opens revealing a single, white LED light.\n\tEntering the small room the door closes behind you and the room shakes downward.\n\t\tThe door opens again revealing an open earth cave.")
							print(f"\t\t\tNestled in the stalagmites you see a grand vault door and labeled above it a quote:\n\t\t\t\t\"Qui quasi anas sonant, sunt qui supersunt.\"\n")
							print(f"||| Thanks for playing! goodbye. |||\n")
							quit()
						elif ui == "Exit":
							print(f"\nFaling to know the code, you exit the shack and drive down the pathway.\n\tHopefuly this world has intenions in your favor...\n\n\t ||| Thanks for playing! Goodbye. |||\n")
							quit()
						else:
							print(f"\nThat was not the code, input 'Exit' to leave the shack.\n")
						
				else:
					print(f"\nInput not recognized or not valid right now.\n")
			quit()
		if CarVar == 0:
			print(f"\nYou get get into your somber excuse of a 'car' and start the engine.\n\tUpon starting it though the vehicle sputters into silence. Opening the hood you realize its cooling fan is gone;\n\t\tin fact, the hoses, exhuast, air filter, and lights are gone. You've been robbed.\n")
			print(f"\t/// Objective: Get {CarObjevInven} ///\n")
			CarVar = 1
		else:
			print(f"\n\t/// Objective: Get {CarObjevInven} ///\n")

def Iti(word):
#function to italicize words (things that are interactable)
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
					print(f"\nYou open the dresser again and find nothing of interest.\n")
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
	global FanVar
	fan = Iti("fan")
	if FanVar == 0:
		print(f"Seeing strewn toys and clothing about; you must be in the room that was once for the children of this home.\n\tAbove a derelict cradle you see a small celing {fan}.")
	else:
		print(f"Seeing strewn toys and clothing about; you must be in the room that was once for the children of this home.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'East', 'South' 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			KidsRoom()
		elif ui == "North":
			Bedroom()
		elif ui == "East":
			UpHall()
		elif ui == "South":
			Roof()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Fan":
				if FanVar == 0:
					print(f"\nYou rip the fan off the ceiling, dust and a cockroach fall to the floor.\n")
					print(f"+ Fan Blades\n")
					inventory.append(f"Fan Blades")
					FanVar = 1
					if "Fan Shell" in inventory:
						print(f"Using the fan shell from the cellar, you are able to make a portable cooler.\n")
						print(f"+ Cooler\n")
						inventory.append(f"Cooler")
						inventory.remove(f"Fan Blades")
						inventory.remove(f"Fan Shell")
						CarObjevInven.remove(f"Cooling Fan")
					else:
						print(f"You could use these fan blades for something if you had a shell to hold them in.\n")
				else:
					print(f"\nOne cannot simply interact with a ceiling fan that which has already been so.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
				KidsRoom()
		else:
			print(f"\nInput not recognized; try again.\n")
			KidsRoom()

def Roof():
	ui = ""
	global UnitVar
	global GooseVar
	unit = Iti("unit")
	if GooseVar == 0:
		print(f"Opening the window, you step out onto the roof. From up here you can see a blazing, orange glow in the distance.\n\tAs you look at its fierce size, a herd of geese fly overhead. To your right is an old air-conditioning {unit} that may still work.")
		GooseVar = 1
	elif UnitVar == 0:
		print(f"Opening the window, you step out onto the roof. From up here you can see a blazing, orange glow in the distance.\n\tTo your right is an old air-conditioning {unit} that may still work.")
	else:
		print(f"Opening the window, you step out onto the roof. From up here you can see a blazing, orange glow in the distance.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Roof()
		elif ui == "North":
			KidsRoom()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Unit":
				if UnitVar == 0:
					if "Shiv" in inventory:
						print(f"\nYou cut out the air-conditioning unit to use as a makeshift air filter.\n")
						print(f"+ Cooler\n")
						inventory.append(f"Air Filter")
						CarObjevInven.remove(f"Air Filter")
						UnitVar = 1
					else:
						print(f"\nYou think that you could probaly put this cooler to good use if you could only extract it.\n")
				else:
					print(f"Since you've already extracted the AC, ya just can't 'gain.")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
				Roof()
		else:
			print(f"\nInput not recognized; try again.\n")
			Roof()

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
			else:
				print(f"\nInput not recognized; try again.\n")
		elif ui == "East":
			LivingRoom()
		elif ui == "South":
			Frontyard()
		else:
			print(f"\nInput not recognized; try again.\n")
			DiningRoom()

def Kitchen():
	global LightbulbVar
	global ChairVar
	ui = ""
	lightbulb = Iti("lightbulb")
	chair = Iti("chair")
	if LightbulbVar == 1:
		print(f"Walking on the checkerboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.")
	elif ChairVar == 1:
		print(f"Walking on the checkerboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.\n\tThough you do see a flickering {lightbulb} above a now right-side up chair.")
	else:
		print(f"Walking on the checkerboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.\n\tThough you do see a flickering {lightbulb} above an overturned {chair}.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'South', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Kitchen()
		elif ui == "East":
			DownHall()
		elif ui == "South":
			DiningRoom()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Lightbulb":
				if LightbulbVar == 0:
					if ChairVar == 0:
						print(f"\nYou attempt to unscrew the lightbulb on the ceiling, but just can't reach it.\n")
					else:
						print(f"\nStanding on the chair, you unscrew the lightbulb and stash it.\n")
						print(f"+ Light Bulb\n")
						inventory.append(f"Light Bulb")
						CarObjevInven.remove(f"Light Bulb")
						LightbulbVar = 1
				else:
					print(f"\nHaving already removed the light bulb, you can no longer interact with it.\n")
			elif ui == "Chair":
				if ChairVar == 0:
					print(f"\nYou turn the kitchen chair on the floor right-side up.\n")
					ChairVar = 1
				else:
					print(f"\nHaving already turned up the chair, you can no longer interact with it.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
				Kitchen()
		else:
			print(f"\nInput not recognized; try again.\n")
			Kitchen()

def DownHall():
	global BladeVar
	ui = ""
	blade = Iti(f"blade")
	if BladeVar == 0:
		print(f"You pass by frames of photos of bygone children; through the home's backdoor you see the moon-lit yard.\n\tOn the ground you see some sort of {blade}.")
	else:
		print(f"You pass by frames of photos of bygone children; through the home's backdoor you see the moon-lit yard.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'North', 'West', 'South', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			DownHall()
		elif ui == "North":
			Backyard()
		elif ui == "West":
			Kitchen()
		elif ui == "South":
			DiningRoom()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Blade":
				if BladeVar == 0:
					print(f"\nYou carefully pick up the gray, shining blade from the floor.\n")
					print(f"+ Blade\n")
					inventory.append(f"Blade")
					BladeVar = 1
					if "Stick" in inventory:
						print(f"Now; with your stick from earlier, you craft a shiv.")
						print(f"+ Shiv\n- Blade\n- Stick")
						inventory.append(f"Shiv")
						inventory.remove(f"Blade")
						inventory.remove(f"Stick")
				else:
					print(f"\nHaving already picked up the blade, you cannot again.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
				DownHall()
		else:
			print(f"\nInput not recognized; try again.\n")
			DownHall()

def Garage():
	ui = ""
	global ToolboxVar
	toolbox = Iti("toolbox")
	print(f"Perhaps the only room that appears like its pre-war self; the garage is where your nearly handmade 'car'\nis dimly light as well as a {toolbox} by a single bulb.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'West', 'Interact', 'Car' ///\n").title()
		if ui == "Menu":
			Menu()
			Garage()
		elif ui == "West":
			LivingRoom()
		elif ui == "Car":
			Car()
			Garage()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Car":
				Car()
				Garage()
			elif ui == "Toolbox":
				if ToolboxVar == 0:
					print(f"\nYou open the rusty red toolbox and find two old batteries.\n")
					print(f"+ Batteries\n")
					inventory.append(f"Batteries")
					ToolboxVar = 1
					if "Dead Flashlight" in inventory:
						print(f"With your new found batteries, you recharge the old flashlight making it useful once more.")
						print(f"+ Charged Flashlight\n- Dead Flashlight\n- Batteries\n")
						inventory.append(f"Charged Flashlight")
						inventory.remove(f"Dead Flashlight")
						inventory.remove(f"Batteries")
				else:
					print(f"\nYou open the damaged red toolbox again but find nothing of interest.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
				Garage()

		else:
			print(f"\nInput not recognized; try again.\n")
			Garage()

def Cellar():
	global FanShellVar
	ui = ""
	crates = Iti("crates")
	print(f"You walk down into the cellar; all is silent but the cyclic dripping from somewhere.\n\tThere are a few {crates} that look un-opened.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'Up', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Cellar()
		elif ui == "East":
			DeepCellar()
		elif ui == "Up":
			LivingRoom()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Crates":
				if FanShellVar == 0:
					print(f"\nOpening the crates, you unfortunately don't see much of importance but a fan shell with no blades.\n")
					inventory.append(f"Fan Shell")
					FanShellVar = 1
					if "Fan Blades" in inventory:
						print(f"Using your fan blades you pulled from the kids' room, you are able to make a portable cooler.\n")
						print(f"+ Cooler\n")
						inventory.append(f"Cooler")
						inventory.remove(f"Fan Blades")
						inventory.remove(f"Fan Shell")
						CarObjevInven.remove(f"Cooling Fan")
				else:
					print(f"\nOpening the crates again, you don't see much of importance.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
		else:
			print(f"\nInput not recognized; try again.\n")
			Cellar()

def DeepCellar():
	global PipeVar
	ui = ""
	pipe = Iti("pipe")
	if "Charged Flashlight" in inventory:
		if PipeVar == 0:
			print(f"Now able to see with your flashlight, you can see the source of the dripping sound: a leaky {pipe}.\n\tThere's also overgrown cobwebs, and long-forgotten boxes.")
		else:
			print(f"Here in the deep cellar, you see the remains of the leaky pipe you cut, some cobwebs, and old boxes.")
		while ui != "Menu":
			ui = input(f"/// Inputs: 'West', 'Interact' ///\n").title()
			if ui == "Menu":
				Menu()
				DeepCellar()
			elif ui == "West":
				Cellar()
			elif ui == "Interact":
				ui = input(f"/// What do you interact with? ///\n").title()
				if ui == "Pipe":
					if PipeVar == 0:
						if "Shiv" in inventory:
							print(f"\nWith your shiv, you cut off a piece of the small pipe for your car.\n")
							print(f"+ Pipe\n")
							inventory.append(f"Pipe")
							CarObjevInven.remove(f"Exhaust Pipe")
							PipeVar = 1
						else:
							print(f"\nLooking at the pipe, you realize it's the perfect size for your car, but you need something strong to remove it\n")
					else:
						print(f"\nYou can't interact with the pipe again, as it is gone. :(\n")
				else:
					print(f"\nInput either not recognized or not valid right now.\n")
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
		print(f"You walk by the gray picket fences in front of the house.")
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
	global StickVar
	ui = ""
	sticks = Iti(f"sticks")
	if StickVar == 0:
		print(f"You walk farther east from the house, not much is here but a pile of {sticks} and a lone red baneberry.")
	else:
		print(f"You walk farther east from the house, not much is here but a lonesome red baneberry.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'West', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			FrontyardEast()
		elif ui == "West":
			Frontyard()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Sticks":
				if StickVar == 0:
					print(f"\nYou pick up a stick.\n")
					print(f"+ Stick")
					inventory.append(f"Stick")
					StickVar = 1
					if "Blade" in inventory:
						print(f"Now; with your blade from earlier, you craft a shiv.")
						print(f"+ Shiv\n- Stick\n- Blade")
						inventory.append(f"Shiv")
						inventory.remove(f"Blade")
						inventory.remove(f"Stick")
				else:
					print(f"\nHaving already picked up a stick, there is no longer one to.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
		else:
			print(f"\nInput not recognized; try again.\n")
			FrontyardEast()

def FrontyardWest():
	ui = ""
	global HoseVar
	hose = Iti(f"hose")
	if HoseVar == 0:
		print(f"You walk a little farther west of the house and see a dark green garden {hose} attached to it by a large vine overtaking the wall.")
	else:
		print(f"You walk a little farther west of the house and see a large vine overtaking the wall.")
	while ui != "Menu":
		ui = input(f"/// Inputs: 'East', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			FrontyardWest()
		elif ui == "East":
			Frontyard()
		elif ui == "Interact":
			ui = input(f"\t/// What do you interact with? ///\n").title()
			if ui == "Hose":
				if HoseVar == 0:
					if "Bobby Pins" in inventory:
						print(f"\nUsing your bobby pins you pick the padlock chaining the hose\n")
						print(f"+ Hose\n")
						inventory.append(f"Hose")
						CarObjevInven.remove(f"Hose")
						HoseVar = 1
					else:
						print(f"\nLooking at the hose you realize that it's chained to the wall, locked by a padlock.\n\tYou need some way of opening the lock.\n")
				else:
					print(f"\nSince you've already interacted with the hose, you can't again.\n")
			else:
				print(f"\nInput not recognized or not valid right now.\n")
		else:
			print(f"\nInput not recognized; try again.\n")
			FrontyardWest()

Player()
Bedroom()