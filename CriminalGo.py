import csv

from models import Pokemon
from models import CrimeRecord
from models import CrimeCluster

def main():
	loadPokemonTypes()
	loadCrimes()

def loadPokemonTypes():
	with open("datasets/pokemon.csv") as input:
		reader = csv.reader(input, delimiter=';')
		for row in reader:
			pokemon = Pokemon(row[0], row[1], row[2])
			print "ID = " + str(pokemon.id) + "; Name = " + pokemon.name + "; Rareness = " + str(pokemon.rareness)

def loadCrimes():
	with open("datasets/Crimes_-_2001_to_present.csv") as input:
		reader = csv.reader(input, delimiter=',')
		i = 0
		next(reader)	# we skip the header row
		for row in reader:
			crime = CrimeRecord(row[0], row[2], row[4], row[7], row[9], row[17], row[19], row[20])
			if (i < 100):
				print "ID = " + str(crime.id) + "; Date = " + crime.date + "; IUCR = " + str(crime.IUCR) + "; Location description = " + crime.locationDescription + "; Domestic = " + crime.domestic + "; Year = " + str(crime.year) + "; Latitude = " + crime.latitude + "; Longitude = " + str(crime.longitude)
			i = i + 1

if __name__ == "__main__":
	main()