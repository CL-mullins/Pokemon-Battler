class Character:
    def __init__(self, name, species):
        self.name = name #Name of the character
        self.species = species #Human or Pokemon
        self.team = list() #pokemon team
        self.items = list()

    def requestNickname(self):
        #Asks user for a name 
        #returns name
        nickname = input('Enter nickname: ')
        return nickname

    def giveNickname(self, name):
        #re declares name value and gives Pokemon (or character) new name
        self.name = name

    def addItem(self, item):
        #Adds item to user's backpack worth of items
        self.items.append(item)

    #def teamFull(self):
     #   if self.species == 'Human':
      #      if len(self.team) > 6:
                #Remove Pokemon from team, send to box
