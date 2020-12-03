class Moves:
    typeChart = {'fire': 
        {'fire': 0.5, 'grass': 2.0, 'water':0.5},
        'grass':{'fire':0.5,'grass': 0.5, 'water':2.0},
        'water': {'fire':2.0, 'grass': 0.5, 'water': 0.5}}
    def __init__(self, name, type, damage,):
        self.name = name #Name of the move
        self.type = type #name of the type
        self.damage = damage #unaltered damage amount
        
    def calculate_damage(self, move_type, damage_amount):
        #This calculates the damage done based on pokemon type
        typeChart = {'fire': 
        {'fire': 0.5, 'grass': 2.0, 'water':0.5},
        'grass':{'fire':0.5,'grass': 0.5, 'water':2.0},
        'water': {'fire':2.0, 'grass': 0.5, 'water': 0.5}}

        conversion_dict = typeChart[self.type]
        #first value in dictionary
        #how does self.poketype access the Pokemon's type
        damage = damage_amount * conversion_dict[move_type]
        return damage