class Item:
    def __init__(self,name,description):
        self.name = name
        self.description = description
    def introduce_self(self):
        print(f"my name is {self.name} and I am in the {self.currentRoom} room")
    def not_allowed(self):
        print("Not allowed please try again ")
# p1 = Player("Larry","Shade Room")
# p1.introduce_self()