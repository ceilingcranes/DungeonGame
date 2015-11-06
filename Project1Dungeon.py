"""
Author: Maxine Hartnett
Date: 9/2/15
A text based dungeon game. 
"""


class Room(object): 
	n=""
	s=""
	e=""
	w=""
	secondary_descr=False
	
	
	def __init__(self, room_name, room_description): #will set the string name of the room, and the description.
		self.inst_name=room_name
		self.room_desc=room_description

	def intro(self): #will get called the first time someone enters the room
		print("\n You are in the {}. There are rooms to the: {}".format(self.inst_name, self.adj_room()))
		print(self.room_desc)
		
	def descrip(self): # will print only the description, not the exits. For the trap.
		print(self.room_desc)
		
	def adj_room(self): #will concatinate a str of all the adjacent rooms, to use in intro method
		str_n=""
		str_s=""
		str_e=""
		str_w=""
		if self.n!="":
			str_n= "north (n) "
		if self.s!="":
			str_s="south (s) "
		if self.e!="":
			str_e="east (e) "
		if self.w!="":
			str_w="west (w) "
		return str_n+ str_s+str_e+str_w
		
	def set_room(self, next_dir): #will set curr_room to the adj room designated by next_dir
		temp=self
		next_room=self
		if next_dir=="n":
			next_room=self.n
		elif next_dir=="w":
			next_room=self.w
		elif next_dir=="s":
			next_room=self.s
		elif next_dir=="e":
			next_room=self.e

		if isinstance(next_room, str): # if there isn't anything to the dir, set the room back to the current room
			next_room=self
		return next_room

class SecondaryRoom(Room):  # still have to figure out a way to actually do the options
	def __init__(self, room_name, room_description): #will set the string name of the room, and the description.
		self.inst_name=room_name
		self.room_desc=room_description
		
	def intro(self): #will get called the first time someone enters the room
		print("\n You are in the {}. There are rooms to the: {}".format(self.inst_name, self.adj_room()))
		print(self.room_desc)
		
	def trapIntro(self): #special case for the trap so it doesn't print the way out	
		print("\n"+self.room_desc)
	"""
	These three functions will set the options for the secondary room. The first is for the list of things people
	can do inside the room. The second is what will print when/if they select that choice. The third is the room that 
	they will go to if they don't go anywhere. "q" is for quit, if they die. Any number but n s e w will default
	to the current room: Here I use "".
	"""
	def setOptOne(self, opt, doOpt, nextDir): 
		self.opt1=opt
		self.doOpt1=doOpt
		self.dir1=nextDir
		
	def setOptTwo(self, opt, doOpt, nextDir):
		self.opt2=opt
		self.doOpt2=doOpt
		self.dir2=nextDir
		
	def setOptThree(self, opt, doOpt, nextDir):
		self.opt3=opt
		self.doOpt3=doOpt
		self.dir3=nextDir
		
		
	def stateOptions(self): # to print out the options
		print("You can: {} (1), {} (2), or {} (3).".format(self.opt1, self.opt2, self.opt3))
		
	def doOption(self, opt): #When they select an option
		chosenO=opt
		next_room=""
		if int(opt) == 1:
			chosenO=self.doOpt1
			next_room=self.dir1
		elif int(opt) == 2:
			chosenO=self.doOpt2
			next_room=self.dir2
		else:
			chosenO=self.doOpt3
			next_room=self.dir3
		
		print("\n"+chosenO) #print out the response
		return next_room #return the next dir
		
			
