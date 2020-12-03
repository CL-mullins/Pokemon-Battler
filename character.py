class Character:
    def __init__(self, name):
        self.name = name

    def requestNickname(self):
        #Asks user for a name 
        #returns name
        nickname = input('Enter nickname: ')
        return nickname

    def giveNickname(self, name):
        #re declares name value and gives Pokemon (or character) new name
        self.name = name
