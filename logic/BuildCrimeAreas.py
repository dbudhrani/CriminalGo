import csv
import os
import sys

from mrjob.job import MRJob
from mrjob.step import MRStep
from traceback import print_exc
import numpy as np

class BuildCrimeAreas(MRJob):

	# MRJob steps
	def steps(self):
		return [
			MRStep(mapper_init=self.mapper_init1, mapper=self.mapper1, reducer=self.reducer1)
		]

	def mapper_init1(self):
		# We start constructing the crime index dictionary
		self.buildCrimeDegreeDictionary()

	def mapper1(self, _, line):
		# We iterate over the row fields
		for fields in csv.reader([line]):
			# We verify whether the latitude and longitude are set in the current row
			if fields[19] and fields[20]:
				# We yield the cluster as the key and the crime index as the value
				yield str(round(float(fields[19]), 3)) + ", " + str(round(float(fields[20]), 3)), self.cdd[fields[5]]

	def reducer1(self, key, values):
		# We compute the average crime index
		lst = list(values)
		yield key, sum(lst)/float(len(lst))

	def buildCrimeDegreeDictionary(self):
		# Definition of the crime indices
		self.cdd = {}
		self.cdd["ARSON"] = 32
		self.cdd["ASSAULT"] = 95
		self.cdd["BATTERY"] = 96
		self.cdd["BURGLARY"] = 51
		self.cdd["CONCEALED CARRY LICENSE VIOLATION"] = 52
		self.cdd["CRIM SEXUAL ASSAULT"] = 100
		self.cdd["CRIMINAL DAMAGE"] = 50
		self.cdd["CRIMINAL TRESPASS"] = 23
		self.cdd["DECEPTIVE PRACTICE"] = 25
		self.cdd["DOMESTIC VIOLENCE"] = 45
		self.cdd["GAMBLING"] = 17
		self.cdd["HOMICIDE"] = 99
		self.cdd["HUMAN TRAFFICKING"] = 100
		self.cdd["INTERFERENCE WITH PUBLIC OFFICER"] = 15
		self.cdd["INTIMIDATION"] = 63
		self.cdd["KIDNAPPING"] = 97
		self.cdd["LIQUOR LAW VIOLATION"] = 1
		self.cdd["MOTOR VEHICLE THEFT"] = 65
		self.cdd["NARCOTICS"] = 55
		self.cdd["NON - CRIMINAL"] = 3
		self.cdd["NON-CRIMINAL (SUBJECT SPECIFIED)"] = 3
		self.cdd["NON-CRIMINAL"] = 3
		self.cdd["OBSCENITY"] = 40
		self.cdd["OFFENSE INVOLVING CHILDREN"] = 93
		self.cdd["OTHER NARCOTIC VIOLATION"] = 21
		self.cdd["OTHER OFFENSE"] = 5
		self.cdd["PROSTITUTION"] = 35
		self.cdd["PUBLIC INDECENCY"] = 40
		self.cdd["PUBLIC PEACE VIOLATION"] = 18
		self.cdd["RITUALISM"] = 60
		self.cdd["ROBBERY"] = 58
		self.cdd["SEX OFFENSE"] = 75
		self.cdd["STALKING"] = 28
		self.cdd["THEFT"] = 70
		self.cdd["WEAPONS VIOLATION"] = 72