def main():
	#To add more rooms: create the instance below. Then go and add it to the 'map' and decide which rooms to connect it to below.
	living_room=Room("living room", "The living room is full of ornate furniture. There is a huge lamp burning in the corner.")
	kitchen=Room("kitchen", "The pots and pans on the wall gleam with the light from the fire. The room is full of \
the scent of savory meat.")
	hallway=Room("hallway", "The carpet here is extremely ugly.")
	furnace=Room("furnace", "furnace")
	library=SecondaryRoom("library", "The towering stacks of books lean towards each other. The whole room has a faint sense of mystery and magic.")
	fork=Room("fork", "Both directions vanish into the distance. A really ugly painting of a dog is on the wall. Like, really \
ugly. Gross.")
	trap=SecondaryRoom("trap", "The door slams shut behind you! You are trapped, probably doomed to starve.")
	bedroom=Room("bedroom", "A huge four-poster bed just begs for you to jump on it.")
	closet=SecondaryRoom("closet", "A vaguely musty scent drifts from the many fancy clothes hanging in the closet. A shelf to your left is \
full of really uncomfortable-looking shoes.")
	reading_room=Room("reading room", "The room is warm from a fire burning in a marble mantle. Unlike the living room, the funiture \
here looks comfortable and well-used.")

	#setting all the directions
	kitchen.e=living_room
	living_room.w=kitchen
	kitchen.s=furnace
	kitchen.w=hallway
	hallway.e=kitchen
	hallway.s=library
	library.n=hallway
	hallway.n=fork
	fork.s=hallway
	fork.w=trap
	trap.e=fork
	fork.e=bedroom
	bedroom.w=fork
	bedroom.n=closet
	closet.s=bedroom
	trap.w=kitchen
	living_room.e=reading_room
	reading_room.w=living_room

	win=False
	dead=False
	curr_room=living_room #the room currently in
	user_input=""
	
	#To set the secondary room options:
	
	trap.setOptThree("go to the window", "Far below, waves crash onto the rocks. The window looks like it can open. \
When you look through the glass, you can see a fire escape! Unfortunately, when \n you attempt to climb onto it, you fall to your death. :(", "q" )
	trap.setOptTwo("go to the mirror", "The mirror is full sized. When you try and pull it off the wall, it swings open, revealing a \
secret passageway.", "w")
	trap.setOptOne("go to the chair.", "The chair is ornate. When you turn it upside down the legs fall off. Good thing \
you didn't try to sit!", "")

	closet.setOptOne("try on shoes",  "Ouch! These shoes are way too small.",  "")
	closet.setOptTwo("try on a dress", "That dress looks wonderful on you.", "")
	closet.setOptThree("look in the trunk", "Gleaming treasure winks at you from the darkness of the closet. No \
princess here!", "")

	library.setOptOne("investigate picture", "Congratuations! You found the princess studying python under the \
painting!", "q")
	library.setOptTwo("check in the closet", "The closet is dark and probably full of spiders. No way the princess is here.", "")
	library.setOptThree("look by the bookshelf",  "The bookshelf contains lots of dusty tomes and cobwebs. No princess has \
touched these books anytime recently.", "")

	while(user_input!="s"):
		user_input=input("Welcome to Maxine's dungeon game! The goal is to find the princess by exploring the castle. To see a list of \
instructions, press 'i' and hit enter. Otherwise, hit 's' to start the game.")

		if user_input=="i":
			print("\n Your goal is to find the princess! To make a selection, type the letter for the option you want and hit enter. \
Press 'q' if you want to quit. Good luck!")
	
	

	while(user_input != "q"): #where all the actual gameplay will go
		if curr_room!=trap:
			curr_room.intro()
		else:
			curr_room.trapIntro()
		if isinstance(curr_room, SecondaryRoom): #if the current room has multipule choices
			curr_room.stateOptions()
			
		user_input=input("What do you want to do?")
		
		if user_input.isdigit()==True:
			running=True
			while(((int(user_input)) not in [1,2,3] )and running==True):
				user_input=input("What do you want to do? running.")
				if not user_input.isDigit():
					running=false
			temp=user_input
			user_input=curr_room.doOption(temp)
			if(user_input!="q"):
				curr_room=curr_room.set_room(user_input)
		else:
			curr_room=curr_room.set_room(user_input)
			#special cases:
		if curr_room==furnace: 
			print("You were burned to a crisp in the furnace! RIP")
			user_input="q"
		"""
		if curr_room==library:
			while(user_input != "n"):
				user_input=input("You look, and see a picture (p), a bookshelf (b), and a closet (c)")
				if user_input=="p":
					print("\n Congratulations! You found the princess studying python in front of the painting!")
					user_input="n"
					win=True
				if user_input=="b":
					print("\n The bookshelf contains lots of dusty tomes and cobwebs. No princess has touched these books anytime recently.")
				if user_input=="c":
					print("\n The closet is dark and probably full of spiders. No way the princess is here.")
		if win==True:
			user_input="q"
			
			
		if curr_room==closet:
			while user_input!="b":
				user_input=input("Would you like to try on some clothes? Type 'd' to try a dress, type 's' to try shoes, and press 'b' \
to go back.")
				if user_input=="d":
					print("You look wonderful in that dress.")
				if user_input=="s":
					print("Ouch! Those shoes are too small.")
				"""

main()
