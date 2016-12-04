import csv
import os
import time

from mrjob.runner import MRJobRunner
from geopy.geocoders import Nominatim

from models import Pokemon
from models import CrimeRecord
from models import CrimeCluster
from logic import BuildCrimeAreas
from logic import PointInPolygon
from logic import PokemonPredictor
from logic import PokemonPredictor2
from logic import BuildClustersMap
from logic import BuildPokemonAreas
from logic import SQLManager
import numpy as np

def main():

	# We execute the pokemon prediction
	pokepredictor = PokemonPredictor()
	pcd = pokepredictor.predictPokemonAppearances()

	# We execute the crime clustering
	mr_job = BuildCrimeAreas(args=['datasets/Crimes_-_2001_to_present_copia.csv'])
	crimes = {}
	with mr_job.make_runner() as runner:
		runner.run()
		print "___ Crime clusters ___"
		for line in runner.stream_output():
			key, value = mr_job.parse_output_line(line)
			crimes[key] = value
			print "key = " + key + "; " + str(value)

	# We execute the pokemon rareness clustering
	mr_job2 = BuildPokemonAreas(args=['datasets/300k.csv'])
	pokemons = {}
	with mr_job2.make_runner() as runner2:
		runner2.run()
		print "___ Pokemon clusters ___"
		for line in runner2.stream_output():
			key, value = mr_job2.parse_output_line(line)
			pokemons[key] = value
			print "key = " + key + "; " + str(value)

	# combined dictionary: crimes + pokemon rareness
	combined = {}
	for k in crimes.keys():
		if k in pokemons:
			x = crimes[k]
			y = pokemons[k]
			# we use the location as the key and the (crime index, pokemon rareness) as the value
			combined[k] = (x, y)

	# output CSV file
	combinedfile = "datasets/combined.csv"
	fw = open(combinedfile, 'w')
	for k in combined:
		# latitude, longitude, crime_index, pokemon_rareness
		line = str(float(k.split(',')[0])) + ";" + str(float(k.split(',')[1])) + ";" + str(combined[k][0]) + ";" + str(combined[k][1]) + "\n"
		fw.write(line)
	fw.close()

	# We construct the SQL database
	sql = SQLManager()
	sql.createDatabase()
	geolocator = Nominatim()

	f = False
	print "____ Clusters sorted by crime index ____"
	print "Cluster; Address; Crime index; Pokemon rareness"
	# We query the clusters sorted by crime index
	for row in sql.sortByCrimeIndex():
		# We obtain the qualitative description of the location using GeoPy
		location = geolocator.reverse(str(row[0]) + ", " + str(row[1]))
		if not f:
			print(location.raw)
			f = True
		# We print the results
		print "(" + str(row[0]) + ", " + str(row[1]) + "); " + location.address + "; " + str(row[2]) + "; " + str(row[3])

	print "___ Clusters sorted by pokemon rareness ___"
	print "Cluster; Address; Crime index; Pokemon rareness"
	# We query the clusters sorted by pokemon rareness
	for row in sql.sortByPokemonRareness():
		# We obtain the qualitative description of the location using GeoPy
		location = geolocator.reverse(str(row[0]) + ", " + str(row[1]))
		# We print the results
		print "(" + str(row[0]) + ", " + str(row[1]) + "); " + location.address + "; " + str(row[2]) + "; " + str(row[3])


	# We build the maps
	m = BuildClustersMap()
	m.buildCrimeMap(crimes)
	m.buildPokemonMap(pokemons)


if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))