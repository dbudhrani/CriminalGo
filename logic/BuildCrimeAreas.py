import csv
import os
import sys

from mrjob.job import MRJob
from mrjob.step import MRStep

from PointInPolygon import PointInPolygon
from traceback import print_exc

import numpy as np

class BuildCrimeAreas(MRJob):

	data = []
	dataLoaded = False

	def steps(self):
		return [
			MRStep(mapper_init=self.mapper_init1, mapper=self.mapper1, reducer=self.reducer1)
		]

	def mapper_init1(self):
		self.buildCrimeDegreeDictionary()
		self.pip = PointInPolygon()
		#self.pip.checkInside()
		self.commAreas = open(os.path.join(os.path.dirname(__file__), '../datasets/CommAreas.csv'), 'r')
		self.commReader = csv.reader(self.commAreas, delimiter=',')
		print "mapper_init - commAreas = " + str(self.commAreas)
		print "mapper_init - commReader = " + str(self.commReader)
		self.data = []
		self.dataLoaded = False

	def mapper1(self, _, line):
#		self.commAreas = open(os.path.join(os.path.dirname(__file__), '../datasets/CommAreas.csv'))
#		self.commReader = csv.reader(self.commAreas, delimiter=',')
		#print "mapper - commAreas = " + str(self.commAreas)
		#print "mapper - commReader = " + str(self.commReader)
		for fields in csv.reader([line]):
			if fields[19] and fields[20]:
				yield str(round(float(fields[19]), 3)) + ", " + str(round(float(fields[20]), 3)), self.cdd[fields[5]]
			#elif fields[13]:
			#	yield "Community area " + fields[13], 1
			#else:
			#	yield -2, 1

	def reducer1(self, key, values):
		lst = list(values)
		yield key, sum(lst)/float(len(lst))
#		yield key, sum(values)

	def buildCrimeDegreeDictionary(self):
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