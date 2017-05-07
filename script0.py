import numpy as np
import matplotlib.pyplot as plt

X = list()
with open('dataset_anos.txt', 'rt') as reader:
    for point in reader:
        X.append(np.asarray(map(float, point.split(","))))

print(X)
print(len(X))
sum = 0

for i in X:
    sum =+ X[1]

print "El total es = " + str(sum)
