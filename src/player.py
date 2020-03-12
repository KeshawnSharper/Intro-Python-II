# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self,name,currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    def introduce_self(self):
        print(f"my name is {self.name} and I am in the {self.currentRoom} room")
    def not_allowed(self):
        print("Not allowed please try again ")
# p1 = Player("Larry","Shade Room")
# p1.introduce_self()
