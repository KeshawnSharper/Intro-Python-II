from room import Room
from player import Player
from item import Item


# Declare all the rooms
key = Item("Key","Unlocks the door")
sword = Item("Sword","Kills the monster")
chest = Item("Treasure","Win the game")

outside =  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[])
p2 = Player("Harry",outside,[])


answered = False 

def move(choice):
    monster = True 
    if p2.currentRoom == outside and choice == "n":
        p2.currentRoom = foyer

    elif p2.currentRoom == outside and choice == "i" :
        p2.add_item(key)
    elif p2.currentRoom == overlook and choice == "i" :
        p2.add_item(sword)
    elif p2.currentRoom == treasure and monster == False and choice == "i" :
        p2.add_item(chest)
   
    elif p2.currentRoom == narrow and choice == "a" and sword in p2.items:
        monster = False
    elif p2.currentRoom == outside and choice != "n" and answered == False:
        value = input("Not allowed please try again")
        
        
    elif p2.currentRoom == foyer and choice == "n" :
        p2.currentRoom = overlook
        
        
    elif p2.currentRoom == foyer and choice == "s" :
        p2.currentRoom = outside
        
        
    elif p2.currentRoom == foyer and choice == "e" :
        p2.currentRoom = narrow
        
    elif p2.currentRoom == overlook and choice == "s" :
        p2.currentRoom = foyer
        
    elif p2.currentRoom == narrow and choice == "w" :
        p2.currentRoom = foyer
    elif p2.currentRoom == narrow and choice == "s" and monster == True :
        value = "q"
    elif p2.currentRoom == narrow and choice == "s" and monster== False :
        p2.currentRoom = treasure   

    else:
        print("not valid please try again")
    
value = input("please enter a direction or enter 'q' to quit")
while value != "q":
    move(value)
    p2.introduce_self()
    
    value = input("select another direction or 'q' to quit")
 
