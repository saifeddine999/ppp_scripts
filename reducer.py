#!/usr/bin/python
import sys
import operator
 
speedTotalNb = 0
speeds = {}
speeds_use = {}
speedTotalTmp = 0
speedTotalNbTmp = 0
speedAvg = 0
oldKey = None

fichier = open("reducer-result.txt", "a")
with open("mapper-result.txt") as f:
	for line in f:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue
	 
		thisKey, thisSpeed = data
		if oldKey and oldKey != thisKey:
			sorted_speeds = sorted(speeds.items(), key=operator.itemgetter(1))
			ratio = 0
			for key in speeds:
				if ratio < 0.9:
					ratio += float(speeds[key]/speedTotalNb)
					speeds_use[key] = speeds[key]
				else:
					break
			for key in speeds_use:
				speedTotalNbTmp += speeds_use[key] 
			for key in speeds_use:
				speedTotalNbTmp += speeds_use[key] 
				speedAvg += float(float(key)/speedTotalNbTmp)
			fichier.write("{0}\t{1}\n".format(oldKey, speedAvg))
			speedTotalNb = 0
			speeds = {}
			speeds_use = {}
			speedAvg = 0
			speedTotalTmp = 0
			speedTotalNbTmp = 0
	 
		oldKey = thisKey
		if thisSpeed in speeds:
			speeds[thisSpeed] += 1
		else:
			speeds[thisSpeed] = 1
		speedTotalNb += 1
	 
	if oldKey != None:
		sorted_speeds = sorted(speeds.items(), key=operator.itemgetter(1))
		ratio = 0
		for key in speeds:
			if ratio < 0.9:
				ratio += float(speeds[key]/speedTotalNb)
				speeds_use[key] = speeds[key]
			else:
				break
		for key in speeds_use:
			speedTotalNbTmp += speeds_use[key] 
		for key in speeds_use:
			speedTotalNbTmp += speeds_use[key] 
			speedAvg += float(key/speedTotalTmp)
		fichier.write("{0}\t{1}\n".format(oldKey, speedAvg))
		
fichier.close()