import matplotlib.pyplot as plt
from matplotlib.path import Path
from decimal import Decimal

class PointInPolygon():

	def checkInside(self, latitude, longitude, polygon):
		#plt.plot([1,2,3,4])
		#plt.ylabel('some numbers')
		#plt.show()

		#print "latitude = " + str(latitude)
		#print "longitude = " + str(longitude)
		#print "polygon = " + str(polygon)

		pol = Path(polygon)
		#print "longitude = " + longitude
		#print float(longitude)
		#print "latitude = " + latitude
		#print "float latitude = " + str(float(latitude))
		point = (float(longitude), float(latitude))
		return pol.contains_point(point)