# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self,name,description,items):
        self.name = name
        self.description = description
        self.items = items
    def introduce_self(self):
        print(f"I am in the {self.name} with the {self.description}")
# p1 = Room("Shade Room","Blue Lights")
# p1.introduce_self()