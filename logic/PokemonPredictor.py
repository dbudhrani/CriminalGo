from sklearn import svm
import csv
import os
import math

class PokemonPredictor():

	def predictPokemonAppearances(self):
		print "Starting Pokemon prediction..."
		self.buildNumericDictionary()
		matrix = []
		pokemonId_res = []
		with open(os.path.join(os.path.dirname(__file__), '../datasets/300k.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=',')
			next(reader)
			for row in reader:
				matrixRow = []
				
				#latitude = row[1]
				#matrixRow.append(latitude)

				#longitude = row[2]
				#matrixRow.append(longitude)

				appearedHour = row[13]
				matrixRow.append(appearedHour)

				appearedDayOfWeek = self.cdd[row[15]]
				matrixRow.append(appearedDayOfWeek)

				terrainType = row[19]
				matrixRow.append(terrainType)

				closeToWater = self.cdd[row[20]]
				matrixRow.append(closeToWater)

				temperature = row[24]
				matrixRow.append(temperature)

				windSpeed = row[25]
				matrixRow.append(windSpeed)

				weatherIcon = self.cdd[row[28]]
				matrixRow.append(weatherIcon)

				population_density = row[37]
				matrixRow.append(population_density)

				gymDistanceKm = row[42]
				matrixRow.append(gymDistanceKm)

				psdst = row[49]
				if psdst == "?":
					psdst = 100
				pokestopDistanceKm = psdst
				matrixRow.append(pokestopDistanceKm)

				matrix.append(matrixRow)

				pokemonId = row[0]
				pokemonId_res.append(pokemonId)
		
		numRows = len(matrix)
		numResults = len(pokemonId_res)

		print "Number of rows = " + str(numRows) + "; Number of results = " + str(numResults)

		# Classifier
		clf = svm.SVC(gamma=0.001, C=100.)
		# The first 90% of our dataset conforms the training set.
		# The last 10% conforms the testing set.
		trainingRowsNumber = int(math.floor(numRows * 0.9))
		testRowsNumber = int(numRows - trainingRowsNumber)

		# we execute our training phase
		print "Training..."
		clf.fit(matrix[:trainingRowsNumber], pokemonId_res[:trainingRowsNumber])
		print("--- %s seconds ---" % (time.time() - start_time))
		
		# we predict the classification over our testing set
		print "Predicting..."
		prediction = clf.predict(matrix[-testRowsNumber:])
		print("--- %s seconds ---" % (time.time() - start_time))

		print "Showing results..."
		print "Length of prediction results = " + str(len(prediction))
		print "Prediction = " + str(prediction)

		# we compare our prediction to the real results and compute the accuracy of the algorithm
		pokemonId_res_check = pokemonId_res[-testRowsNumber:]
		i = 0
		accuracy = 0
		while i < testRowsNumber:
			if pokemonId_res_check[i] == prediction[i]:
				accuracy += 1
			i += 1

		accuracy /= float(testRowsNumber)
		accuracy *= 100
		print "Accuracy = " + str(accuracy) + "%"


	def buildNumericDictionary(self):
		self.cdd = {}
		self.cdd["Monday"] = 1
		self.cdd["Tuesday"] = 2
		self.cdd["Wednesday"] = 3
		self.cdd["Thursday"] = 4
		self.cdd["Friday"] = 5
		self.cdd["Saturday"] = 6
		self.cdd["Sunday"] = 7
		self.cdd["dummy_day"] = 8
		self.cdd["true"] = -1
		self.cdd["false"] = 0
		self.cdd["fog"] = 10
		self.cdd["clear-night"] = 11
		self.cdd["partly-cloudy-night"] = 12
		self.cdd["partly-cloudy-day"] = 13
		self.cdd["cloudy"] = 14
		self.cdd["clear-day"] = 15
		self.cdd["rain"] = 16
		self.cdd["wind"] = 17
		self.cdd["?"] = 100

