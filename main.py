import pickle, time, sys
#main file for text-based game

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
StartVar = 0

class Title():
#Class to print the game's title
	def __init__(self):
		print("""
   ____                                                                                                  
  / __ \__  __(_)  ____ ___  ______ ______(_)  ____ _____  ____ ______   _________  ____  ____ _____  / /_
 / / / / / / / /  / __ `/ / / / __ `/ ___/ /  / __ `/ __ \/ __ `/ ___/  / ___/ __ \/ __ \/ __ `/ __ \/ __/
/ /_/ / /_/ / /  / /_/ / /_/ / /_/ (__  / /  / /_/ / / / / /_/ (__  )  (__  / /_/ / / / / /_/ / / / / /__ 
\___\_\__,_/_/   \__, /\__,_/\__,_/____/_/   \__,_/_/ /_/\__,_/____/  /____/\____/_/ /_/\__,_/_/ /_/\__  ( )
                   /_/                                                                                   |/ 
""")
class Player():
#Class to determine player's name and initialize program/resume previous file
	def __init__(self):
		ui = ""
		ui = input(f"PROGRAM BEGUN. \nWould you like to 'Resume' a game or start a 'New' game?\n").title()
		if ui == "New":
			if StartVar == 0:
				self.name = input(f"\nGAME BEGUN.\nWhat is your name?\n").title()
				print(f"\n{self.name} begins a maybe-not-so-epic quest!\n\n\tREMEMBER: You may always access the Menu by inputting 'Menu'.")
				Title()
				print(f"---===---===---===---===---===---===---===---\n")
			else:
				print(f"\nGAME RESUMED. \nReturning to your maybe-not-so epic quest, your progress has been saved! You will renew in the master bedroom.\n\n\tREMEMBER: You may always access the Menu by inputting 'Menu'.")
				Title()
				print(f"---===---===---===---===---===---===---===---\n")
		elif ui == "Resume":
			filecheck()
			if StartVar == 0:
				print(f"\nNo previous game file found, starting new game.\n")
				self.name = input(f"GAME BEGUN.\nWhat is your name?\n").title()
				print(f"\n{self.name} begins a maybe-not-so-epic quest!\n\n\tREMEMBER: You may always access the Menu by inputting 'Menu'.")
				Title()
				print(f"---===---===---===---===---===---===---===---\n")
			else:
				load()
				print(f"\nGAME RESUMED. \nReturning to your maybe-not-so epic quest, your progress has been saved! You will renew in the master bedroom.\n\n\tREMEMBER: You may always access the Menu by inputting 'Menu'.")
				Title()
				print(f"---===---===---===---===---===---===---===---\n")
		else:
			print(f"\nInput not recognized; type either 'New' or 'Resume'.\n")
			Player()

class Menu(Player):
#Class that will be called multiple times to allow player many commands
	def __init__(self):
		ui = ""
		while ui != "R":
			print(f"\n---///---///---[ MENU ]---///---///---")
			ui = input(f"\nThis is the menu, here you may:\nI - View Inventory\nS - Save Game\nL - Load Game\nR - Return to Game\nQ - Quit Game\n\n  ---///---///---///---///---///---\n").title()
			if ui == "I":
				print(f"\nInventory: {inventory}")
			elif ui == "S":
				save()
				print(f"\nGame Saved!")
			elif ui == "L":
				print(f"\nLoading the game may overwrite unsaved progress; therefore, you may want to save before loading.")
				ui = ""
				ui = input("\tWould you like to 'load' game or 'return' to menu to save?\n").title()
				if ui == "Load":
					try:
						load()
						print(f"\nGame Loaded!")
					except FileNotFoundError:
						print(f"\nGame file not found!")
				elif ui == "Return":
					pass
				else:
					print(f"\nInput was not recognized, returning to menu.")
			elif ui == "R":
				print()
			elif ui == "Q":
				print(f"\nQuitting the game will NOT save; therefore, you may want to save before quitting.")
				ui = ""
				ui = input("\tWould you like to 'quit' game or 'return' to menu to save?\n").title()
				if ui == "Quit":
					print(f"\n\tThanks for playing, goodbye.\n")
					print(f"---===---===---===---===---===---===---===---\n")
					exit()
				elif ui == "Return":
					pass
				else:
					print(f"\nInput was not recognized, returning to menu.")
			else:
				print(f"\nInput not recognized; try again.")
				Menu()

