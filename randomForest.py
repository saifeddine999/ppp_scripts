#! /usr/bin/python
import sys
import operator
import numpy as np
from sklearn.preprocessing import LabelEncoder  
from sklearn.ensemble import RandomForestRegressor

x = []
y = []
x_predict = []
x_all = []
app_nb = 0
nb = 0

fichier_predict = open("preduct-item.txt", "a")
with open("mapper-result.txt") as f:
	for line in f:
		data = line.strip().split("\t")
		if len(data) == 2:
			date, speed = data
			streetLook = date.strip().split(";")
			if len(streetLook) == 2:
				date, street = streetLook
				dateLook = date.strip().split(" ")
				if len(dateLook) == 2:
					date, hour = dateLook
					dayLook = date.strip().split("-")
					if len(dayLook) == 3:
						year, month, day = dayLook
						item = (float(year), float(month), float(day), float(hour), street)
						x_all.append(item)
						y.append(speed)
						app_nb+=1
						nb+=1

with open("predict-item.txt") as f:
	for line in f:
		data = line.strip().split("\t")
		if len(data) == 5:
			year, month, day, street = data
			item = (float(year), float(month), float(day), float(hour), street)
			x_all.append(item)
			nb+=1

X_all = np.asarray(x_all) 
Yl = np.asarray(y)
X_all[:, 4] = LabelEncoder().fit_transform(X_all[:,4]) 
X = X_all[app_nb-1, :]
predit_nb = nb - app_nb
X_predict = X_all[predit_nb, :]
regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1)
regressor.fit(X, Y)
print (regressor.predict(X_predict))
fichier_predict.close()
