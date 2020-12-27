import pandas as pd


df = pd.read_csv('dataframes/pokemon.csv')

#print(df["Legendary"])


#CSV works!




#Found a way to return the index, now I need a wway to return the index number

def locatePokemon():
    #Enter name of Pokemon that you wish to find
    pokeFinder = input("Enter a Pokemon's name!: ")
    #Enters that Pokemon's name into function that finds the Pokemon's row number
    #relative to the csv file
    #Theres probably another way to do this..
    pokeLocation = df.index[df["Name"].str.contains(pokeFinder) == True].tolist()
    #Pull Pokemon's row number from index # ___
    return pokeLocation[0]
    #print(pokeLocation[0])


seven = locatePokemon()
print(seven)

#Parse through CSV for Pokemon's name

