from sklearn import svm
import csv
import os
import math
import time
from sets import Set
from sklearn.feature_extraction import FeatureHasher
from sklearn.ensemble import RandomForestClassifier
from scipy import *
from scipy.sparse import *
from sklearn import preprocessing

class PokemonPredictor2():

	def getL2(self, matrix):
		for elem in matrix:
			return str(elem)

	def predictPokemonAppearances(self):
		start_time = time.time()
		print "Starting Pokemon prediction..."
		matrix = []
		pokemonId_res = []
		features = Set()
		le = preprocessing.LabelEncoder()
		fw = open(os.path.join(os.path.dirname(__file__), '../matrix.txt'), 'w')
		with open(os.path.join(os.path.dirname(__file__), '../datasets/300k.csv'), 'r') as input:
			reader = csv.reader(input, delimiter=',')
			next(reader)
			for row in reader:
				if (not row[15] == "dummy_day") and (float(row[1]) < 42.024254 and float(row[1]) > 41.6177356) and (float(row[2]) > -87.9520771 and float(row[2]) < -87.5266041):
					#cluster = "cluster-(" + str(round(float(row[1]), 2)) + ", " + str(round(float(row[2]), 2)) + ")"
					#features.add(cluster)

					appearedHour = row[13]
					features.add("hour-" + appearedHour)

					appearedDayOfWeek = row[15]
					features.add("weekday-" + appearedDayOfWeek)

					terrainType = row[19]
					features.add("terrain-" + terrainType)

					closeToWater = row[20]
					features.add("ctw-" + closeToWater)

					#temperature = row[24]
					#features.add("temp-" + temperature)

					#windSpeed = row[25]
					#features.add("ws-" + windSpeed)

					weatherIcon = row[28]
					features.add("wi-" + weatherIcon)

					#population_density = row[37]
					#features.add("pd-" + population_density)

					#gymDistanceKm = row[42]
					#features.add("gd-" + gymDistanceKm)

			lst = list(features)
			print "Number of features = " + str(len(lst))
			fw.write(str(lst) + "\n")

			input.seek(0)
			next(reader)
			for row in reader:
				if (not row[15] == "dummy_day") and (float(row[1]) < 42.024254 and float(row[1]) > 41.6177356) and (float(row[2]) > -87.9520771 and float(row[2]) < -87.5266041):
					matrixRow = []

					for f in lst:
						value = -1
						#if f.startswith("cluster-"):
						#	if f == "cluster-(" + str(round(float(row[1]), 2)) + ", " + str(round(float(row[2]), 2)) + ")":
						#		value = 1
						#	else:
						#		value = 0

						if f.startswith("hour-"):
							if f == "hour-" + row[13]:
								value = 1
							else:
								value = 0
						if f.startswith("weekday-") and not f == "weekday-dummy_day":
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
						#if f.startswith("temp-"):
						#	if f == "temp-" + row[24]:
						#		value = 1
						#	else:
						#		value = 0
						#if f.startswith("ws-"):
						#	if f == "ws-" + row[25]:
						#		value = 1
						#	else:
						#		value = 0
						if f.startswith("wi-"):
							if f == "wi-" + row[28]:
								value = 1
							else:
								value = 0
						#if f.startswith("pd-"):
						#	if f == "pd-" + row[37]:
						#		value = 1
						#	else:
						#		value = 0
						#if f.startswith("gd-"):
						#	if f == "gd-" + row[42]:
						#		value = 1
						#	else:
						#		value = 0

						matrixRow.append(value)
					matrix.append(matrixRow)
					fw.write(str(matrixRow) + "\n")
					pokemonId_res.append(row[0])
		fw.close()
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

		print "Computing prediction accuracy..."
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

'''
		hasher = FeatureHasher(n_features=100, input_type='string')
		rf = RandomForestClassifier(n_estimators=50)
		newMatrix = hasher.transform(self.getL2(d) for d in matrix)
		D = csr_matrix(newMatrix).todense()

		numRows = len(D)
		print "D rows = " + str(len(D))
		print "D cols = " + str(D[0].size)

		trainingRowsNumber = int(math.floor(numRows * 0.9))
		targetRowsNumber = trainingRowsNumber
		testRowsNumber = int(numRows - trainingRowsNumber)
		trainingRows = D[:trainingRowsNumber]
		testRows = D[-testRowsNumber:]
		targetRows = pokemonId_res[:trainingRowsNumber]

		print "Training..."
		rf.fit(trainingRows, targetRows)

		print "Predicting..."
		prediction = rf.predict(testRows)
		print "Prediction = " + str(prediction)
'''

