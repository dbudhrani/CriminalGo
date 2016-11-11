import csv

from models import Pokemon

def main():
	loadPokemonTypes()

def loadPokemonTypes():
	with open("datasets/pokemon.csv") as input:
		reader = csv.reader(input, delimiter=';')
		for row in reader:
			pokemon = Pokemon(row[0], row[1], row[2])
			print "ID = " + str(pokemon.id) + "; Name = " + pokemon.name + "; Rareness = " + str(pokemon.rareness)


if __name__ == "__main__":
	main()