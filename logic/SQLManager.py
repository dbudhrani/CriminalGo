import sqlite3
import os
import csv

class SQLManager():

	def createDatabase(self):
		# Create database
		conn = sqlite3.connect('combined.db')
		# Create cursor
		c = conn.cursor()
		# Check if table exists. If so, drop it.
		c.execute('DROP TABLE IF EXISTS combined')
		conn.commit()
		# Create table 'combined'
		c.execute('CREATE TABLE combined (latitude real, longitude real, crimeIndex real, pokemonRareness real)')
		conn.commit()
		with open(os.path.join(os.path.dirname(__file__), '../datasets/combined.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=';')
			for row in reader:
				# We create a new line in SQL from every line in the CSV file
				c.execute('INSERT INTO combined VALUES (' + row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3] + ')')
				conn.commit()
		conn.close()

	# We sort the clusters by crime index in descending mode
	def sortByCrimeIndex(self):
		conn = sqlite3.connect('combined.db')
		c = conn.cursor()
		return c.execute('SELECT latitude, longitude, crimeIndex, pokemonRareness FROM combined ORDER BY crimeIndex DESC')

	# We sort the clusters by pokemon rareness in descending mode
	def sortByPokemonRareness(self):
		conn = sqlite3.connect('combined.db')
		c = conn.cursor()
		return c.execute('SELECT latitude, longitude, crimeIndex, pokemonRareness FROM combined ORDER BY pokemonRareness DESC')
