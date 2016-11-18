


class CrimeRecord(object):

	def __init__ (self, _id, _date, _IUCR, _locationDescription, _domestic, _district, _year, _latitude, _longitude):
		self.id = _id
		self.date = _date
		self.IUCR = _IUCR
		self.locationDescription = _locationDescription
		self.domestic = _domestic
		self.district = _district
		self.year = _year
		self.latitude = _latitude
		self.longitude = _longitude