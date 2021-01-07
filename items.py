#def heal(amount):
 #   self.current_HP += amount
  #  pass
#The function would need to be within the Pokemon class?

class Items:
    def __init__(self, name, amount):
        self.name = name
        #self.effect = effect #Pass a function from one of the item's methods that is used
        self.amount = amount #If effect is of a specific type, it'll restore or add a specified amount
         #What the item does when activated
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

