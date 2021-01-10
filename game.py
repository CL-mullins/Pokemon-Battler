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



bg = pygame.image.load("/Users/chrismullins/dev/courses/cs1.1/Pokemon-Battler/sprites/battlebg.png")
background_colour = (255,255,255)
(width, height) = (300, 200)
picture = pygame.transform.scale(bg, (width, height))
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
screen.blit(picture, (0,0))
pygame.display.flip()
running = True
FPS = 60
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pokemonImage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pokemonImage
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,height / 2)

    def draw(self,surface,destination):
        surface.blit(self.image,destination)



while running:
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

    # test
    all_sprites = pygame.sprite.Group()
    player = Player(squirtle.image)
    all_sprites.add(player)
    player.draw(screen,(0,100))
    #Draws Player's Pokemon onto the screen
    #Destination of player's Pokemon should be determined by the battle location spot
    pygame.display.update()
    #squirtle.battle(charmander)
        # I want an add attack method that also uses the type dictionary
        # Also stats, I have two weeks. I want there to be a window with Sprites as well

        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running=False

