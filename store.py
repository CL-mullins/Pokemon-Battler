from items import Items
from character import Character

class store:
    #Purchase items for character here
    #Give store a name (class attribute)
    def __init__(self, name):
        self.name = name
        self.potions = Items('Potion', 20)
        self.megaPotion = Items('Potion', 50)

    def purchase(self, obj):
        #chatbot for purchasing items
        #character -= amount
        self.addItem(obj)
        