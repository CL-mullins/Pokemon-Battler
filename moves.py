class Moves:
    typeChart = {'fire': 
        {'fire': 0.5, 'grass': 2.0, 'water':0.5},
        'grass':{'fire':0.5,'grass': 0.5, 'water':2.0},
        'water': {'fire':2.0, 'grass': 0.5, 'water': 0.5}}
    def __init__(self, name, type, damage,):
        self.name = name #Name of the move
        self.type = type #name of the type
        self.damage = damage #unaltered damage amount
        #potentially want to add status effects
