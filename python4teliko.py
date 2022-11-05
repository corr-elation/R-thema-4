from sklearn.linear_model import  LinearRegression
import numpy as np
import pandas


def euklideanDistance(point1, point2):
    dist = np.linalg.norm(point1 - point2)
    return dist

point1 = np.array([1,2,3,4,5,6])
point2 = np.array([1,2,3,4,5,6])
dist = euklideanDistance(point1, point2)
print(dist)

point1 = np.array([-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3])
point2 = np.array([0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3])
dist = euklideanDistance(point1, point2)
print(dist)

point1 = np.array([-0.5, 1, 7.3, 7, 9.4, -8.2])
point2 = np.array([1.25, 9.02, -7.3, -7, 5, 1.3])
dist = euklideanDistance(point1, point2)
print(dist)


point1 = np.array([0, 0, 0.2])
point2 = np.array([0.2, 0.2, 0])
dist = euklideanDistance(point1, point2)
print(dist)





xristis1 = np.array([25000, 14, 7])
xristis2 = np.array([42000, 17, 9])
xristis3 = np.array([55000, 22, 5])
xristis4 = np.array([27000, 13, 11])
xristis5 = np.array([58000, 21, 13])
xristes = [xristis1, xristis2, xristis3, xristis4, xristis5]
distances = []

for i in range(len(xristes)-1 ) :
    dist = euklideanDistance(xristes[i], xristis5)
    print(dist)
    distances.append(dist)
distances = list(distances)
minimum = min(distances)
finder = 0
for i in range(len(distances)):
    if distances[i] == minimum :
        finder = i
        break
print({finder + 1})
distances.append(0)






xristis1 = np.array([25000, 14, 7, distances[0]])
xristis2 = np.array([42000, 17, 9, distances[1]])
xristis3 = np.array([55000, 22, 5, distances[2]])
xristis4 = np.array([27000, 13, 11, distances[3]])
xristis5 = np.array([58000, 21, 13, distances[4]])


data = pandas.DataFrame([xristis1,xristis2,xristis3,xristis4,xristis5],["Xristis 1", "Xristis 2", "Xristis 3", "Xristis 4", "Xristis 5"],['minutes','sms', 'mb', 'distance'])
print(data)

X = data[['minutes']]
Y = data[['distance']]
regr = LinearRegression().fit(X, Y)
rsq = regr.score(X, Y)
print({rsq})

X = data[['minutes']]
Y = data[['sms']]
regr = LinearRegression().fit(X, Y)
rsq = regr.score(X, Y)
print({rsq})

X = data[['minutes']]
Y = data[['sms']]
regr = LinearRegression().fit(X, Y)
rsq = regr.score(X, Y)
print({rsq})
print("Minutes")
