#! /usr/bin/python
import sys
from geopy.geocoders import Nominatim
import time
 
geolocator = Nominatim()
with open("out-parse.txt") as f:
	for line in f:
		data = line.strip().split("\t")
		if len(data) == 6:
			id, lat, lng, date, street, speed = data
			date2 = date[:13]
			pos = "{0}, {1}".format(lat, lng)
			#result = geolocator.reverse(pos)
			#details = result.raw['address']
			#street = details['road']
			#city = details['city']
			#country = details['country']
			#state = details['state']
			#destination = ', '.join((street, city, state, country))
			key = "{0};{1}".format(date2, street)
			print("{0}\t{1}\n".format(key, speed))
