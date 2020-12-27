from moves import Moves
from moves import *
from character import Character
from items import Items
import random
import pandas as pd

#Pokemon object that can battle
class Pokemon(Character):

         #determines the type effectiveness for the attacking Pokemon
    def __init__(self, name, HP, type1, attack, defense, spAttack, spDefense, speed, level): 
        self.name = name #sets the name of the Pokemon
        self.hp = HP #sets the max hit points of the Pokemon
        self.current_HP = HP #sets current HP of Pokemon
        #self.Damage = Damage #sets the damage of the Pokemon (might not keep it)
        self.type1 = type1 #determines type effectiveness of attack
        self.baseAttack = attack #determines base attack value
        self.currentAttack = self.baseAttack #sets current attack value @ level 1
        self.baseDefense = defense #determines base defense value
        self.currentDefense = self.baseDefense
        self.baseSpAttack = spAttack #determines
        self.currentSpAttack = self.baseSpAttack
        self.baseSpDefense = spDefense #determines
        self.currentSpDefense = self.baseSpDefense
        self.baseSpeed = speed #determines attack order
        self.currentSpeed = self.baseSpeed
        self.moves = list() #holds all moves, maximum, 4 moves
        self.bag = list() #holds all items, maximum, 1 item
        self.level = level #holds level value, max level: 100
        self.exp = 0 #holds current exp
        self.maxEXP = 100 #exp requirement to level up
        self.rewardEXP = 9
        self.expMultiplier = 1
        #considering a rewardEXP property that scales by level
        #Example: a level 1 charmander's reward EXP is 9

    def attack(self, opponent):
        total_damage = 0
        #calculate attack damage by taking the moves' damage, then check the type between
        #the moves' type and the opponents type.
        #take that value and multiply the attack damage by it to get attack damage
        attackDamage = self.damage * (typeChart[self.type][opponent.type])
        #how do I access the opponent.type
        return attackDamage

    def take_damage(self, damage):
        #Updates self.current_HP to reflect damage taken
        #Pass in value from calculate damage
        self.current_HP -= damage

    def __calculate_damage(self, move_type, damage_amount, opponent_type):
        #This calculates the damage done based on pokemon type
        #Ex. typeChart =  {move_type: {opponent_type: damage outcome}}
        typeChart = {'Fire': {'Fire': 0.5, 'Grass': 2.0, 'Water':0.5, 'Normal': 1},'Grass':{'Fire':0.5,'Grass': 0.5, 'Water':2.0, 'Normal': 1},'Water': {'Fire':2.0, 'Grass': 0.5, 'Water': 0.5, 'Normal': 1},'Normal': {'Fire': 1, 'Grass': 1, 'Water': 1, 'Normal': 1}}
        conversion_dict = typeChart[move_type]

        #first value in dictionary
        damage = damage_amount * conversion_dict[opponent_type]
        return damage

    def isAlive(self):
        #Checks to see is the Pokemon has or has not fainted
        if self.current_HP <= 0:
            return False
        else:
            return True

    def add_move(self, move):
        #Adds a move to the Pokemon
        self.moves.append(move)

    def give_item(self, item):
        #Gives the Pokemon an item to 'hold'
        self.bag.append(item)

    def __addEXP(self, amount):
        #adds the EXP to the selected Pokemon [post battle]
        #private because all EXP functions should not be called outside of class
        self.exp += amount

    def __levelUp(self):
        #private because all EXP functions should not be called outside of class
        #Levels up the Pokemon

        if self.exp == self.maxEXP or self.exp > self.maxEXP:
            self.level = self.level + 1
            self.maxEXP = self.maxEXP + 50
            #reward EXP multiplier += 1
            #Upon leveling, a Pokemon's stats will increase
            #for each level, the Pokemon's stat will increase for 1/50th the base value
            # ~and combined individual & effort value~ 
            self.currentAttack = self.currentAttack + (self.baseAttack * 0.02)
            self.currentDefense = self.currentDefense + (self.baseDefense * 0.02)
            self.currentSpAttack = self.currentSpAttack + (self.baseSpAttack * 0.02)
            self.currentSpDefense = self.currentSpDefense + (self.baseSpDefense * 0.02)
            self.currentSpeed = self.currentSpeed + (self.baseSpeed * 0.02)
            print(f'{self.name} leveled up!')
        else:
            pass

    def __calculateEXP(self):
        #calculates the amount of EXP the pokemon will award upon defeat
        #Private because EXP does not need to be altered outside of class
        self.rewardEXP = int(self.rewardEXP) * int(self.expMultiplier)
        return int(self.rewardEXP)

    def addItem(self, item):
        self.bag.append(item)

    def requestNickname(self):
        #Asks user for a name 
        #returns name
        #overridden from character
        nickname = input('Enter Pokemon nickname: ')
        return nickname


    def giveNickname(self, name):
        #re-declares name value and gives Pokemon (or character) new name
        #overridden from character
        self.name = name

    def heal(self, amount):
        #actually applies the healing
        self.current_HP += amount

    def useItem(self, item):
        #If the item is a restorative item
        if item.name == 'Potion' or 'Super Potion' or 'Hyper Potion' or 'Max Potion' or 'Full Restore':
            #Heal the Pokemon for a specified amount
            self.heal(item.amount)
        else: 
            pass
        
 

    def battle(self, opponent):
        #Pick which move you want to use
        while(self.isAlive() and opponent.isAlive()):
            select_action = input(f"What will {self.name} do?: \n \n[1]Attack [2]Bag \n [3]Pokemon [4]Run\n :")
            if select_action == "1":
                #Attack Menu
                select_move = input(f"Select your move: \n \n[1]{self.moves[0].name} [2]{self.moves[1].name} \n[3]{self.moves[2].name} [4]{self.moves[3].name}\n Enter:  ")
                #Each move attacks and does damage
                if select_move == "1":
                    print(f'{self.name} used {self.moves[0].name}!')
                    #Print out effectiveness
                    print(f'{self.name} did {self.__calculate_damage(self.moves[0].type, self.moves[0].damage, opponent.type1)} damage!')
                    opponentDamage = self.__calculate_damage(self.moves[0].type, self.moves[0].damage, opponent.type1)
                    opponent.take_damage(opponentDamage)
                    print(f'{opponent.name} remaining HP: {opponent.current_HP}')
                    #choose the move and attack the opponent with the move
                if select_move == "2":
                    print(f'{self.name} used {self.moves[1].name}!')
                    print(f'{self.name} did {self.__calculate_damage(self.type1, self.moves[1].damage, opponent.type1)} damage!')
                    opponentDamage = self.__calculate_damage(self.type1, self.moves[1].damage, opponent.type1)
                    opponent.take_damage(opponentDamage)
                    print(f'{opponent.name} remaining HP: {opponent.current_HP}')
                    
                    #choose the move and attack the opponent with the move
                if select_move == "3":
                    print(f'{self.name} used {self.moves[2].name}!')
                    print(self.__calculate_damage(self.type1, self.moves[2].damage, opponent.type1))
                    opponentDamage = self.__calculate_damage(self.type1, self.moves[2].damage, opponent.type1)
                    opponent.take_damage(opponentDamage)
                    print(opponent.current_HP)
                    #choose the move and attack the opponent with the move
                if select_move == "4":
                    print(f'{self.name} used {self.moves[3].name}!')
                    print(f'{self.name} Did {self.__calculate_damage(self.moves[3].type1, self.moves[3].damage, opponent.type1)} damage!')
                    opponentDamage = self.__calculate_damage(self.type1, self.moves[3].damage, opponent.type1)
                    opponent.take_damage(opponentDamage)
                    print(opponent.current_HP)
                #then computer controls opponent and it attacks
                move_decision = random.randint(0,3)
                #random value for which move the opponent uses
                if opponent.isAlive() == True:
                    print(f'{opponent.name} did {opponent.__calculate_damage(opponent.moves[move_decision].type, self.moves[move_decision].damage, self.type)} damage!')
                    selfDamage = opponent.__calculate_damage(opponent.moves[move_decision].type, self.moves[move_decision].damage, self.type)
                    self.take_damage(selfDamage)
                    print(f'{self.name} remaining HP: {self.current_HP}')
                else:
                    #self.name win print message
                    print(f'{opponent.name} fainted!')
                    print(f'{self.name} received {opponent.__calculateEXP()} EXP!')
                    self.__addEXP(opponent.__calculateEXP())
                    self.__levelUp()


            elif select_action == "2":
                #Item menu
                i = 1
                for item in self.bag:
                    print(f'[{i}] {item.name}')
                    i += 1
                select_item = input('Which item would you like to use? \n :')
                #select item based on which increment i is at, at the corresponding item
                if select_item == "1":
                    #use the item
                    self.useItem(self.bag[0])
                    print(f'{self.name} has {self.current_HP} HP')

            



    #def take_damage(sef):

