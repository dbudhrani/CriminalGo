from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import csv
import os
import math
import time
from sets import Set

class PokemonPredictor():

	def predictPokemonAppearances(self):
		# We start the pokemon appearances prediction
		print "Starting Pokemon prediction..."
		# We build the necessary dictionaries
		self.buildNumericDictionary()
		self.buildPokemonRarenessDictionary()
		self.pcd = {}
		# The matrix that will hold our rows and features
		matrix = []
		# The array thay will hold the target values
		pokemonId_res = []

		# We load the pokemon appearances CSV file
		with open(os.path.join(os.path.dirname(__file__), '../datasets/300k.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=',')
			# We skip the header row
			next(reader)
			for row in reader:
				# Some row have "dummy_day" as the day, so we skip them
				# Moreover, we are only interested in the pokemon appearances of Chicago
				if (not row[15] == "dummy_day") and row[21] == "Chicago":
					# We create a new matrix row
					matrixRow = []

					# Appearance latitude
					latitude = float(row[1])
					matrixRow.append(round(latitude, 4))

					# Appearance longitude
					longitude = float(row[2])
					matrixRow.append(round(longitude, 4))

					# Appearance day of week
					appearedDayOfWeek = self.cdd[row[15]]
					matrixRow.append(appearedDayOfWeek)

					# terrain type in the appearance (numerical value)
					terrainType = row[19]
					matrixRow.append(terrainType)

					# boolean value that determines whether the appearance was close to the water (100m or less)
					closeToWater = self.cdd[row[20]]
					matrixRow.append(closeToWater)

					# Weather in the pokemon appearance
					weatherIcon = self.cdd[row[28]]
					matrixRow.append(weatherIcon)

					# population density in the area in which the pokemon appeared
					population_density = float(row[37])
					matrixRow.append(round(population_density, 1))

					# distance to a pokemon gym
					gymDistanceKm = float(row[42])
					matrixRow.append(round(gymDistanceKm, 1))

					# we append the current row
					matrix.append(matrixRow)

					# we include the pokemon id in the target array
					pokemonId = row[0]
					pokemonId_res.append(self.prd[pokemonId])
		
		# total number of rows
		numRows = len(matrix)
		numResults = len(pokemonId_res)

		# Classifier
		rf = RandomForestClassifier(n_estimators=50)
		# The first 80% of our dataset conforms the training set.
		# The last 20% conforms the testing set.
		trainingRowsNumber = int(math.floor(numRows * 0.8))
		testRowsNumber = int(numRows - trainingRowsNumber)

		# we execute our training phase
		print "Training..."
		rf.fit(matrix[:trainingRowsNumber], pokemonId_res[:trainingRowsNumber])

		# we predict the classification over our testing set
		print "Predicting..."
		prediction = rf.predict(matrix[-testRowsNumber:])

		# We show the results
		print "Showing results..."
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

		return self.pcd


	def buildNumericDictionary(self):
		# We assign a numerical value to every possible textual value
		self.cdd = {}
		self.cdd["Monday"] = 0
		self.cdd["Tuesday"] = 1
		self.cdd["Wednesday"] = 2
		self.cdd["Thursday"] = 3
		self.cdd["Friday"] = 4
		self.cdd["Saturday"] = 5
		self.cdd["Sunday"] = 6
		self.cdd["dummy_day"] = 7
		self.cdd["true"] = 0
		self.cdd["false"] = 1
		self.cdd["fog"] = 0
		self.cdd["clear-night"] = 1
		self.cdd["partly-cloudy-night"] = 2
		self.cdd["partly-cloudy-day"] = 3
		self.cdd["cloudy"] = 4
		self.cdd["clear-day"] = 5
		self.cdd["rain"] = 6
		self.cdd["wind"] = 7
		self.cdd["?"] = 5

	def buildPokemonRarenessDictionary(self):
		# We condense the pokemon rareness categories in 3 values
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

	def addPokemonCluster(self, latitude, longitude, rareness, decimals):
		# We add a pokemon appearance
		key = str(round(float(latitude), decimals)) + ", " + str(round(float(longitude), decimals))
		values = Set()
		if key in self.pcd:
			values.update(self.pcd.get(key))
		values.add(rareness)
		self.pcd[key] = values