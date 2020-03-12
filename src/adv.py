from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
p2 = Player("Harry","outside")
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

answered = False 
def move(choice):
    if p2.currentRoom == "outside" and choice == "n" and answered == False:
        p2.currentRoom = "foyer"
        
        
    elif p2.currentRoom == "outside" and choice != "n" and answered == False:
        value = input("Not allowed please try again")
        
        
    elif p2.currentRoom == "foyer" and choice == "n" :
        p2.currentRoom = "overlook"
        
        
    elif p2.currentRoom == "foyer" and choice == "s" :
        p2.currentRoom = "outside"
        
       
        
    elif p2.currentRoom == "foyer" and choice == "e" :
        p2.currentRoom = "narrow"
        
    elif p2.currentRoom == "overlook" and choice == "s" :
        p2.currentRoom = "foyer"
        
    elif p2.currentRoom == "narrow" and choice == "w" :
        p2.currentRoom = "foyer"

    elif p2.currentRoom == "narrow" and choice == "s" :
        p2.currentRoom = "treasure"   

    else:
        print("not valid please try again")
    
value = input("please enter a direction or enter 'q' to quit")
while value != "q":
    move(value)
    p2.introduce_self()
    
    value = input("select another direction or 'q' to quit")
    
    

    
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
