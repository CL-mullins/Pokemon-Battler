A fun Pokemon Battler inspired by the Superhero Dueler done for class / intensive also inspired by Zarel's Pokemon Showdown [https://pokemonshowdown.com/]


***MEDIA***

Screenshots:

Main Menu


![Main Menu](https://github.com/CL-mullins/Pokemon-Battler/blob/main/screenshots/Main%20Menu.png?raw=true)

Attack Menu


![Attack Menu](https://github.com/CL-mullins/Pokemon-Battler/blob/main/screenshots/Attack%20Menu.png?raw=true)


Interactable User Interface

! [UI](https://github.com/CL-mullins/Pokemon-Battler/blob/main/screenshots/Screen%20Shot%202021-01-11%20at%206.01.24%20PM.png)

Youtube Explanation

UNDER CONSTRUCTION


***END OF MEDIA***


***BREAKDOWN***


Theres a Pokemon class which contains:
    The Pokemon (it's name)
    It's maximum HP
    It's type
    It's damage modifier (based on level)
        I want to make this complex, but do I have time ??
    It's level
    It's moves list
    It's held item and it's effects

    An IsAlive() method
        checks if the Pokemon is alive based on current HP
    A LevelUp() method
        checks if current XP >= max XP and increases the Pokemon's level by one
    A LearnMove(move) method
        adds a move to the Pokemon's move roster. If theres already 4 moves then it deletes one move to add another
    An attack(move) method which when selected during the user's turn, activates the required move


Theres a Moves class which contains:
    The move (it's name)
    It's type
    It's damage modifier
    It's PP
    [Extra] It's effect
    Calling the Moves class creates a move object.

Theres an items class which contains:
    The item (it's name)
    It's effect
    
Theres a Battle class which contains:
    YourTurn(): which allows the user whose turn it is to chose thier move
    Fight(): battles two Pokemon against eachother and rewards XP to the participating Pokemon
    Switch(): Switches participating Pokemon 

Theres a GUI I created with PyGame:
    Allows for the user to choose between Fight, Pokemon, Bag, and Run options
    Has sprite representations for the terminal battles
    Does not include all back end functionality


***END OF BREAKDOWN***