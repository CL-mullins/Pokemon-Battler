A fun Pokemon Battler inspired by the Superhero Dueler done for class

TODO: Trying to integrate battle & attack methods with this type chart dictionary data.

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


Assignment Requirements:

Classes:

At least 4 classes are defined.
At least 1 class demonstrates composition (being composed of other objects).
At least 1 class inherits from another class.
All classes are used to instantiate example objects.
Methods:

Each class has at least 2 methods that use and/or modify class attributes.
The subclass overrides at least one superclass method (this can be init or another method).
Rationale about which methods are private, protected, or public should be provided in code comments or verbally during presentation.
Attributes:

Each class has a least 2 instance attributes created in init()
Rationale about which attributes are private, protected, or public should be provided in code comments or verbally during presentation.
Diagram:

A diagram is provided that shows an overview of all the classes that make up the system design
Diagram shows relationships between classes.
Presentation:

5 - 10 min in-class presentation is given showing off all of the above requirements.
Note: If you cannot make the presentation day, you may turn in a video presentation beforehand to instructor via Slack.