class Car():
#Class for the primary game objective (fixing and leaving through car) and ending the game.
	def __init__(self):
		global CarVar
		ui = ""
		if CarObjevInven == []:
			typingPrint(f"\n ||| Now, with all the required car parts, you are able to successfully start the engine of your vehicle.\n\tDriving out of the garage you see an illuminated sign that indicates an upcoming offshoot. ||| \n")
			while ui != "Main":
				ui = typingInput(f"\n\t/// Do you take the 'main' path or the 'offshoot'? ///\n").title()
				if ui == "Main":
					typingPrint(f"\nDriving continuouly down the main path, you are able to leave the home's property a final time.\n\tHopefuly this world has intentions in your favor...\n\n ||| Thanks for playing! Goodbye. |||\n")
					typingPrint(f"---===---===---===---===---===---===---===---\n\n")
					quit()
				elif ui == "Offshoot":
					typingPrint(f"\nLeaving the main path, and taking the offshoot, you drive down an unpaved road until you see a small shack.\n\tUpon entering you see nothing but a large, metal door and a keypad taking numbers that correlate with letters h, g, f, e and d in that order.\n")
					while ui != "76776":
						ui = typingInput(f"/// What is the code? ///\n").title()
						if ui == "76776":
							typingPrint(f"\nThe metal door loudly opens revealing a single, white LED light.\n\tEntering the small room the door closes behind you and the room shakes downward.\n\t\tThe door opens again revealing an open earth cave.\n")
							typingPrint(f"\t\t\tNestled in the stalagmites you see a grand vault door and labeled above it a quote:\n\t\t\t\t\"Qui quasi anas sonant, sunt qui supersunt.\"\n")
							typingPrint(f"||| Thanks for playing! goodbye. |||\n")
							typingPrint(f"---===---===---===---===---===---===---===---\n\n")
							quit()
						elif ui == "Exit":
							typingPrint(f"\nFailing to know the code, you exit the shack and drive down the pathway.\n\tHopefuly this world has intenions in your favor...\n\n\t ||| Thanks for playing! Goodbye. |||\n")
							typingPrint(f"---===---===---===---===---===---===---===---\n\n")
							quit()
						else:
							typingPrint(f"\nThat was not the code, input 'Exit' to leave the shack.\n")
						
				else:
					typingPrint(f"\nInput not recognized or not valid right now. Input either 'Offshoot' or 'Main'.\n")
			quit()
		if CarVar == 0:
			typingPrint(f"\nYou get get into your somber excuse of a 'car' and start the engine.\n\tUpon starting it though the vehicle sputters into silence. Opening the hood you realize its cooling fan is gone;\n\t\tin fact, the hoses, exhaust, air filter, and lights are gone. You've been robbed.\n")
			typingPrint(f"\t/// Objective: Get {CarObjevInven} ///\n")
			CarVar = 1
		else:
			typingPrint(f"\n\t/// Objective: Get {CarObjevInven} ///\n")

def typingPrint(text):
#function to print words at a slower, more appealing speed
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0315) #0.0315
  
def typingInput(text):
#ditto of above function, but for input
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0315)
	value = input()
	return value

def Iti(word):
#function to italicize words (things that are interactable)
	italics = '\033[3m'
	end = '\033[0m'
	word = (italics + word + end)
	return word