#Add & Configure Data from Pokemon CSV
#as to Pokemon name, stats and type(s)

df = pd.read_csv('dataframes/pokemon.csv')
pokeName = df['Name']
pokeType1 = df['Type 1']
pokeAttack = df['Attack']
pokeDefense = df['Defense']
pokeSpAttack = df['Sp. Atk']
pokeSpDefense = df['Sp. Def']
pokeSpeed = df['Speed']
#For some reason you take row index number and subtract 2

#Initialize battling Pokemon

def locatePokemon():
    #Enter name of Pokemon that you wish to find
    pokeFinder = input("Enter a Pokemon's name!: ")
    #Enters that Pokemon's name into function that finds the Pokemon's row number
    #relative to the csv file
    #Theres probably another way to do this..
    pokeLocation = df.index[df["Name"].str.contains(pokeFinder) == True].tolist()
    #Pull Pokemon's row number from index # ___
    return pokeLocation[0]

#This is a mechanics decision...
#Every time a new Pokemon is brought into the game, you can now search for it in the CSV
#in order to initialize it. 
#As of right now, the program initializes squirtle & charmander in a sort of Pokemon showdown
#-esque battle sim.

#However, if I want to make this game like the overworld games (with graphics and what not),
#then this feature really isn't that needed.
#So basically I have to decide which step i want to take, especially in terms of this intensive.

