from items import Items
from character import Character

class store:
    #Purchase items for character here
    def __init__(self, name):
        self.name = name
        self.potions = Items('Potion', 20)

    def purchase(self, obj):
        #chatbot for purchasing items
        self.addItem(obj)
        