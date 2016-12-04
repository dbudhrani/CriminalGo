import csv
import os
import sys

from mrjob.job import MRJob
from mrjob.step import MRStep

class BuildPokemonAreas(MRJob):

	# MRJob steps
	def steps(self):
		return [
			MRStep(mapper_init=self.mapper_init1, mapper=self.mapper1, reducer=self.reducer1)
		]

	def mapper_init1(self):
		# We start constructing the pokemon rareness dictionary
		self.buildPokemonRarenessDictionary()

	def mapper1(self, _, line):
		# We iterate over the row fields
		for fields in csv.reader([line]):
			# We verify whether the pokemon id, latitude and longitude are set in the current row
			if fields[0] and fields[1] and fields[2]:
				# We yield the cluster as the key and the pokemon rareness as the value
				yield str(round(float(fields[1]), 3)) + ", " + str(round(float(fields[2]), 3)), int(self.prd[fields[0]])

	def reducer1(self, key, values):
		# We compute the average crime index
		lst = list(values)
		yield key, sum(lst)/float(len(lst))

	def buildPokemonRarenessDictionary(self):
		# Definition of the pokemon rareness degrees based on our own dataset
		self.prd = {}
		with open(os.path.join(os.path.dirname(__file__), '../datasets/pokemon.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=';')
			for row in reader:
				rareness = int(row[2])
				self.prd[row[0]] = rareness