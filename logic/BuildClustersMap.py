from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from sets import Set

class BuildClustersMap():

	def buildCrimeMap(self, crimeClusters):
		# Chicago
		#m = Basemap(projection='merc', lat_0=41.84, lon_0=-87.73, resolution='h', area_thresh=0.1,
		#	llcrnrlon=-87.9520771, llcrnrlat=41.6177356, urcrnrlon=-87.5266041, urcrnrlat=42.024254)

		# Chicago greater area
		m = Basemap(projection='merc', lat_0=41.84, lon_0=-87.73, resolution='h', area_thresh=0.1,
			llcrnrlon=-87.9520771, llcrnrlat=41.6177356, urcrnrlon=-87.48, urcrnrlat=42.05)

		# World
		#m = Basemap(projection='robin', lat_0=0, lon_0=-130, resolution='l', area_thresh=1000)

		m.drawcoastlines()
		m.drawcountries()
		m.fillcontinents(color='green')
		m.drawmapboundary()

		m.drawmeridians(np.arange(0, 360, 30))
		m.drawparallels(np.arange(-90, 90, 30))

		cid = {}
		for k in crimeClusters.keys():
			crimeIndex = crimeClusters.get(k)
			if crimeIndex >= 0 and crimeIndex < 5:
				color = 'yo'
			elif crimeIndex >= 5 and crimeIndex < 10:
				color = 'yo'
			elif crimeIndex >= 10 and crimeIndex < 15:
				color = 'yo'
			elif crimeIndex >= 15 and crimeIndex < 20:
				color = 'yo'
			elif crimeIndex >= 20 and crimeIndex < 25:
				color = 'co'
			elif crimeIndex >= 25 and crimeIndex < 30:
				color = 'co'
			elif crimeIndex >= 30 and crimeIndex < 35:
				color = 'co'
			elif crimeIndex >= 35 and crimeIndex < 40:
				color = 'co'
			elif crimeIndex >= 40 and crimeIndex < 45:
				color = 'bo'
			elif crimeIndex >= 45 and crimeIndex < 50:
				color = 'bo'
			elif crimeIndex >= 50 and crimeIndex < 55:
				color = 'bo'
			elif crimeIndex >= 55 and crimeIndex < 60:
				color = 'bo'
			elif crimeIndex >= 60 and crimeIndex < 65:
				color = 'ko'
			elif crimeIndex >= 65 and crimeIndex < 70:
				color = 'ko'
			elif crimeIndex >= 70 and crimeIndex < 75:
				color = 'ko'
			elif crimeIndex >= 75 and crimeIndex < 80:
				color = 'ko'
			elif crimeIndex >= 80 and crimeIndex < 85:
				color = 'mo'
			elif crimeIndex >= 85 and crimeIndex < 90:
				color = 'mo'
			elif crimeIndex >= 90 and crimeIndex < 95:
				color = 'mo'
			elif crimeIndex >= 95:
				color = 'mo'

			if not color in cid:
				x = []
				y = []
				cid[color] = x, y
			else:
				cid.get(color)[0].append(float(k.split(',')[0]))
				cid.get(color)[1].append(float(k.split(',')[1]))

		for k in cid.keys():
			x,y = m(cid[k][1], cid[k][0])
			m.plot(x, y, k, markersize=5)

		plt.show()

	def buildPokemonMap(self, pokemonClusters):

		# Chicago
		#m = Basemap(projection='merc', lat_0=41.84, lon_0=-87.73, resolution='h', area_thresh=0.1,
		#	llcrnrlon=-87.9520771, llcrnrlat=41.6177356, urcrnrlon=-87.5266041, urcrnrlat=42.024254)

		# Chicago greater area
		#m = Basemap(projection='merc', lat_0=41.84, lon_0=-87.73, resolution='h', area_thresh=0.1,
		#	llcrnrlon=-87.9520771, llcrnrlat=41.6177356, urcrnrlon=-87.48, urcrnrlat=42.05)

		# World
		m = Basemap(projection='robin', lat_0=0, lon_0=-130, resolution='l', area_thresh=1000)

		m.drawcoastlines()
		m.drawcountries()
		m.fillcontinents(color='green')
		m.drawmapboundary()

		m.drawmeridians(np.arange(0, 360, 30))
		m.drawparallels(np.arange(-90, 90, 30))

		prd = {}
		for k in pokemonClusters.keys():
			rareness = pokemonClusters.get(k)
			if rareness >= 0 and rareness < 0.5:
				color = 'yo'
			elif rareness >= 0.5 and rareness < 1.0:
				color = 'yo'
			elif rareness >= 1.0 and rareness < 1.5:
				color = 'co'
			elif rareness >= 1.5 and rareness < 2.0:
				color = 'co'
			elif rareness >= 2.0 and rareness < 2.5:
				color = 'bo'
			elif rareness >= 2.5 and rareness < 3.0:
				color = 'bo'
			elif rareness >= 3.0 and rareness < 3.5:
				color = 'ko'
			elif rareness >= 3.5 and rareness < 4.0:
				color = 'ko'
			elif rareness >= 4.0 and rareness < 4.5:
				color = 'mo'
			elif rareness >= 4.5:
				color = 'mo'

			if not color in prd:
				x = []
				y = []
				prd[color] = x, y
			else:
				prd.get(color)[0].append(float(k.split(',')[0]))
				prd.get(color)[1].append(float(k.split(',')[1]))

		for k in prd.keys():
			x,y = m(prd[k][1], prd[k][0])
			m.plot(x, y, k, markersize=5)

		plt.show()
'''
		for k in pokemonClusters.keys():
			print "k = " + str(k)
			lats.append(float(k.split(',')[0]))
			lons.append(float(k.split(',')[1]))
			rareness = Set()
			rareness.update(pokemonClusters.get(k))
'''