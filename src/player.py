# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self,name,currentRoom,items):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
    def introduce_self(self):
        print(f"my name is {self.name} and I am in the {self.currentRoom.name} room")
    def not_allowed(self):
        print("Not allowed please try again ")
    def change_room(self, room):
        self.currentRoom = room
    def add_item(self,item):
        self.items.append(item)
        for x in self.items:
            print(x.name)

# p1 = Player("Larry","Shade Room")
# p1.introduce_self()