def filecheck():
	#this function checks if a previous game file is loadable, aids Player() class
	try:
		load()
	except FileNotFoundError:
		pass

def save():
#of course, function to save all relevant variables to data.pkl
	with open("data.pkl", "wb") as f:
		pickle.dump(StartVar, f)
		pickle.dump(CarObjevInven, f)
		pickle.dump(inventory, f)
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
		pickle.dump(StickVar, f)
		pickle.dump(BladeVar, f)
		pickle.dump(FanVar, f)
		pickle.dump(UnitVar, f)
		pickle.dump(FanShellVar, f)
		pickle.dump(GooseVar, f)

def load():
	#of course, function to load all relevant variables from data.pkl
	global StartVar, CarObjevInven, inventory, BedroomVar, FrontyardVar, DresserVar, MirrorVar, ToolboxVar, CarVar, ChairVar, LightbulbVar, HoseVar, PipeVar, StickVar, BladeVar, FanVar, UnitVar, FanShellVar, GooseVar
	with open("data.pkl", "rb") as f:
		StartVar = pickle.load(f)
		CarObjevInven = pickle.load(f)
		inventory = pickle.load(f)
		BedroomVar = pickle.load(f)
		FrontyardVar= pickle.load(f)
		DresserVar = pickle.load(f)
		MirrorVar = pickle.load(f)
		ToolboxVar = pickle.load(f)
		CarVar = pickle.load(f)
		ChairVar = pickle.load(f)
		LightbulbVar = pickle.load(f)
		HoseVar = pickle.load(f)
		PipeVar = pickle.load(f)
		StickVar = pickle.load(f)
		BladeVar = pickle.load(f)
		FanVar = pickle.load(f)
		UnitVar = pickle.load(f)
		FanShellVar = pickle.load(f)
		GooseVar = pickle.load(f)

	return StartVar, CarObjevInven, inventory, BedroomVar, FrontyardVar, DresserVar, MirrorVar, ToolboxVar, CarVar, ChairVar, LightbulbVar, HoseVar, PipeVar, StickVar, BladeVar, FanVar, UnitVar, FanShellVar, GooseVar

###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---###---

def Bedroom():
#starting location, from here on are functions of in-game rooms/locations
	global BedroomVar
	global DresserVar
	dresser = Iti("dresser")
	ui = ""
	if BedroomVar == 0:
		typingPrint(f"Screams of the distance awaken you from your short lived slumber, and thus your stay here.\n\tYou sit up and out of the creaking bed, grab your rifle off the {dresser}, begin to head to the garage.\n")
	else:
		typingPrint(f"\nYou re-enter the master bedroom; not much is here besides a {dresser} and bedframe.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'East', 'West', 'South', 'Interact' ///\n").title()
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
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Dresser":
				if DresserVar == 0:
					typingPrint(f"\nYou open the dresser and find an old flashlight, but upon clicking it you find it has no batteries.\n")
					typingPrint(f"\n+ Flashlight!\n\n")
					inventory.append("Dead Flashlight")
					DresserVar = 1
					if "Batteries" in inventory:
						typingPrint(f"\nYou place your batteries from the toolbox into the flashlight; making them useful once more.\n")
						typingPrint(f"\n+ Charged Flashlight!\n- Dead Flashlight!\n- Batteries!\n")
						inventory.append(f"Charged Flashlight")
						inventory.remove(f"Dead Flashlight")
						inventory.remove(f"Batteries")
				else:
					typingPrint(f"\nYou open the dresser again and find nothing of interest.\n")
			else:
				typingPrint(f"\nInput either not recognized or not valid right now.\n\n")
				Bedroom()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Bedroom()

