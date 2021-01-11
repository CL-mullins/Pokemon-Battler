import pygame, sys
from pygame.locals import *
from sys import exit
import os
from moves import Moves
from moves import *
from character import Character
from items import Items
import random
import pandas as pd
from pokemon import Pokemon

pygame.init()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


''' TextObjects '''
#Base
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
#Secondary
def text_objects2(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
#Writes to the message bar
def message_display(text):
    fontObj = pygame.font.Font('/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/assets/pkmnrs.ttf',35)
    TextSurf, TextRect = text_objects(text, fontObj)
    TextRect.center = (200,500)
    screen.blit(TextSurf, TextRect)

#Displays opponents name
def oppName_display(text):
    fontObj2 = pygame.font.Font('/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/assets/pkmnrs.ttf',25)
    TextSurf, TextRect = text_objects2(text, fontObj2)
    TextRect.center = (280,150)
    screen.blit(TextSurf, TextRect)

#Displays opponents level
def oppLevel_display(text):
    fontObj2 = pygame.font.Font('/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/assets/pkmnrs.ttf',20)
    TextSurf, TextRect = text_objects2(text, fontObj2)
    TextRect.center = (450,147)
    screen.blit(TextSurf, TextRect)

#Display players name
def playerName_display(text):
    fontObj2 = pygame.font.Font('/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/assets/pkmnrs.ttf',25)
    TextSurf, TextRect = text_objects2(text, fontObj2)
    TextRect.center = (785,383)
    screen.blit(TextSurf, TextRect)

#Display players level
def playerLevel_display(text):
    fontObj2 = pygame.font.Font('/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/assets/pkmnrs.ttf',20)
    TextSurf, TextRect = text_objects2(text, fontObj2)
    TextRect.center = (972,383)
    screen.blit(TextSurf, TextRect)

def playerHP_display(text):
    fontObj2 = pygame.font.Font('/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/assets/pkmnrs.ttf',15)
    TextSurf, TextRect = text_objects2(text, fontObj2)
    TextRect.center = (935,417)
    screen.blit(TextSurf, TextRect)

bg = pygame.image.load("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/battlebg.png")
background_colour = (255,255,255)
(width, height) = (1000, 564) #Image dimensions are 250 x 141 so I scale to 400% of it
picture = pygame.transform.scale(bg, (width, height))
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
screen.blit(picture, (0,0))
pygame.display.flip()
running = True
FPS = 60
clock = pygame.time.Clock()

'''Fade for Run'''

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((black))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def redrawWindow():
    screen.fill(white)

'''Selection object'''
class Selector(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center  = (width / 2, height / 2)
        self.movex = 0 #Move along X
        self.movey = 0 #Move along Y
        self.frame = 0 #Count frames


    #Draws image to screen
    def draw(self,surface,destination):
        surface.blit(self.image,destination)

    #Resize image
    def scale(self,wdth,hght):
        pygame.transform.scale(self.image,(wdth,hght))

    def control(self, x,y):
        '''Control player movement'''
        self.movex += x
        self.movey += y


    def update(self):
        '''Update sprite position'''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

class Player(pygame.sprite.Sprite):
    def __init__(self, pokemonImage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pokemonImage
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,height / 2)

    #Draws image to screen
    def draw(self,surface,destination):
        surface.blit(self.image,destination)

    #Resize image
    def scale(self,wdth,hght):
        pygame.transform.scale(self.image,(wdth,hght))

class HPBar(pygame.sprite.Sprite):
    def __init__(self, HPBarImage):
        self.image = pygame.image.load(HPBarImage)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    def draw(self, surface, destination):
        surface.blit(self.image,destination)

class TextBar(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    def draw(self, surface, destination):
        surface.blit(self.image,destination)

    def scale(self,wdth,hght):
        pygame.transform.scale(self.image,(wdth,hght))

class TaskBar(pygame.sprite.Sprite):
    def __init__(self,image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    def draw(self, surface, destination):
        surface.blit(self.image,destination)

    def scale(self,wdth,hght):
        pygame.transform.scale(self.image,(wdth,hght))


class BattleBar(pygame.sprite.Sprite):
    def __init__(self,image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)

    def draw(self, surface, destination):
        surface.blit(self.image,destination)
    def scale(self,wdth,hght):
        pygame.transform.scale(self.image,(wdth,hght))



'''Controller Functionality'''
arrayX = [{'cursor':(578,470),'action': 'Attack'},{'cursor':(791,470),'action':'Bag'}] #Attack or Bag # Selects the specific function
arrayY = [{'cursor':(578,510),'action':'Pokemon',},{'cursor':(791,510),'action':'Run'}] #Pokemon or RUn
controller = [arrayX,arrayY]

indexX = 0
indexY = 0 #Chooses if we select from array x or array y

def helper(num): #Holds everything within either 0 or 1
    if num < 0:
        return 1
    elif num >= 2:
        return 0
    else:
        return num

    clock.tick(FPS)

        

    # Add & Configure Data from Pokemon CSV
    # as to Pokemon name, stats and type(s)

df = pd.read_csv('dataframes/pokemon.csv')
pokeName = df['Name']
pokeType1 = df['Type 1']
pokeAttack = df['Attack']
pokeDefense = df['Defense']
pokeSpAttack = df['Sp. Atk']
pokeSpDefense = df['Sp. Def']
pokeSpeed = df['Speed']

# For some reason you take row index number and subtract 2

# Initialize battling Pokemon

def locatePokemon():
    '''Finds Pokemon within CSV'''
    # Enter name of Pokemon that you wish to find
    pokeFinder = input("Enter a Pokemon's name!: ")
    # Enters that Pokemon's name into function that finds the Pokemon's row number
    # relative to the csv file
    # Theres probably another way to do this..
    pokeLocation = df.index[df["Name"].str.contains(pokeFinder) == True].tolist()
    # Pull Pokemon's row number from index # ___
    return pokeLocation[0]

# Mechanics decision, make it Pokemon Showdown-esque, that way I can work backwards from already having a comprehensive
# combat system and add overworld if I want to!

squirtle = Pokemon(pokeName[9], 100, pokeType1[9], pokeAttack[9], pokeDefense[9], pokeSpAttack[9], pokeSpDefense[9], pokeSpeed[9], 1, "/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/squirtle.png")
charmander = Pokemon(pokeName[4], 100, pokeType1[4], pokeAttack[4], pokeDefense[4], pokeSpAttack[4], pokeSpDefense[4], pokeSpeed[4],1, "/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/charmander.png")


# Add moves
# TODO: Considering automating the process of adding moves by finding an appropriate moves csv

# initialize squirtle moveset
WaterGun = Moves("Water Gun", 'Water', 40, 'Special', 25)
bubble = Moves("Bubble", 'Water', 40, 'Special', 25)
scratch = Moves("Scratch", 'Normal', 15, 'Physical', 25)
growl = Moves("Growl", 'Normal', 15, 'Physical', 25)

# initialize charmander moveset
FireSpin = Moves("Fire Spin", 'Fire', 25, 'Special', 25)
flamethrower = Moves('Flamethrower', 'Fire', 50, 'Special', 25)

# initialize item
# TODO: Considering having an effect be a function or method called within the parameters of 
# TODO: the item call
potion = Items('Potion', 20)
superpotion = Items('Super Potion', 50)

# Squirtle Add Moves
squirtle.add_move(WaterGun)
squirtle.add_move(bubble)
squirtle.add_move(scratch)
squirtle.add_move(growl)

# Squirtle Add Item
squirtle.addItem(potion)

# Charmander Add Moves
charmander.add_move(scratch)
charmander.add_move(growl)
charmander.add_move(FireSpin)
charmander.add_move(flamethrower)

'''Initializes  Pokemon as Players'''
#Player
player = Player(squirtle.image) #96 x 96 Image Resolution
#Opponent
player2 = Player(charmander.image) #96 x 96 Image Resolution
#Resize (scale) sprite for game window resolution
'''Scales Pokemon to Screen '''

player.image = pygame.transform.scale(player.image,(384,384))
player2.image = pygame.transform.scale(player2.image, (384,384))

'''Draws Pokemon onto Screen '''
#Draws player pokemon
player.draw(screen,(5,250))
#Draws opponent pokemon
player2.draw(screen,(575,60))
#Destination of player's Pokemon should be determined by the battle location spot

'''Draws HP Bars onto Screen '''
#Player HP Bar
playerHPBar = HPBar("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/[T]PlayerHPBar.png")
playerHPBar.image = pygame.transform.scale(playerHPBar.image,(300,75))
playerHPBar.draw(screen,(700,364))

#Opponent HP Bar
opponentHPBar = HPBar("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/[T]OpponentHPBar.png")
opponentHPBar.image = pygame.transform.scale(opponentHPBar.image,(300,75))
opponentHPBar.draw(screen,(200,125))

'''Draw text screen'''
#Player text screen
MainBar = TextBar("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/BaseTextMenu.png")

#Scale MainBar
MainBar.image = pygame.transform.scale(MainBar.image,(width,125))
MainBar.draw(screen, (0,439))

taskBar = TaskBar("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/TaskMenu.png") #119 x 47
taskBar.image = pygame.transform.scale(taskBar.image,(450,125))
taskBar.draw(screen, (550,439))

'''Initialize Battle Bar'''
battleBar = BattleBar("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/MoveSelection.png")
battleBar.image = pygame.transform.scale(battleBar.image,(width,125))

'''Initialize Menu Text'''
oppName_display(f"{charmander.name}")
oppLevel_display(f"{charmander.level}")
playerName_display(f"{squirtle.name}")
playerLevel_display(f"{squirtle.level}")
playerHP_display(f"{squirtle.current_HP} / {squirtle.hp}")
message_display(f"What will {squirtle.name} do?")

'''Initialize Selector'''
selector = Selector("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/selectionPicker.png")
selector.image = pygame.transform.scale(selector.image,(24,30))
#selector.draw(screen, (578, 470))

while running:

    
    #pygame.display.update()
        # I want an add attack method that also uses the type dictionary
        # Also stats, I have two weeks. I want there to be a window with Sprites as well
    


    #if keypress == 'w': #Calls the function
        #indexY = helper(indexY - 1) #Limits between top or bottom row
        #selector.draw(screen, controller[indexY][indexX]['cursor']

    #if keypress == 's':
    #   indexY = helper(indexY + 1)

        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running=False

        #Moves seelctor around the screen by rewriting it
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                #Move selector up, prepare for selection
                #selector.kill()
                indexY = helper(indexY - 1) #Limits between top or bottom row
                taskBar.draw(screen, (550,439))
                selector.draw(screen, controller[indexY][indexX]['cursor'])
                
                #Needs to stay a specific place
                #selector.control(0,30)
            if event.key == ord('a'):
                #Move selector left
                indexX = helper(indexX - 1) #Limits between top or bottom row
                taskBar.draw(screen, (550,439))
                selector.draw(screen, controller[indexY][indexX]['cursor'])               

            if event.key == ord('s'):
                indexY = helper(indexY + 1) #Limits between top or bottom row
                taskBar.draw(screen, (550,439))
                selector.draw(screen, controller[indexY][indexX]['cursor'])
            if event.key == ord('d'):
                indexX = helper(indexX + 1) #Limits between top or bottom row
                taskBar.draw(screen, (550,439))
                selector.draw(screen, controller[indexY][indexX]['cursor'])
            if event.key == ord('\r'):
                action = controller[indexY][indexX]['action']
                if action == 'Attack':
                    battleBar.draw(screen, (0,439))
                    print('We made it! Back end time!')
                if action == 'Bag':
                    battleBar.draw(screen, (0,439))
                    print('We made it! Back end time!')
                if action == 'Run': #Upon success, closes the game
                    MainBar.draw(screen, (0,439))
                    escapeChance = random.randint(1,60)
                    if escapeChance >= 30:
                        message_display('You escaped!')
                        pygame.display.update()
                        pygame.time.wait(1000)
                        fade(width,height)
                        pygame.time.wait(600)
                        pygame.quit()
                        sys.exit()
                        running=False
                    else:
                        message_display('You could\'t get away!')
                        pygame.time.wait(60)
                    print('We made it! Back end time!')
                if action == 'Pokemon':
                    battleBar.draw(screen, (0,439))
                    print('We made it! Back end time!')
    pygame.display.update()
        
