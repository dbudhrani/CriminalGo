from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import csv
import os
import math
import time
from sets import Set

class PokemonPredictor():

	def predictPokemonAppearances(self):
		start_time = time.time()
		print "Starting Pokemon prediction..."
		self.buildNumericDictionary()
		self.buildPokemonRarenessDictionary()
		self.pcd = {}
		matrix = []
		pokemonId_res = []
		with open(os.path.join(os.path.dirname(__file__), '../datasets/300k.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=',')
			next(reader)
			for row in reader:
				#if (not row[15] == "dummy_day") and (float(row[1]) < 42.024254 and float(row[1]) > 41.6177356) and (float(row[2]) > -87.9520771 and float(row[2]) < -87.5266041):
				if (not row[15] == "dummy_day") and row[21] == "Chicago":
					matrixRow = []
					
					latitude = float(row[1])
					matrixRow.append(round(latitude, 4))

					longitude = float(row[2])
					matrixRow.append(round(longitude, 4))

					#appearedHour = row[13]
					#matrixRow.append(appearedHour)

					appearedDayOfWeek = self.cdd[row[15]]
					matrixRow.append(appearedDayOfWeek)

					terrainType = row[19]
					matrixRow.append(terrainType)

					closeToWater = self.cdd[row[20]]
					matrixRow.append(closeToWater)

					#temperature = float(row[24])
					#matrixRow.append(round(temperature, 1))

					#windSpeed = row[25]
					#matrixRow.append(windSpeed)

					weatherIcon = self.cdd[row[28]]
					matrixRow.append(weatherIcon)

					population_density = float(row[37])
					matrixRow.append(round(population_density, 1))

					gymDistanceKm = float(row[42])
					matrixRow.append(round(gymDistanceKm, 1))

					#psdst = row[49]
					#if psdst == "?":
					#	psdst = 100
					#pokestopDistanceKm = round(float(psdst), 1)
					#matrixRow.append(pokestopDistanceKm)

					matrix.append(matrixRow)

					pokemonId = row[0]
					pokemonId_res.append(self.prd[pokemonId])
		
		numRows = len(matrix)
		numResults = len(pokemonId_res)

		print "Number of rows = " + str(numRows) + "; Number of results = " + str(numResults)

		# Classifier
		clf = svm.SVC(gamma=0.001, C=100.)
		#rf = RandomForestClassifier(n_estimators=50)
		# The first 90% of our dataset conforms the training set.
		# The last 10% conforms the testing set.
		trainingRowsNumber = int(math.floor(numRows * 0.8))
		testRowsNumber = int(numRows - trainingRowsNumber)

		# we execute our training phase
		print "Training..."
		clf.fit(matrix[:trainingRowsNumber], pokemonId_res[:trainingRowsNumber])
#		rf.fit(matrix[:trainingRowsNumber], pokemonId_res[:trainingRowsNumber])
		print("--- %s seconds ---" % (time.time() - start_time))

		# we predict the classification over our testing set
		print "Predicting..."
		prediction = clf.predict(matrix[-testRowsNumber:])
		#prediction = rf.predict(matrix[-testRowsNumber:])
		print("--- %s seconds ---" % (time.time() - start_time))

		print "Showing results..."
		print "Length of prediction results = " + str(len(prediction))
		print "Prediction = " + str(prediction)

		# we compare our prediction to the real results and compute the accuracy of the algorithm
		pokemonId_res_check = pokemonId_res[-testRowsNumber:]
		i = 0
		accuracy = 0
		while i < testRowsNumber:
			self.addPokemonCluster(matrix[trainingRowsNumber+i][0], matrix[trainingRowsNumber+i][1], prediction[i], 2)
			if pokemonId_res_check[i] == prediction[i]:
				accuracy += 1
			i += 1

		accuracy /= float(testRowsNumber)
		accuracy *= 100
		print "Accuracy = " + str(accuracy) + "%"

		#for k in self.pcd.keys():
		#	print "key = " + k + "; value = " + str(self.pcd[k])
		return self.pcd


	def buildNumericDictionary(self):
		self.cdd = {}
		self.cdd["Monday"] = 0#1
		self.cdd["Tuesday"] = 1#2
		self.cdd["Wednesday"] = 2#3
		self.cdd["Thursday"] = 3#4
		self.cdd["Friday"] = 4#5
		self.cdd["Saturday"] = 5#6
		self.cdd["Sunday"] = 6#7
		self.cdd["dummy_day"] = 7#8
		self.cdd["true"] = 0#-1
		self.cdd["false"] = 1#0
		self.cdd["fog"] = 0#10
		self.cdd["clear-night"] = 1#11
		self.cdd["partly-cloudy-night"] = 2#12
		self.cdd["partly-cloudy-day"] = 3#13
		self.cdd["cloudy"] = 4#14
		self.cdd["clear-day"] = 5#15
		self.cdd["rain"] = 6#16
		self.cdd["wind"] = 7#17
		self.cdd["?"] = 5#100

	def buildPokemonRarenessDictionary(self):
		self.prd = {}
		with open("datasets/pokemon.csv") as input:
			reader = csv.reader(input, delimiter=';')
			for row in reader:
				rareness = int(row[2])
				if rareness == 1 or rareness == 2:
					self.prd[row[0]] = 1
				elif rareness == 3 or rareness == 4:
					self.prd[row[0]] = 2
				else:
					self.prd[row[0]] = 3
				#self.prd[row[0]] = int(row[2]) > 3

	def addPokemonCluster(self, latitude, longitude, rareness, decimals):
		key = str(round(float(latitude), decimals)) + ", " + str(round(float(longitude), decimals))
		values = Set()
		if key in self.pcd:
			values.update(self.pcd.get(key))
		values.add(rareness)
		self.pcd[key] = values