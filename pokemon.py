from moves import Moves

#Pokemon object that can battle
class Pokemon(object):
    typeChart = {'fire': 
        {'fire': 0.5, 'grass': 2.0, 'water':0.5},
        'grass':{'fire':0.5,'grass': 0.5, 'water':2.0},
        'water': {'fire':2.0, 'grass': 0.5, 'water': 0.5}}
         #determines the type effectiveness for the attacking Pokemon
    def __init__(self, name, HP, Damage, type): 
        self.name = name #sets the name of the Pokemon
        self.hp = HP #sets the max hit points of the Pokemon
        self.current_HP = HP #sets current HP of Pokemon
        self.Damage = Damage #sets the damage of the Pokemon (might not keep it)
        self.type = type #determines type effectiveness of attack
        self.moves = list()

    def attack(self, opponent):
        total_damage = 0
        #calculate attack damage by taking the moves' damage, then check the type between
        #the moves' type and the opponents type.
        #take that value and multiply the attack damage by it to get attack damage
        attackDamage = self.damage * (typeChart[self.type][Opponent.type])
        #how do I access the opponent.type
        return attackDamage

    def take_damage(self, damage):
        #Updates self.current_HP to reflect damage taken
        self.current_HP -= damage

    def isAlive(self):
        #Checks to see is the Pokemon has or has not fainted
        if self.current_HP <= 0:
            return False
        else:
            return True

    def add_move(self, move):
        self.moves.append(move)

    #Is it an object of the Pokemon class or move class?
    #Pokemon can attack, moves cant
    #How do I utilize the move class within Pokemon class

    def battle(self, opponent):
        #Pick which move you want to use
        #I want to do something similar to the superhero dueler, so I'll have the 
        #terminal print out all (4) moves and have the user enter a number to use it!
        while(self.isAlive() and opponent.isAlive()):
        select_move = input(f"Select your move: \n  
        [1]{self.moves[1]} , 
        [2]{self.moves[2]} , 
        [3]{self.moves[3]} 
        [4]{self.moves[4]} ")
        if select_move = "1":
            #choose the move and attack the opponent with the move
        #ability.attack self.opponent?
        #Whats different about this than the superhero dueler
        #is that im not using every move, instead, the Pokemon 
        #can only attack with one move per turn
        #so it would have to be something like move.attack()
            #TODO:where would the target go
            #TODO:how would the specfic move be passed in?
        if select_move = "2":
            #choose the move and attack the opponent with the move
        if select_move = "3":
            #choose the move and attack the opponent with the move
        if select_move = "4":
            #choose the move and attack the opponent with the move



    #def take_damage(sef):



squirtle = Pokemon('Squirtle', 100, 5, 'water')

    #I want an add attack method that also uses the type dictionary
    #Also stats, I have two weeks. I want there to be a window with Sprites as well