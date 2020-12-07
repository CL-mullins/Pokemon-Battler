class Items:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount #What the item does when activated
        #conditions that activate the item?

    def heal(self, amount):
        #item heals a certain amount of health to the respective Pokemon
        self.current_HP += amount
        pass
    def status_remove(self, status):
        pass
        #check if Pokemon has status, if it has status, remove the status
        #if self.hasStatus == True:
         #   pass
        #else:
         #   pass
   # def stat_increase(self, value):
    #    pass

#Initialize a potion:
#potion = Items('Potion', self.heal() [or, self.hp + 20]