squirtle = Pokemon(pokeName[9], 100, pokeType1[9], pokeAttack[9], pokeDefense[9], pokeSpAttack[9], pokeSpDefense[9], pokeSpeed[9], 1)
charmander = Pokemon(pokeName[4], 100, pokeType1[4], pokeAttack[4], pokeDefense[4], pokeSpAttack[4], pokeSpDefense[4], pokeSpeed[4],1)


#Add moves

#Shouldn't  be able to change a few things like EXP or HP in obj initialization
#add underscores and update it everywhere

#initialize squirtle moveset
WaterGun = Moves("Water Gun", 'Water', 50)
bubble = Moves("Bubble", 'Water', 25)
scratch = Moves("Scratch", 'Normal', 15)
growl = Moves("Growl", 'Normal', 15)

#initialize charmander moveset
FireSpin = Moves("Fire Spin", 'Fire', 25)
flamethrower = Moves('Flamethrower', 'Fire', 50)

#initialize item
potion = Items('Potion', 20)
superpotion = Items('Super Potion', 50)

#Squirtle Add Moves
squirtle.add_move(WaterGun)
squirtle.add_move(bubble)
squirtle.add_move(scratch)
squirtle.add_move(growl)

#Squirtle Add Item
squirtle.addItem(potion)

#Charmander Add Moves
charmander.add_move(scratch)
charmander.add_move(growl)
charmander.add_move(FireSpin)
charmander.add_move(flamethrower)

#test

squirtle.battle(charmander)
    #I want an add attack method that also uses the type dictionary
    #Also stats, I have two weeks. I want there to be a window with Sprites as well