def Bathroom():
	ui = ""
	global MirrorVar
	mirror = Iti("mirror")
	typingPrint(f"\nYou enter the master bedroom's bathroom. In it, cracked {mirror} and stained walls.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'East', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Bathroom()
		elif ui == "East":
			Bedroom()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Mirror":
				if MirrorVar == 0:
					typingPrint(f"\nYou open the damaged mirror and pull out a few bobby pins.\n")
					typingPrint(f"\n+ Bobby Pins\n\n")
					inventory.append(f"Bobby Pins")
					MirrorVar = 1
				else:
					typingPrint(f"\nYou re-open the bathroom mirror but find only forgotten medicine bottles.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
				Bathroom()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Bathroom()

def KidsRoom():
	ui = ""
	global FanVar
	fan = Iti("fan")
	if FanVar == 0:
		typingPrint(f"\nSeeing strewn toys and clothing about; you must be in the room that was once for the children of this home.\n\tAbove a derelict cradle you see a small celing {fan}.\n")
	else:
		typingPrint(f"\nSeeing strewn toys and clothing about; you must be in the room that was once for the children of this home.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'North', 'East', 'South' 'Interact' ///\n").title()
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
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Fan":
				if FanVar == 0:
					typingPrint(f"\nYou rip the fan off the ceiling, dust and a cockroach fall to the floor.\n")
					typingPrint(f"\n+ Fan Blades\n")
					inventory.append(f"Fan Blades")
					FanVar = 1
					if "Fan Shell" in inventory:
						typingPrint(f"\nUsing the fan shell from the cellar, you are able to make a portable cooler.\n")
						typingPrint(f"\n+ Cooler\n")
						inventory.append(f"Cooler")
						inventory.remove(f"Fan Blades")
						inventory.remove(f"Fan Shell")
						CarObjevInven.remove(f"Cooling Fan")
					else:
						typingPrint(f"\nYou could use these fan blades for something if you had a shell to hold them in.\n\n")
				else:
					typingPrint(f"\nOne cannot simply interact with a ceiling fan that which has already been so.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
				KidsRoom()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			KidsRoom()

def Roof():
	ui = ""
	global UnitVar
	global GooseVar
	unit = Iti("unit")
	if GooseVar == 0:
		typingPrint(f"\nOpening the window, you step out onto the roof. From up here you can see a blazing, orange glow in the distance.\n\tAs you look at its fierce size, a herd of buffleheads fly overhead. To your right is an old air-conditioning {unit} that may still work.\n")
		GooseVar = 1
	elif UnitVar == 0:
		typingPrint(f"\nOpening the window, you step out onto the roof. From up here you can see a blazing, orange glow in the distance.\n\tTo your right is an old air-conditioning {unit} that may still work.\n")
	else:
		typingPrint(f"Opening the window, you step out onto the roof. From up here you can see a blazing, orange glow in the distance.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'North', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Roof()
		elif ui == "North":
			KidsRoom()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Unit":
				if UnitVar == 0:
					if "Shiv" in inventory:
						typingPrint(f"\nYou cut out the air-conditioning unit to use as a makeshift air filter.\n")
						typingPrint(f"\n+ Air Filter\n\n")
						inventory.append(f"Air Filter")
						CarObjevInven.remove(f"Air Filter")
						UnitVar = 1
					else:
						typingPrint(f"\nYou think that you could probaly put this cooler to good use if you could only extract it.\n\n")
				else:
					typingPrint(f"\nSince you've already extracted the AC, ya just can't 'gain.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
				Roof()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Roof()

def UpHall():
	ui = ""
	typingPrint(f"\nYou enter the hallway connecting two bedrooms and a staircase. You see a wanning crescent glisten through the dilapidated roof.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'West', 'Down' ///\n").title()
		if ui == "Menu":
			Menu()
			UpHall()
		elif ui == "West":
			Bedroom()
		elif ui == "Down":
			LivingRoom()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			UpHall()

def LivingRoom():
	ui = ""
	typingPrint(f"\nYour movement silently rocks a thin wooden chair in front of an old television set. The rug of this living room is moldy in wet.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'East', 'West', 'Up', 'Down' ///\n").title()
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
			typingPrint(f"\nInput not recognized; try again.\n")
			LivingRoom()

def DiningRoom():
	ui = ""
	typingPrint(f"\nA low light lamp lights the family table. China and cutlery are littered on the floor.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'North', 'East', 'South' ///\n").title()
		if ui == "Menu":
			Menu()
			DiningRoom()
		elif ui == "North":
			ui = typingInput(f"\nWould you like to enter the 'Kitchen' or 'Hallway'?\n").title()
			if ui == "Kitchen":
				Kitchen()
			elif ui == "Hallway":
				DownHall()
			else:
				typingPrint(f"\nInput not recognized; try again.\n")
		elif ui == "East":
			LivingRoom()
		elif ui == "South":
			Frontyard()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			DiningRoom()

def Kitchen():
	global LightbulbVar
	global ChairVar
	ui = ""
	lightbulb = Iti("lightbulb")
	chair = Iti("chair")
	if LightbulbVar == 1:
		typingPrint(f"\nWalking on the checkerboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.\n")
	elif ChairVar == 1:
		typingPrint(f"\nWalking on the checkerboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.\n\tThough you do see a flickering {lightbulb} above a now right-side up chair.\n")
	else:
		typingPrint(f"Walking on the checkerboard floor you see a disheveled, looted kitchen. Any trace of food is simply gone.\n\tThough you do see a flickering {lightbulb} above an overturned {chair}.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'East', 'South', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Kitchen()
		elif ui == "East":
			DownHall()
		elif ui == "South":
			DiningRoom()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Lightbulb":
				if LightbulbVar == 0:
					if ChairVar == 0:
						typingPrint(f"\nYou attempt to unscrew the lightbulb on the ceiling, but just can't reach it.\n")
					else:
						typingPrint(f"\nStanding on the chair, you unscrew the lightbulb and stash it.\n")
						typingPrint(f"\n+ Light Bulb\n\n")
						inventory.append(f"Light Bulb")
						CarObjevInven.remove(f"Light Bulb")
						LightbulbVar = 1
				else:
					typingPrint(f"\nHaving already removed the light bulb, you can no longer interact with it.\n")
			elif ui == "Chair":
				if ChairVar == 0:
					typingPrint(f"\nYou turn the kitchen chair on the floor right-side up.\n")
					ChairVar = 1
				else:
					typingPrint(f"\nHaving already turned up the chair, you can no longer interact with it.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
				Kitchen()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Kitchen()

def DownHall():
	global BladeVar
	ui = ""
	blade = Iti(f"blade")
	if BladeVar == 0:
		typingPrint(f"\nYou pass by frames of photos of bygone children; through the home's backdoor you see the moon-lit yard.\n\tOn the ground you see some sort of {blade}.\n")
	else:
		typingPrint(f"\nYou pass by frames of photos of bygone children; through the home's backdoor you see the moon-lit yard.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'North', 'West', 'South', 'Interact' ///\n").title()
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
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Blade":
				if BladeVar == 0:
					typingPrint(f"\nYou carefully pick up the gray, shining blade from the floor.\n")
					typingPrint(f"\n+ Blade\n\n")
					inventory.append(f"Blade")
					BladeVar = 1
					if "Stick" in inventory:
						typingPrint(f"Now; with your stick from earlier, you craft a shiv.")
						typingPrint(f"\n\n+ Shiv\n\n- Blade\n\n- Stick\n\n")
						inventory.append(f"Shiv")
						inventory.remove(f"Blade")
						inventory.remove(f"Stick")
				else:
					typingPrint(f"\nHaving already picked up the blade, you cannot again.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
				DownHall()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			DownHall()

def Garage():
	ui = ""
	global ToolboxVar
	toolbox = Iti("toolbox")
	typingPrint(f"\nPerhaps the only room that appears like its pre-war self; the garage is where your nearly handmade 'car'\n\tis dimly light as well as a {toolbox} by a single bulb.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'West', 'Interact', 'Car' ///\n").title()
		if ui == "Menu":
			Menu()
			Garage()
		elif ui == "West":
			LivingRoom()
		elif ui == "Car":
			Car()
			Garage()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Car":
				Car()
				Garage()
			elif ui == "Toolbox":
				if ToolboxVar == 0:
					typingPrint(f"\nYou open the rusty red toolbox and find two old batteries.\n")
					typingPrint(f"\n+ Batteries\n\n")
					inventory.append(f"Batteries")
					ToolboxVar = 1
					if "Dead Flashlight" in inventory:
						typingPrint(f"With your new found batteries, you recharge the old flashlight making it useful once more.")
						typingPrint(f"\n\n+ Charged Flashlight\n\n- Dead Flashlight\n\n- Batteries\n\n")
						inventory.append(f"Charged Flashlight")
						inventory.remove(f"Dead Flashlight")
						inventory.remove(f"Batteries")
				else:
					typingPrint(f"\nYou open the damaged red toolbox again but find nothing of interest.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
				Garage()

		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Garage()

def Cellar():
	global FanShellVar
	ui = ""
	crates = Iti("crates")
	typingPrint(f"\nYou walk down into the cellar; all is silent but the cyclic dripping from somewhere.\n\tThere are a few {crates} that look un-opened.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'East', 'Up', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			Cellar()
		elif ui == "East":
			DeepCellar()
		elif ui == "Up":
			LivingRoom()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Crates":
				if FanShellVar == 0:
					typingPrint(f"\nOpening the crates, you unfortunately don't see much of importance but a fan shell with no blades.\n")
					typingPrint(f"\n+ Fan Shell\n\n")
					inventory.append(f"Fan Shell")
					FanShellVar = 1
					if "Fan Blades" in inventory:
						typingPrint(f"Using your fan blades you pulled from the kids' room, you are able to make a portable cooler.\n")
						typingPrint(f"\n+ Cooler\n\n")
						inventory.append(f"Cooler")
						inventory.remove(f"Fan Blades")
						inventory.remove(f"Fan Shell")
						CarObjevInven.remove(f"Cooling Fan")
				else:
					typingPrint(f"\nOpening the crates again, you don't see much of importance.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Cellar()

def DeepCellar():
	global PipeVar
	ui = ""
	pipe = Iti("pipe")
	if "Charged Flashlight" in inventory:
		if PipeVar == 0:
			typingPrint(f"\nNow able to see with your flashlight, you can see the source of the dripping sound: a leaky {pipe}.\n\tThere's also overgrown cobwebs, and long-forgotten boxes.\n")
		else:
			typingPrint(f"\nHere in the deep cellar, you see the remains of the leaky pipe you cut, some cobwebs, and old boxes.\n")
		while ui != "Menu":
			ui = typingInput(f"/// Inputs: 'West', 'Interact' ///\n").title()
			if ui == "Menu":
				Menu()
				DeepCellar()
			elif ui == "West":
				Cellar()
			elif ui == "Interact":
				ui = typingInput(f"\t/// What do you interact with? ///\n").title()
				if ui == "Pipe":
					if PipeVar == 0:
						if "Shiv" in inventory:
							typingPrint(f"\nWith your shiv, you cut off a piece of the small pipe for your car.\n")
							typingPrint(f"\n+ Pipe\n\n")
							inventory.append(f"Pipe")
							CarObjevInven.remove(f"Exhaust Pipe")
							PipeVar = 1
						else:
							typingPrint(f"\nLooking at the pipe, you realize it's the perfect size for your car, but you need something strong to remove it.\n")
					else:
						typingPrint(f"\nYou can't interact with the pipe again, as it is gone. :(\n")
				else:
					typingPrint(f"\nInput either not recognized or not valid right now.\n")
			else:
				typingPrint(f"\nInput not recognized; try again.\n")
				DeepCellar()
	else:
		typingPrint(f"\nThis part of the cellar is so far from the staircase that visibility is naught, you need some sort of tool to aid your eyes to proceed.\n")
		typingPrint(f"\tReturning west to the lit part of the cellar.\n")
		Cellar()

def Backyard():
	ui= ""
	typingPrint(f"\nExiting the house you feel the early morning dew brush against your boots.\n\tThere's a small table with a chessboard but no chairs; there are only black pawns on squares h7, g6, f7, e7, and d6.\n\t\tWhen you try to move the pieces they solidly stay put.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'South' ///\n").title()
		if ui == "Menu":
			Menu()
			Backyard()
		elif ui == "South":
			DownHall()
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			Backyard()

def Frontyard():
	global FrontyardVar
	ui = ""
	if FrontyardVar == 0:
		typingPrint(f"\nAs you open the front door, leaving the home, a faraway explosion is heard followed by more screams.\n\tYou should leave soon.\n")
	else:
		typingPrint(f"\nYou walk by the gray picket fences in front of the house.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'North', 'East', 'West' ///\n").title()
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
			typingPrint(f"\nInput not recognized; try again.\n")
			Frontyard()

def FrontyardEast():
	global StickVar
	ui = ""
	sticks = Iti(f"sticks")
	if StickVar == 0:
		typingPrint(f"\nYou walk farther east from the house, not much is here but a pile of {sticks} and a lone red baneberry.\n")
	else:
		typingPrint(f"\nYou walk farther east from the house, not much is here but a lonesome red baneberry.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'West', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			FrontyardEast()
		elif ui == "West":
			Frontyard()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Sticks":
				if StickVar == 0:
					typingPrint(f"\nYou pick up a stick.\n")
					typingPrint(f"\n+ Stick\n\n")
					inventory.append(f"Stick")
					StickVar = 1
					if "Blade" in inventory:
						typingPrint(f"Now; with your blade from earlier, you craft a shiv.")
						typingPrint(f"\n\n+ Shiv\n\n- Stick\n\n- Blade\n\n")
						inventory.append(f"Shiv")
						inventory.remove(f"Blade")
						inventory.remove(f"Stick")
				else:
					typingPrint(f"\nHaving already picked up a stick, there is no longer one to.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			FrontyardEast()

def FrontyardWest():
	ui = ""
	global HoseVar
	hose = Iti(f"hose")
	if HoseVar == 0:
		typingPrint(f"\nYou walk a little farther west of the house and see a dark green garden {hose} attached to it by a large vine overtaking the wall.\n")
	else:
		typingPrint(f"\nYou walk a little farther west of the house and see a large vine overtaking the wall.\n")
	while ui != "Menu":
		ui = typingInput(f"/// Inputs: 'East', 'Interact' ///\n").title()
		if ui == "Menu":
			Menu()
			FrontyardWest()
		elif ui == "East":
			Frontyard()
		elif ui == "Interact":
			ui = typingInput(f"\t/// What do you interact with? ///\n").title()
			if ui == "Hose":
				if HoseVar == 0:
					if "Bobby Pins" in inventory:
						typingPrint(f"\nUsing your bobby pins you pick the padlock chaining the hose.\n")
						typingPrint(f"\n+ Hose\n\n")
						inventory.append(f"Hose")
						CarObjevInven.remove(f"Hose")
						HoseVar = 1
					else:
						typingPrint(f"\nLooking at the hose you realize that it's chained to the wall, locked by a padlock.\n\tYou need some way of opening the lock.\n")
				else:
					typingPrint(f"\nSince you've already interacted with the hose, you can't again.\n")
			else:
				typingPrint(f"\nInput not recognized or not valid right now.\n")
		else:
			typingPrint(f"\nInput not recognized; try again.\n")
			FrontyardWest()
Player()
StartVar = 1
Bedroom()