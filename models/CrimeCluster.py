


class CrimeCluster(object):

	def __init__(self, _centerLatitude, _centerLongitude, _radius):
		self.centerLatitude = _centerLatitude
		self.centerLongitude = _centerLongitude
		self.radius = _radius
		self.crimes = []

	def addCrime(_crime):
		self.crimes.append(_crime)
