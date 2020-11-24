class Pokemon:
    def __init__(self, name, HP, Damage, type):
        typeDict = {'fire': {'fire': 0.5, 'grass': 2.0, 'water':0.5}} #determines the type effectiveness for the attacking Pokemon
        self.name = name #sets the name of the Pokemon
        self.hp = HP #sets the hit points of the Pokemon
        self.Damage = Damage #sets the damage of the Pokemon (might not keep it)
        self.type = type #determines type effectiveness of attack