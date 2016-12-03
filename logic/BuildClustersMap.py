from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from sets import Set

class BuildClustersMap():

	def buildMap(self, crimeClusters, pokemonClusters):
		# Chicago
		#m = Basemap(projection='merc', lat_0=41.84, lon_0=-87.73, resolution='h', area_thresh=0.1,
		#	llcrnrlon=-87.9520771, llcrnrlat=41.6177356, urcrnrlon=-87.5266041, urcrnrlat=42.024254)
		
		# World
		m = Basemap(projection='robin', lat_0=0, lon_0=-130, resolution='l', area_thresh=1000)
		
		m.drawcoastlines()
		m.drawcountries()
		m.fillcontinents(color='green')
		m.drawmapboundary()

		m.drawmeridians(np.arange(0, 360, 30))
		m.drawparallels(np.arange(-90, 90, 30))
		lats = []
		lons = []
		for k in crimeClusters.keys():
			print "k = " + str(k)
			lats.append(float(k.split(',')[0]))
			lons.append(float(k.split(',')[1]))
			rareness = Set()
			rareness.update(crimeClusters.get(k))

		print "lats = " + str(lats)
		print "lons = " + str(lons)
		x,y = m(lons, lats)
		m.plot(x, y, 'bo', markersize=10)

		
		plt.show()
