from sklearn import svm
import csv
import os
import math
import time
from sets import Set

class PokemonPredictor2():

	def predictPokemonAppearances(self):
		start_time = time.time()
		print "Starting Pokemon prediction..."
		matrix = []
		pokemonId_res = []
		features = Set()
		with open(os.path.join(os.path.dirname(__file__), '../datasets/300k.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=',')
			next(reader)
			for row in reader:
				if True or (float(row[1]) < 42.024254 and float(row[1]) > 41.6177356) and (float(row[2]) > -87.9520771 and float(row[2]) < -87.5266041):
					cluster = "cluster-(" + str(float(row[1])) + ", " + str(float(row[2])) + ")"
					features.add(cluster)

					appearedHour = row[13]
					features.add("hour-" + appearedHour)

					appearedDayOfWeek = row[15]
					features.add("weekday-" + appearedDayOfWeek)

					terrainType = row[19]
					features.add("terrain-" + terrainType)

					closeToWater = row[20]
					features.add("ctw-" + closeToWater)

					temperature = row[24]
					features.add("temp-" + temperature)

					windSpeed = row[25]
					features.add("ws-" + windSpeed)

					weatherIcon = row[28]
					features.add("wi-" + weatherIcon)

					population_density = row[37]
					features.add("pd-" + population_density)

					gymDistanceKm = row[42]
					features.add("gd-" + gymDistanceKm)

			lst = list(features)
			print "Number of features = " + str(len(lst))

			input.seek(0)
			next(reader)
			for row in reader:
				if True or (float(row[1]) < 42.024254 and float(row[1]) > 41.6177356) and (float(row[2]) > -87.9520771 and float(row[2]) < -87.5266041):
					matrixRow = []

					for f in lst:
						value = -1
						if f.startswith("cluster-"):
							if f == "cluster-(" + str(float(row[1])) + ", " + str(float(row[2])) + ")":
								value = 1
							else:
								value = 0

						if f.startswith("hour-"):
							if f == "hour-" + row[13]:
								value = 1
							else:
								value = 0
						if f.startswith("weekday-"):
							if f == "weekday-" + row[15]:
								value = 1
							else:
								value = 0
						if f.startswith("terrain-"):
							if f == "terrain-" + row[19]:
								value = 1
							else:
								value = 0
						if f.startswith("ctw-"):
							if f == "ctw-" + row[20]:
								value = 1
							else:
								value = 0
						if f.startswith("temp-"):
							if f == "temp-" + row[24]:
								value = 1
							else:
								value = 0
						if f.startswith("ws-"):
							if f == "ws-" + row[25]:
								value = 1
							else:
								value = 0
						if f.startswith("wi-"):
							if f == "wi-" + row[28]:
								value = 1
							else:
								value = 0
						if f.startswith("pd-"):
							if f == "pd-" + row[37]:
								value = 1
							else:
								value = 0
						if f.startswith("gd-"):
							if f == "gd-" + row[42]:
								value = 1
							else:
								value = 0

						matrixRow.append(value)
					matrix.append(matrixRow)
					pokemonId_res.append(row[0])

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