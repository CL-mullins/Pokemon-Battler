class Items:
    def __init__(self, name, amount,):
        self.name = name
        self.effect = effect #What the item does when activated
        #conditions that activate the item?

    def heal(self, amount):
        #item heals a certain amount of health to the respective Pokemon
        pass
    def status_remove(self, status):
        pass
    def stat_increase(self, value):

#Initialize a potion:
# potion = Items('Potion', self.heal() [or, self.hp + 20])